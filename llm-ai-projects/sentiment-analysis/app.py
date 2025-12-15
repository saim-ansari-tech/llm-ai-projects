import os
from dotenv import load_dotenv
import openai
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def Sentiment_analysis(text):
  messages = [
      {"role" : "system", "content" : """ You are trained to analyze and detect the sentiment analysis of given text.
                                           if you are unsure of an answer, you can say "not sure" and recommend users to review manually"""},
      {"role" : "user", "content" : f""" Analyze the following text and determine if the sentiment is: positive or negative.
                                         Return answer in single word either positive or negative: {text}"""}
  ]


  response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messages,
                                                 max_tokens=1,
                                                 n=1,
                                                 temperature=0)
  response_text = response.choices[0].message.content.strip().lower()
  return response_text







 #Calling a function
input = "I hate fast food"
response = Sentiment_analysis(input)
print(input,': The Sentiment is', response)