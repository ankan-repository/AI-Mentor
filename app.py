from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyCr8PilqKP-zw8I1rA01UxQL3kQq2BAzpc"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def generate_explanation(topic, level="intermediate"):
    """Generate a personalized explanation for a given topic using the Gemini API."""
    prompt = f"Explain {topic} in a {level} way. Include key points."
    
    # Prepare the payload for the Gemini API
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    
    try:
        # Make a POST request to the Gemini API
        response = requests.post(GEMINI_API_URL, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # Extract the generated text from the response
        explanation = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No explanation received.")
        return explanation
    except Exception as e:
        print("Error generating explanation:", e)
        return f"Error generating explanation: {str(e)}"

@app.route("/explain", methods=["POST"])
def explain():
    data = request.json
    topic = data.get("topic")
    level = data.get("level", "intermediate")
    explanation = generate_explanation(topic, level)
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(debug=True)













# from flask import Flask, request, jsonify
# import openai  # Use Llama 3 or GPT-4 for explanation generation
# import json

# app = Flask(__name__)

# # Load AI Model (Llama 3 / GPT-4 API Integration)
# openai.api_key = "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"

# def generate_explanation(topic, level="intermediate"):
#     """Generate a personalized explanation for a given topic."""
#     prompt = f"Explain {topic} in a {level} way. Include key points."
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']

# @app.route("/explain", methods=["POST"])
# def explain():
#     data = request.json
#     topic = data.get("topic")
#     level = data.get("level", "intermediate")
#     explanation = generate_explanation(topic, level)
#     return jsonify({"explanation": explanation})

# if __name__ == "__main__":
#     app.run(debug=True)

# def generate_explanation(topic, level="intermediate"):
#     """Generate a personalized explanation for a given topic."""
#     prompt = f"Explain {topic} in a {level} way. Include key points."
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # or try using 'gpt-3.5-turbo' if GPT-4 is not available
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         # Log the error to the terminal for debugging
#         print("Error generating explanation:", e)
#         # Return a simple error message (you might also consider returning a proper HTTP error status)
#         return "Error generating explanation: " + str(e)





# from flask import Flask, request, jsonify
# import openai  # Use Llama 3 or GPT-4 for explanation generation
# from transformers import pipeline  # For OCR and speech-to-text
# import json

# app = Flask(__name__)

# # Load AI Model (Llama 3 / GPT-4 API Integration)
# openai.api_key = "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"

# def generate_explanation(topic, level="intermediate"):
#     """Generate a personalized explanation for a given topic."""
#     prompt = f"Explain {topic} in a {level} way. Include key points."
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']

# @app.route("/explain", methods=["POST"])
# def explain():
#     data = request.json
#     topic = data.get("topic")
#     level = data.get("level", "intermediate")
#     explanation = generate_explanation(topic, level)
#     return jsonify({"explanation": explanation})

# if __name__ == "__main__":
#     app.run(debug=True)


