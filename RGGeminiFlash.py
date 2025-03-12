import streamlit as st
import google.generativeai as genai


# Securely store the API key
api_key = "AIzaSyCG6ndOPAyCm-ePaSjktEtKUAaqTj0mpXs"
genai.configure(api_key=api_key)



# Model configuration
generative_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1024,
}


def generate_resume(name, job_title):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro", generation_config=generative_config)

    prompt = f"""Generate a professional resume for:
    Name: {name}
    Job Title: {job_title}
    """

    response = model.generate_content(prompt)

    return response.text if hasattr(response, "text") else "Error generating resume."


def clean_resume_text(text):
    replacements = {
        "[Add Email Address]": "[Your Email Address]",
        "[Add Phone Number]": "[Your Phone Number]",
        "[Add LinkedIn Profile URL (optional)]": "[Your LinkedIn URL (optional)]",
        "[University Name]": "[Your University Name]",
        "[Graduation Year]": "[Your Graduation Year]",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# Streamlit UI
st.title("Resume Generator")

name = st.text_input("Enter your name")
job_title = st.text_input("Enter your job title")

if st.button("Generate Resume"):
    if name and job_title:
        resume = generate_resume(name, job_title)
        cleaned_resume = clean_resume_text(resume)
        st.markdown("### Generated Resume")
        st.markdown(cleaned_resume)
    else:
        st.warning("Please enter both your name and job title.")
