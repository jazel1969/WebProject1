from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Welcome from root"

@app.route('/home')
def home():
    return "Welcome from home"

@app.route('/janusz')
def janusz():
    return "Janusz"

if __name__ == '__main__':
    app.run('localhost',5050)
