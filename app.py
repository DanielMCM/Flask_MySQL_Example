from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import xmltodict
import os

os.system('./helpers/create_database.py')

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'phpmyadmin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'P@ssword'
app.config['MYSQL_DATABASE_DB'] = 'exercise'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/daniel_minguez")
def showSignUp():
    return render_template('signup.html')

@app.route('/daniel_minguez/signUp',methods=['POST'])
def signUp():
    print(request.form)
    # read the posted values from the UI
    cont = contact(request.form['firstname'],request.form['lastname'],request.form['address'],request.form['email'],request.form['phone'])

    return cont.insert(mysql)
    


@app.route('/daniel_minguez/uploader', defaults={'file': None}, methods = ['POST','GET'])
@app.route('/daniel_minguez/uploader/<file>', methods = ['POST','GET'])
def upload_file(file):

    if request.method == 'POST':
        f = xmltodict.parse(request.files['file'])
        return f
    
    else:
        if file != "":

            path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'htdocs\\' + file)
            g_cont = contact(pth = path)

            if g_cont.validate():
                g_cont.insert(mysql)

            return "File loaded succesfully!"
        else:
            return "No file provided"


@app.route("/phpmyadmin")
def hello():
    return "Phpmyadmin page!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='localhost', port=port)