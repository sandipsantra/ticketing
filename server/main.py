#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template,redirect,request
import requests



app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    result=''
    if request.method == 'POST':
        text=request.form.get('text')
        headers={'Content-Type':'text/plain'}
        url='http://10.140.46.189:5000/ticketing/'
        info = requests.post(url=url,headers=headers,data=text)
        result=info.json()
    return render_template('home.html',result=result)
    


