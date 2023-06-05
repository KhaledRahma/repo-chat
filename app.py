from flask import Flask, render_template, request
from main import run_chatbot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        response = run_chatbot(query)
        return render_template('index.html', query=query, response=response)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)