from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploaded_file():
   if request.method == 'POST':
      f = request.files['file']
      os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
      f.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(f.filename)))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
