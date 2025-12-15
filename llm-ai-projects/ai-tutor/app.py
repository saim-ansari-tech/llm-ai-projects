import os
from dotenv import load_dotenv
import openai
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Its your three subject tutor\n Made by Saim Ansari")



#Physics Tutor

#checking the subject
subject = input("Enter the subject name\t")
subject = subject.lower()

if subject == "physics":
  #defining a function
  def physics_tutor(question):

    messages = [
        {"role" : "system", "content" : """You are trained to answer any question regarding the Physics subject.
                                             The answer should be detailed and simple"""},
        {"role" : "user", "content" : f"""Analyze the question and generate the answer of the {question}.
                            first give the answer in two or three lines then breakdown the answer in key points"""}
    
    ]

    response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                     messages=messages,
                                                     max_tokens=1000,
                                                     n=1,
                                                     temperature=0.5)
    
    response_text = response.choices[0].message.content.strip().lower()
    return response_text
  
  #taking input to receive question from user
  question = input("Enter your question here\t")
  #calling the function
  answer = physics_tutor(question)
  print(answer)

#Computer Tutor



   

  
elif subject == "computer" or "computer science": 
    # Defining the function
    def comp_tutor(question):
       
        messages = [
            {"role" : "system", "content" : """You are trained to answer any question regrading the computer science subject.
                                        The answer should be detailed and simple"""},
            {"role" : "user", "content" : f"""Analyze the {question} and generate the answer of the {question}.
                                          first give the answer in two or three lines then breakdown the answer in key points according to the question."""}
        ]

        response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                             messages=messages,
                                             max_tokens = 1000,
                                             n=1,
                                             temperature=0.5)         
        response_text = response.choices[0].message.content.strip().lower()
        return response_text
    
    #taking input to recieve question from the user
    question = input("Enter the question here\t")
    #calling a function
    answer = comp_tutor(question)
    print(answer)

#mathematics tutor





elif subject == "math" or "maths" or "mathematics":
   
   #defining a function
   def maths_tutor(question):

    messages = [
        {"role" : "system", "content" : """You are trained to answer any question regarding the mathematics subject.
                                            The answer should be detailed and short."""},
        {"role" : "user", "content" : f"""Analyze the question and generate the answer of the {question}.
                                          first answer the question themn breakdown the answer into steps."""}                                       
    ]
    response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                     messages=messages,
                                                     n=1,
                                                     max_tokens=1000,
                                                     temperature=0.6)
    response_text = response.choices[0].message.content.strip().lower()
    return response_text
   
   #taking input to recieve question from the user

   question = input("Enter the question here\t")
   










    
                                                     