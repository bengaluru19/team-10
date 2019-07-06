from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/client.html')
def client_page():
    return render_template('client.html')

@app.route('/survey.html')
def survey():
    return render_template('survey.html')


if __name__ == '__main__':
    app.run()