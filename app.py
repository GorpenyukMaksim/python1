from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Carpe diem - лови момент!"

if __name__ == '__main__':
    app.run(debug=True)