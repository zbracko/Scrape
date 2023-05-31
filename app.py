import streamlit as st
import google.generativeai as palm

# Configure the generative AI model
palm.configure(api_key="AIzaSyDGfvSdyOOtM7WGyRA7-eK3PqVEuw8gnE4")

# Define the Streamlit app
def main():
    # Set the title of the app
    st.title("Text Generation")

    # Set the default parameters for text generation
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [
            {"category":"HARM_CATEGORY_DEROGATORY","threshold":1},
            {"category":"HARM_CATEGORY_TOXICITY","threshold":1},
            {"category":"HARM_CATEGORY_VIOLENCE","threshold":2},
            {"category":"HARM_CATEGORY_SEXUAL","threshold":2},
            {"category":"HARM_CATEGORY_MEDICAL","threshold":2},
            {"category":"HARM_CATEGORY_DANGEROUS","threshold":2}
        ],
    }

    # Display the text generation form
    prompt = st.text_area("Enter Prompt", height=100)
    temperature = st.slider("Temperature", min_value=0.1, max_value=1.0, step=0.1, value=0.7)
    top_k = st.slider("Top K", min_value=1, max_value=100, step=1, value=40)
    top_p = st.slider("Top P", min_value=0.1, max_value=1.0, step=0.1, value=0.95)

    if st.button("Generate Text"):
        # Update the parameters with user inputs
        defaults['temperature'] = temperature
        defaults['top_k'] = top_k
        defaults['top_p'] = top_p

        # Generate text using the model and prompt
        response = palm.generate_text(**defaults, prompt=prompt)

        # Display the generated text
        st.code(response.result)

if __name__ == "__main__":
    main()
