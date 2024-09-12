from flask import Flask, jsonify
from flask_cors import CORS
from markupsafe import escape
from openai import OpenAI
from icecream import ic as dd

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

base_url = "/api/v1"

@app.route(f"{base_url}/question/plural")
def hello_world():
    ## gets API Key from environment variable OPENAI_API_KEY
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="1",
    )

    completion = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content":
        '''
            Give me randomize sample of singular and plural
        ''',
        },
    ],
    )

    return jsonify(
        {
            'message': completion.choices[0].message.content,
            'status': 200,
            'success': 'ok'
        }
    )

@app.route(f"{base_url}/sample/<int:id>")
def sample(id):
    return jsonify({
            "message":"Singular:\n1. Dog\n2. Chair\n3. Table\n4. Phone\n5. Car\n\nPlural: \n1. Dogs\n2. Chairs\n3. Tables\n4. Phones\n5. Cars",
            "status":200
        })

if __name__ == "__main__":
    app.run(debug=True, port="8000")
