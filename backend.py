from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

@app.route('/api/typing', methods=['POST'])
def typing_effect():
    data = request.json  # Get user input
    text = data.get("text", "")
    
    # Simulate typing animation (basic logic)
    animated_text = " ".join([char for char in text])  # Example effect
    
    return jsonify({"animated_text": animated_text})

if __name__ == '__main__':
    app.run(debug=True)
