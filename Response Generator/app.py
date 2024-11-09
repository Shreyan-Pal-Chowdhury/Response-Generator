import streamlit as st
import google.generativeai as genai  # Assuming "google.generativeai" is the wrong import. Please replace with the correct import path.
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config = generation_config,
    safety_settings=safety_settings
)

st.set_page_config(layout="wide")
st.title('Your AI Writing Fellow....')
st.subheader("VlogVista is now your writing partner")

with st.sidebar:
    st.title("Input your blog details")
    st.subheader("enter details for your vlogs")
    blog_title = st.text_input("Enter Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=250)
    num_images = st.number_input("Number of images", min_value=1, max_value=5, step=1)
    prompt = f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."

submit_button = st.button("Generate Blog")
if submit_button:
    #st.image("")
    response = model.generate_content(prompt)
    st.write(response.text)






    