import os
from flask import *
from flask import Flask,render_template,request,flash,redirect,url_for,session,session


images=os.path.join('static','images','icons')
photos=os.path.join('static','images','members')
event_1=os.path.join('static','images','event1')
app=Flask(__name__)
app.config['icons'] = images
app.config['members'] = photos
app.config['event1'] = event_1


t1 = os.path.join(app.config['icons'], 'ECELL LOGO.png')
t2 = os.path.join(app.config['icons'], 'conclave16.png')
t3 = os.path.join(app.config['icons'], 'E_week16.png')
t4 = os.path.join(app.config['icons'], 'e_week18.jpg')

l1 = os.path.join(app.config['icons'], 'lamp.png')
l2 = os.path.join(app.config['icons'], 'light.png')

tm1 = os.path.join(app.config['members'], 'karthikaa.jpg')
tm2 = os.path.join(app.config['members'], 'gokulakrishnan.jpg')
tm3 = os.path.join(app.config['members'], 'lokchandar.jpg')
tm4 = os.path.join(app.config['members'], 'riyazmohammed.jpg')
tm5 = os.path.join(app.config['members'], 'kesavaraj.jpg')
tm6 = os.path.join(app.config['members'], 'subakrishna.jpg')
tm7 = os.path.join(app.config['members'], 'suman.jpg')
tm8 = os.path.join(app.config['members'], 'kaavyaagith.jpg')
tm9 = os.path.join(app.config['members'], 'shankar.jpg')
tm10 = os.path.join(app.config['members'], 'madhumita.jpg')
tm11 = os.path.join(app.config['members'], 'vejaysundaram.jpg')
tm12 = os.path.join(app.config['members'], 'kokilappriya.jpg')
tm13 = os.path.join(app.config['members'], 'deepak.jpg')
tm14 = os.path.join(app.config['members'], 'shephrine.jpg')
tm15 = os.path.join(app.config['members'], 'kathirelakkiyan.jpg')
tm16 = os.path.join(app.config['members'], 'joelsam.jpg')
tm17 = os.path.join(app.config['members'], 'subash.jpg')
tm18 = os.path.join(app.config['members'], 'nitin.jpg')
tm19 = os.path.join(app.config['members'], 'vaishnavi.jpg')
tm20 = os.path.join(app.config['members'], 'prabathateni.jpg')
tm21 = os.path.join(app.config['members'], 'haribalaji.jpg')
tm22 = os.path.join(app.config['members'], 'saiganesh.jpg')
tm23 = os.path.join(app.config['members'], 'manish.jpg')
tm24 = os.path.join(app.config['members'], 'keerthana.jpg')
tm25 = os.path.join(app.config['members'], 'soorajnikam.jpg')
tm26 = os.path.join(app.config['members'], 'vaishnavisri.jpg')

g1 = os.path.join(app.config['event1'],'photo1.png')
g2 = os.path.join(app.config['event1'],'photo2.png')
@app.route('/')
def home():
    return render_template('index.html',img1=l1,img2=l2)

@app.route('/masterpiecemoments')
def masterpiecemoments():
    return render_template('gallery.html',photo1=g1,photo2=g2)


@app.route('/team')
def teampage():
    return render_template('team.html',img1=tm1,img2=tm2,img3=tm3,img4=tm4,img5=tm5,img6=tm6,img7=tm7,img8=tm8,img9=tm9,img10=tm10,img11=tm11,img12=tm12,img13=tm13,img14=tm14,img15=tm15,img16=tm16,img17=tm17,img18=tm18,img19=tm19,img20=tm20,img21=tm21,img22=tm22,img23=tm23,img24=tm24,img25=tm25,img26=tm26)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',img1=t1,img2=t2,img3=t3,img4=t4)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",use_reloader=False)