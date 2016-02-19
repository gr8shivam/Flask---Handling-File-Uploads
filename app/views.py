from .master import UserActions
from app import app

@app.route('/')
def start():
    user=UserActions()
    return user.reset()

@app.route('/home/', methods=['GET', 'POST'])
def main():
    user=UserActions()
    return user.upload_file()

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    user=UserActions()
    return user.delete_file(filename)
