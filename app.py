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













