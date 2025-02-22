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






