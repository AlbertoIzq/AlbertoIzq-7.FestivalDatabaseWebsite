from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/en/home")
def en_home():
    return render_template("en-home.html")

@app.route("/es/home")
def es_home():
    return render_template("es-home.html")

@app.route("/en/success", methods = ['POST'])
def en_success():
    if request.method == 'POST':
        email = request.form["form_email"]
        age = request.form["form_age"]
        gender = request.form["form_gender"]
        music_genre = request.form["form_music_genre"]
        festivals_number = request.form["form_festivals_number"]
        festivals_age = request.form["form_festivals_age"]
        festival_name = request.form["form_festival_name"]
        festival_music_genre = request.form["form_festival_music_genre"]
        yesno = request.form["form_yesno"]
        festival_name_2021 = request.form["form_festival_name_2021"]

        print(email, age, gender, music_genre, festivals_number, festivals_age, festival_name, festival_music_genre,
              yesno, festival_name_2021)
    return render_template("en-success.html")

@app.route("/es/success", methods = ['POST'])
def es_success():
    if request.method == 'POST':
        email = request.form["form_email"]
        age = request.form["form_age"]
        gender = request.form["form_gender"]
        music_genre = request.form["form_music_genre"]
        festivals_number = request.form["form_festivals_number"]
        festivals_age = request.form["form_festivals_age"]
        festival_name = request.form["form_festival_name"]
        festival_music_genre = request.form["form_festival_music_genre"]
        yesno = request.form["form_yesno"]
        festival_name_2021 = request.form["form_festival_name_2021"]

        print(email, age, gender, music_genre, festivals_number, festivals_age, festival_name, festival_music_genre,
              yesno, festival_name_2021)
    return render_template("es-success.html")

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5003) # port = 5000, by default