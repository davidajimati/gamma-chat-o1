import streamlit as st
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, trim_messages, BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from streamlit_chat_widget import chat_input_widget
from streamlit_extras.bottom_container import bottom
from typing_extensions import Annotated, TypedDict
from typing import Sequence
import groq

GROQ_API_KEY = st.secrets['GROQ_API_KEY']
client = groq.Client(api_key=GROQ_API_KEY)

# session creation
if 'messages' not in st.session_state:
    st.session_state.messages = [] 
    
if 'memory' not in st.session_state:
    st.session_state.memory = MemorySaver()

# initialize the chat model 
model = init_chat_model(
    'llama-3.3-70b-specdec',
    model_provider='groq',
)

st.title('Your Chatbot 😶‍🌫️')

# Character Provision
CHARACTERS = [
    'Ruthless Pirate',
    'Otaku',
    'Anime Weeb',
    'Quantum Scientist',
    'Custom Character'
]

chosen_character = st.sidebar.selectbox('Select Character 👺', CHARACTERS)
if chosen_character == 'Custom Character':
    chosen_character = None
    custom_character = st.sidebar.text_input('Enter Character Name 🥸')
    if custom_character:
        chosen_character = custom_character
    

# getting the user query
def transcribe_audio(audio_file):
    with open(audio_file, "rb") as file:
        response = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=file
        )
    return response.text

chat_placeholder = st.container()

with bottom():
    user_input = chat_input_widget()
    
    query = ''
    if user_input:
        if 'text' in user_input:
            query = user_input['text']
        elif 'audioFile' in user_input:
            with open("temp_audio.wav", "wb") as f:
                f.write(bytes(user_input["audioFile"]))
            query = transcribe_audio("temp_audio.wav")
            

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are {character}. Stay fully in character at all times and respond exactly as {character} would. Answer all questions directly, without internal thoughts, explanations, or reasoning—just pure, in-character responses."),
    MessagesPlaceholder(variable_name='messages'),
])

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    character: str

# Defining the langgraph workflow
workflow = StateGraph(state_schema=State)

def call_model(state: State):   
    # trin the messages that are stored as memory     
    trimmed_messages = trim_messages(
        messages = state['messages'],
        max_tokens=100,
        strategy='last',
        token_counter=model,
        include_system=True,
        allow_partial=False,
        start_on='human',
    )
    
    # use those messages as prompt
    prompt = prompt_template.invoke({
        'messages': trimmed_messages,
        'character': state['character']
    })
    
    response = model.invoke(prompt)
    return {'messages': [response]}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = st.session_state.memory
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

for message in st.session_state.messages:
     st.chat_message(message['role']).markdown(message['content'])
     
if len(query) > 0:
    st.chat_message('user').markdown(query)
    st.session_state.messages.append({'role': 'user', 'content': query})
    
    input_message = [HumanMessage(query)]
    past_messages = st.session_state.messages + input_message   
    
    output = app.invoke(input={
            'messages': past_messages,
            'character': chosen_character,
        }, config=config)
    current_output = output['messages'][-1].content

    
    if current_output:
        st.chat_message('assistant').markdown(current_output)
        st.session_state.messages.append({'role': 'assistant', 'content': current_output})
    else:
        st.error('Something went wrong! Please try again.') 

    
