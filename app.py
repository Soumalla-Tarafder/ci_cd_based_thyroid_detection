from flask import Flask
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'Hello, Soumalla!'

if __name__ == '__main__':
    app.run(debug=True)