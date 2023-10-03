from flask import *
from flask import Flask,render_template,request,flash,redirect,url_for,session,session

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",use_reloader=False)