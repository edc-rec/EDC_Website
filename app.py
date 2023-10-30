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

l1 = os.path.join(app.config['icons'], 'lamp.png')
l2 = os.path.join(app.config['icons'], 'light.png')

tm1 = os.path.join(app.config['icons'], 'conclave16.png')
tm2 = os.path.join(app.config['icons'], 'conclave16.png')
tm3 = os.path.join(app.config['icons'], 'conclave16.png')
tm4 = os.path.join(app.config['icons'], 'conclave16.png')
tm5 = os.path.join(app.config['icons'], 'conclave16.png')
tm6 = os.path.join(app.config['icons'], 'conclave16.png')
tm7 = os.path.join(app.config['icons'], 'conclave16.png')
tm8 = os.path.join(app.config['icons'], 'conclave16.png')
tm9 = os.path.join(app.config['icons'], 'conclave16.png')
tm10 = os.path.join(app.config['icons'], 'conclave16.png')
tm11 = os.path.join(app.config['icons'], 'conclave16.png')
tm12 = os.path.join(app.config['icons'], 'conclave16.png')

@app.route('/')
def home():
    return render_template('index.html',img1=l1,img2=l2)


@app.route('/team')
def teampage():
    return render_template('team.html',img1=tm1,img2=tm2,img3=tm3,img4=tm4,img5=tm5,img6=tm6,img7=tm7,img8=tm8,img9=tm9,img10=tm10,img11=tm11,img12=tm12)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',img1=t1,img2=t2,img3=t3,img4=t4)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",use_reloader=False)