import os
from dotenv import load_dotenv
import openai
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog(topic):
    messages =  [
        {"role" : "system", "content" : """You are trained to analyze the given topic and generate the blog.
                                            The blog should be maximun 3000 words."""},
        {"role" : "user", "content" : f"""Analyze the topic and generate the blog. The topic is {topic}.
                                          The topic must follow the following format.
                                       1) Title (It must be in one line)
                                       2) Introduction (Give introduction about the topic)
                                       3) Engaging Content (Provide valuable and relavant information.
                                                            Use the conversational tone to connect with the audience.
                                                            Break content into easy section with subheadings.)
                                       4) Visual Appeal (Use images, infographics or videos to break up the text.
                                                          Insure the blog is visually appealing and easy to read.)
                                       5) Concise and clear writing (Keep sentences and paragraphs concise.
                                                                Use clear language and avoid jorgon unless your audience is familiar with it.)
                                       6) Use keywords (Incorporate and relevant keywords to improve search engine optimazation (SEO).
                                                        Dont overstuff keywords; maintain a natural fkow of writing.)
                                       7) Structued Format (Organize your content with a logical flow.
                                                            Use bullets points or number list for easy readability.)
                                       8) Unique Perspective or Angle (Offer a unique perspective on the topic.
                                                                        Share personal experiences.)
                                       9) Engage with Audience (Encourage comments, questions or discussions.
                                                                Responds to comments to foster a sense of community.)
                                      10) Conclusion (Summarize the main points.
                                                      End with a strong conclusion or a call to action.)"""}
                                       
                                                           
    ]
    response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                      messages=messages,
                                                      max_tokens = 1500,
                                                      n=1,
                                                      temperature=0.8)
    response_text = response.choices[0].message.content.strip().lower()
    return response_text

# Using Streamlit
st.title("Its Saim Ansari Product")
st.title("Blog Post Generator")
model = "gpt-3.5-turbo"
topic = st.text_input("Enter your Topic here")
if st.button('submit'):
    with st.spinner('Processing in progress'):
       response=generate_blog(topic)
       st.success ('Processing complete')
    st.write(response)
