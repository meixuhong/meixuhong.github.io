from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/<string:name1>/<int:id>')    
def hello_user(name1,id):
    return 'Hello {} {}'.format(name1,id)

if __name__ == "__main__":
    app.run(debug=True)    