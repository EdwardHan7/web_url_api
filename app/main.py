from flask import Flask, request, jsonify
from app.my_cryptography import Cryptography
import re
#regular expression

app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to my Flask app!"

DEFAULT_BASE_URL = "https://example.co"
DEFAULT_MAX_LENGTH = 6

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    long_url = request.json.get('long_url')
    
    if not long_url:
        return jsonify({"error": "Original URL is empty or null."}), 400

    if not re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', long_url):
        return jsonify({"error": "Original URL format is invalid."}), 400
    
    encrypted = Cryptography.encrypt_url(long_url, DEFAULT_MAX_LENGTH)
    short_url = f"{DEFAULT_BASE_URL}/{encrypted}"
    #f-string
    return jsonify({"short_url": short_url})

if __name__ == "__main__":
    app.run(debug=True)
