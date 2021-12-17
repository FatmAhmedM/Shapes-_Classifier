import flask
from flask import Flask, render_template, request, url_for , redirect
import os
from model import model



   
image_folder ="static\userphotos"

app = Flask( __name__, template_folder= "templates", static_folder= "static")

app.config["IMAGE_UPLOADS"] = image_folder






@app.route('/')
def hello():
  return render_template('z.html')


@app.route('/dis', methods = ['POST', 'GET'])
def he():
  global text
  text = request.form['text']
  return render_template('o.html', text = text)  
 
   
@app.route('/dd/', methods = ['POST', 'GET'])
def ano():
  
  image = request.files["image"]
  image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
  model_pre, info = model(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
  return render_template('o.html' ,uploaded_image=image.filename , text = text , model_pre=model_pre , info = info)


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):

  from flask import send_from_directory
  return send_from_directory(app.config["IMAGE_UPLOADS"], filename)




if __name__ == '__main__':
  app.run(debug= True)
