from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/festival_survey'
db = SQLAlchemy(app)

message_email_en = "Seems like I've got something from that email address already"
message_email_es = "Parece que alguien ya ha introducido datos con ese correo electrónico"

message_age_en = "Your age cannot be less than when you first went to a festival, can it?"
message_age_es = "Tu edad no puede ser menor que la que tenías cuando fuiste por primera vez a un festival, ¿no?"

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(8))
    music_genre = db.Column(db.String(12))
    festival_number = db.Column(db.Integer)
    festival_age = db.Column(db.Integer)
    festival_name = db.Column(db.String(120))
    festival_music_genre = db.Column(db.String(12))
    yesno_2021 = db.Column(db.String(5))
    festival_name_2021 = db.Column(db.String(120))

    def __init__(self, email, age, gender, music_genre, festival_number, festival_age,
                 festival_name, festival_music_genre, yesno_2021, festival_name_2021):
        self.email = email
        self.age = age
        self.gender = gender
        self.music_genre = music_genre
        self.festival_number = festival_number
        self.festival_age = festival_age
        self.festival_name = festival_name
        self.festival_music_genre = festival_music_genre
        self.yesno_2021 = yesno_2021
        self.festival_name_2021 = festival_name_2021

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
        festival_number = request.form["form_festival_number"]
        festival_age = request.form["form_festival_age"]
        festival_name = request.form["form_festival_name"]
        festival_music_genre = request.form["form_festival_music_genre"]
        yesno_2021 = request.form["form_yesno_2021"]
        festival_name_2021 = request.form["form_festival_name_2021"]

        if db.session.query(Data).filter(Data.email==email).count() == 0: # count() counts how many values satisfy this condition
            data = Data(email, age, gender, music_genre, festival_number, festival_age,
                        festival_name, festival_music_genre, yesno_2021, festival_name_2021)
            db.session.add(data) # You add the variable created before for the database to recognize the values
            db.session.commit()
            #average_height = db.session.query(func.avg(Data.height_)).scalar()
            #average_height = round(average_height, 1)
            #count = db.session.query(Data.height_).count()
            #send_email(email, height, average_height, count)
            #return render_template("success.html")

            print(email, age, gender, music_genre, festival_number, festival_age, festival_name, festival_music_genre,
                   yesno_2021, festival_name_2021)
            return render_template("en-success.html")
        elif age < festival_age:
            return render_template("en-home.html", text = message_age_en)
        else:
            return render_template("en-home.html", text = message_email_en)

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
        yesno_2021 = request.form["form_yesno_2021"]
        festival_name_2021 = request.form["form_festival_name_2021"]

        print(email, age, gender, music_genre, festivals_number, festivals_age, festival_name, festival_music_genre,
              yesno_2021, festival_name_2021)
    return render_template("es-success.html")

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5003) # port = 5000, by default