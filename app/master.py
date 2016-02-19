import os
from app.config import ALLOWED_EXTENSIONS
from flask import render_template, request, redirect
from werkzeug import secure_filename
from os import listdir
from os.path import isfile, join
from app import app

class UserActions():
    def allowed_file(self,filename):
            return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def upload_file(self):
        if request.method == 'POST':
            files = request.files.getlist('file[]')
            responses={}
            for file in files:
                responses.update(self.handle_file(file))
            return render_template('upload.html',responses=responses,user=self)
        return render_template('upload.html',user=self)

    def handle_file(self,file):
        folder = app.config['UPLOAD_FOLDER']
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            response={filename: 1}
            return response
        else:
            response={file.filename: 0}
            return response

    def fetch_files(self):
        folder = app.config['UPLOAD_FOLDER']
        allfiles = [f for f in listdir(folder) if isfile(join(folder, f)) if not f.startswith('.')]
        if allfiles:
            return allfiles

    def delete_file(self,filename):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/home/')

    def reset(self):
        folder = app.config['UPLOAD_FOLDER']
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return render_template('main.html')