import os
from flask import *
from flask import Flask,render_template,request,flash,redirect,url_for,session,session


images=os.path.join('static','images')
app=Flask(__name__)
app.config['icons'] = images
t1 = os.path.join(app.config['icons'], 'ECELL LOGO.png')
t2 = os.path.join(app.config['icons'], 'conclave16.png')
t3 = os.path.join(app.config['icons'], 'E_week16.png')
t4 = os.path.join(app.config['icons'], 'e_week18.jpg')



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',img1=t1,img2=t2,img3=t3,img4=t4)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",use_reloader=False)