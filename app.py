import streamlit as st
import google.generativeai as genai
import creds
genai.configure(api_key=creds.api_key)

sys_prompt = """You are an adavanced data science tutor who can code in python as well. You can only resolve any AI and ML and Data Science related queries. In case if someone as queries which are not relevant, 
            politely tell them to ask relevant queries only."""
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

st.title("Data Science Tutor Application")
user_prompt = st.text_input("Enter Your Query: ", placeholder="Type Your Query here...")
btn_click = st.button("Generate Answer")

if btn_click:
    response = model.generate_content(user_prompt)

    # Extract the text from the response object
    try:
        generated_text = response.candidates[0].content.parts[0].text
        st.write(generated_text)  # Display the text in Streamlit
    except AttributeError:
        st.write("An error occurred while processing the response.")
        print(response)  # Print the full response for debugging

