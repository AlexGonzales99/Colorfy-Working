import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import color

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/colorfilter')
def upload_form():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER']) 
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST']) #This is where images are uploaded
def upload_image():
    
    #gonna be real, not sure what this block accomplishes yet, but its necessary
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)	
	file = request.files['file']
	
 	#Checking if file is blank
	if file.filename == '':
		flash('No image selected for uploading') 
		return redirect(request.url)

	#if the file is one of the allowed types
	if file and allowed_file(file.filename): 
		filterType = request.form.get('filters')
		#
  		#
		#THIS IS WHERE THE FILE FILTERING NEEDS TO HAPPED
		#file = filter(file, filterType) #Important to resave the file here
		#
		#
		filename = secure_filename(file.filename)   
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template('Display.html', user_Image=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

def filter(f, filtertype): #Do filter stuff <--- return a new filtered file
	print(f.filename)	#Just So you know the file and color filter string are being passed propperly
	print(filtertype)
	#
	#
	#Call whatever color functions you want here
   #if filtertype = "red-green":
   #	doRedGreenFilter()	or something
	#
	#
	#return f #make sure to return the filtered file, currently saved as an object to you can do f.filename and f.path and stuff

if __name__ == "__main__":
    app.run()