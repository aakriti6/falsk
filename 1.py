from flask import Flask,render_template
from flask import request

app = Flask(__name__)



@app.route("/")
def pro():
    return "hello world"
    #return render_template('index.html')

@app.route("/123")
def test2():
    data=request.args.get('x')
    return "this is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(debug=True)