import os
from dotenv import load_dotenv
import openai
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def personal_assistant(question):
  messages = [
      {"role" : "system", "content" : f"""You are my personal assistant. You only know information that i will give you.
                                          Analyze the {question} and generate the answer in a more presized way"""},
      {"role" : "user", "content" : f"""Analyze the {question} and answer the question from the following data. If user ask's a question that is not mentioned in the following then you will reply "I don't have any information about this."
                                        My name is Muhammad Saim Ansari. I lived in Pakistan. My passion is Artificial Intelligence and Robotics. And Now I am currently inrolled in Bahria University Islamabad in BS Robotics And Intelligent System. at Islamabad. 
                                        My mentor name is Irfan Malik who is the CEO of Xeven Solution company. I am very inspired with this man. My religion is Islam."""}
  ]
  response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=messages,
                                            max_tokens = 100,
                                            n=1,
                                            temperature=0.1)
  response_text =  response.choices[0].message.content.strip().lower()
  return response_text
