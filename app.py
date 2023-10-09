import os
from flask import *
from flask import Flask,render_template,request,flash,redirect,url_for,session,session


images=os.path.join('static','images')
app=Flask(__name__)
app.config['icons'] = images
timeline2 = os.path.join(app.config['icons'], '2017.jpg')



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',img1=timeline2)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",use_reloader=False)