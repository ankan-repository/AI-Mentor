import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import base64

# Configure Gemini API Key
genai.configure(api_key="AIzaSyCr8PilqKP-zw8I1rA01UxQL3kQq2BAzpc")

def generate_explanation(topic, level="intermediate"):
    """Generate explanation using Gemini API."""
    prompt = f"Explain {topic} in a {level} way. Include key points."
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" model
        response = model.generate_content(prompt)
        return response.text  # Access the generated text using `.text`
    except Exception as e:
        return "Error generating explanation: " + str(e)


def generate_summary(text):
    """Generate a concise summary of the explanation."""
    summary_prompt = f"Summarize the following explanation:\n{text}"
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" model
        response = model.generate_content(summary_prompt)
        return response.text  # Access the generated text using `.text`
    except Exception as e:
        return "Error generating summary: " + str(e)


def create_pdf(content, filename="explanation.pdf"):
    """Create and return a downloadable PDF file."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf_output = f"./{filename}"
    pdf.output(pdf_output)
    return pdf_output


def get_pdf_download_link(pdf_path):
    """Generate a Streamlit download button for the PDF."""
    with open(pdf_path, "rb") as pdf_file:
        b64 = base64.b64encode(pdf_file.read()).decode()
    return f'<a href="data:application/pdf;base64,{b64}" download="explanation.pdf">📄 Download Explanation</a>'

# Streamlit UI
st.set_page_config(page_title="AI Mentor", layout="centered")

# Custom Background & Styling
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1485470733090-0aae1788d5af?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .main-title {
            color: white;
            text-align: center;
            font-size: 48px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .sidebar .sidebar-content {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #1f77b4;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
        .stButton button:hover {
            background-color: #165d8f;
        }
        </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='main-title'>📚 AI Mentor: Learn Smarter</h1>", unsafe_allow_html=True)

# User Input
st.sidebar.header("Customize Explanation")
topic = st.sidebar.text_input("Enter Topic:")
level = st.sidebar.selectbox("Choose Complexity:", ["Beginner", "Intermediate", "Advanced"])

if st.sidebar.button("Generate Explanation"):
    if topic:
        explanation = generate_explanation(topic, level)
        summary = generate_summary(explanation)
        
        # Display Explanation
        st.subheader("📖 Explanation")
        st.write(explanation)
        
        # Summary & Key Takeaways
        st.subheader("🔑 Summary & Key Takeaways")
        st.write(summary)
        
        # Generate PDF & Download
        pdf_path = create_pdf(f"Topic: {topic}\n\nExplanation:\n{explanation}\n\nSummary:\n{summary}")
        st.markdown(get_pdf_download_link(pdf_path), unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic.")






# import streamlit as st
# import requests

# # Set page configuration
# st.set_page_config(
#     page_title="Gemini-Powered Personalized Tutor",
#     page_icon="📚",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# # Add a background image
# def add_bg_from_url():
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("https://images.unsplash.com/photo-1533134486753-c833f0ed4866?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
#             background-size: cover;
#             background-position: center;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_from_url()

# # Update the title to reflect Gemini-powered tutoring
# st.title("Gemini-Powered Personalized Tutor")

# # User Input for Topic and Difficulty Level
# topic = st.text_input("Enter a topic:")
# level = st.selectbox("Select difficulty level:", ["beginner", "intermediate", "advanced"])

# if st.button("Generate Explanation"):
#     # Define the endpoint URL (adjust if your backend runs on a different address/port)
#     url = "http://127.0.0.1:5000/explain"
#     payload = {"topic": topic, "level": level}
    
#     try:
#         response = requests.post(url, json=payload, timeout=10)  # Add a timeout
#         response.raise_for_status()  # Raise an error for bad status codes
#         data = response.json()
#         explanation = data.get("explanation", "No explanation received.")
        
#         # Display the explanation
#         st.write("### Explanation:")
#         st.write(explanation)

#         # Add a section for Summary & Key Takeaways
#         st.write("### Summary & Key Takeaways:")
#         st.write("Here are the main points from the explanation:")
#         st.write("- Point 1: [AI-generated summary]")
#         st.write("- Point 2: [AI-generated summary]")
#         st.write("- Point 3: [AI-generated summary]")

#         # Add an AI-generated illustration
#         st.write("### AI-Generated Illustration:")
#         illustration_url = "https://via.placeholder.com/600x400.png?text=AI+Generated+Illustration"
#         st.image(illustration_url, caption="AI-Generated Illustration", use_column_width=True)

#         # Add a button to save and download the explanation
#         st.write("### Save & Download Explanation:")
#         explanation_bytes = explanation.encode("utf-8")
#         b64 = base64.b64encode(explanation_bytes).decode()
#         href = f'<a href="data:file/txt;base64,{b64}" download="explanation.txt">Download Explanation</a>'
#         st.markdown(href, unsafe_allow_html=True)

#     except requests.exceptions.RequestException as e:
#         st.error(f"Failed to connect to the server: {e}")



# import streamlit as st
# import requests

# # Update the title to reflect Gemini-powered tutoring
# st.title("Gemini-Powered Personalized Tutor")

# # User Input for Topic and Difficulty Level
# topic = st.text_input("Enter a topic:")
# level = st.selectbox("Select difficulty level:", ["beginner", "intermediate", "advanced"])

# if st.button("Generate Explanation"):
#     # Define the endpoint URL (adjust if your backend runs on a different address/port)
#     url = "http://127.0.0.1:5000/explain"
#     payload = {"topic": topic, "level": level}
    
#     try:
#         response = requests.post(url, json=payload)
#         if response.status_code == 200:
#             data = response.json()
#             explanation = data.get("explanation", "No explanation received.")
#             st.write("### Explanation:")
#             st.write(explanation)
#         else:
#             st.error(f"Error generating explanation. Status code: {response.status_code}")
#     except Exception as e:
#         st.error(f"Error generating explanation: {e}")
