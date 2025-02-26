# Task Breakdown for Mandatory Features

Okay, so I tried to break it down simply, with a focus on the mandatory features first and using the roles we introduced ourselves with. Since the deadline is Friday noon, we can give ourselves until Wednesday or, at the latest, Thursday to have the MVP of the chatbot with the mandatory features.

This is the general description of each task (just a guideline, you can follow whatever process fits you best as long as it works):

---

## **1. Project Setup and Initialization**

### **Task 1: Set up the development environment**
- Install dependencies: **Streamlit**, **LangChain**, **LangGraph**, **Groq**, and any other required libraries.  
- Create a shared GitHub repository for collaboration.  
- Assign roles and ensure everyone has access to the repo.  

**Owner:** Anyone

### **Task 2: Initialize the Streamlit app**
- Create a basic **Streamlit** app with a placeholder UI for character selection and chat interface.  
- Ensure the app runs locally and can be tested.  

**Owner:** 1 Fullstack Engineer

---

## **2. Chatbot Logic with LangChain & Groq**  
This is the core task for the mandatory features.

### **Task 3: Integrate Groq with LangChain**
- Set up **Groq API** access and integrate it with **LangChain** for text-based interactions.  
- Create a basic chatbot pipeline that takes user input and generates responses using **Groq**.  

**Owner:** 2 Data/ML Engineers  

### **Task 4: Implement Character Selection**
- Define a set of pre-defined AI characters (e.g., "Friendly Assistant", "Sarcastic Bot", etc.).  
- Modify the chatbot logic to dynamically adjust responses based on the selected character.  

**Owner:** 1 Data/ML Engineer + 1 Backend Engineer  

### **Task 5: Build the Chat Interface**
- Integrate the chatbot logic into the **Streamlit** app.  
- Create a simple UI for character selection and text-based conversation.  

**Owner:** 2 Fullstack Engineers  

---

## **3. Deployment**

### **Task 6: Deploy the Streamlit App**
- Use **Streamlit Community** to deploy the app.  
- Ensure the app is accessible via a public URL.  

**Owner:** 1 Backend Engineer  

### **Task 7: Test Deployment**
- Verify that the deployed app works as expected and that everyone's code integrates fine with no merge conflicts.  
- Fix any deployment-related issues (e.g., environment variables, API keys).  

**Owner:** 1 Fullstack Engineer + ML Engineer / Everyone

---

## **4. Documentation**

### **Task 8: Write the Report**
- Document the approach, design decisions, challenges, and key features (possibly add a bit of storytelling).  
- Include the deployed URL in the report.  

**Owner:** Everyone documents what they have done and their reasoning in the `.readme` / discussions / commit messages, then 1 person compiles that into a report.
