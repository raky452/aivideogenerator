import os

from flask import Flask
from flask import render_template
from flask import request

import openai

app = Flask(__name__)

@app.route('/get_story')
def get_story():
    storyline = request.args.get('storyline')
    openai.api_key = "Add Your Key"

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=storyline,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message

@app.route('/')
def home():
    return render_template('homepage.html',version=1)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))