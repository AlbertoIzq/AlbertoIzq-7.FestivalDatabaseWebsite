from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email_en
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/festival_survey'
db = SQLAlchemy(app)

message_email_en = "Seems like I've got something from that email address already"
message_email_es = "Parece que alguien ya ha introducido datos con ese correo electrónico"

message_first_en = "If you enter your age when going to your first festival then number of festivals cannot be 0, can it?"
message_first_es = "Si has introducido la edad con la que fuiste a tu primer festival entonces el número de festivales no puede ser 0, ¿no?"

message_first2_en = "If you have been in any festival then you have to enter your age at the first one, don't you?"
message_first2_es = "Si has ido a algún festival 0 entonces tienes que introducir la edad en el primero, ¿no?"

message_age_en = "Your age cannot be less than when you first went to a festival, can it?"
message_age_es = "Tu edad no puede ser menor que la que tenías cuando fuiste por primera vez a un festival, ¿no?"

message_yes2021_en = "If you say you wanna go to a festival in 2021, then please enter its name"
message_yes2021_es = "Si dices que quieres ir a un festival en 2021, entonces introduce el nombre por favor"

message_no2021_en = "If you say you don't wanna go to a festival in 2021, then why do you enter a name?"
message_no2021_es = "Si dices que no quieres ir a un festival en 2021, entonces ¿porqué introduces cómo se llama?"

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
        if request.form["form_festival_age"] == "":
            festival_age = None
        else:
            festival_age = request.form["form_festival_age"]
        festival_name = request.form["form_festival_name"]
        festival_music_genre = request.form["form_festival_music_genre"]
        yesno_2021 = request.form["form_yesno_2021"]
        if request.form["form_festival_name_2021"] == "":
            festival_name_2021 = None
        else:
            festival_name_2021 = request.form["form_festival_name_2021"]

        # Handling missentered data before saving it into database
        if int(festival_number) == 0 and festival_age is not None:
            return render_template("en-home.html", text = message_first_en)
        if int(festival_number) != 0 and festival_age is None:
            return render_template("en-home.html", text = message_first2_en)
        if festival_age is not None and int(festival_age) > int(age):
            return render_template("en-home.html", text = message_age_en)
        if yesno_2021 == "yes" and festival_name_2021 is None:
            return render_template("en-home.html", text = message_yes2021_en)
        if yesno_2021 == "no" and festival_name_2021 is not None:
            return render_template("en-home.html", text = message_no2021_en)
        # Save data into database if there's no entry with the same email address
        if db.session.query(Data).filter(Data.email==email).count() == 0: # count() counts how many values satisfy this condition
            data = Data(email, age, gender, music_genre, festival_number, festival_age,
                        festival_name, festival_music_genre, yesno_2021, festival_name_2021)
            db.session.add(data) # You add the variable created before for the database to recognize the values
            db.session.commit()

            c_number_entries = db.session.query(Data.email).count()
            c_min_age = db.session.query(func.min(Data.age)).scalar()
            c_max_age = db.session.query(func.max(Data.age)).scalar()
            c_avg_age = db.session.query(func.avg(Data.age)).scalar()
            c_avg_age = round(c_avg_age, 1)
            c_males = db.session.query(Data).filter(Data.gender=="male").count()
            c_males = str(round(float(100 * c_males / c_number_entries), 2))
            c_females = db.session.query(Data).filter(Data.gender=="female").count()
            c_females = str(round(float(100 * c_females / c_number_entries), 2))
            c_other = db.session.query(Data).filter(Data.gender=="other").count()
            c_other = str(round(float(100 * c_other / c_number_entries), 2))
            c_min_num_fest = db.session.query(func.min(Data.festival_number)).scalar()
            c_max_num_fest = db.session.query(func.max(Data.festival_number)).scalar()
            c_avg_num_fest = db.session.query(func.avg(Data.festival_number)).scalar()
            c_avg_num_fest = round(c_avg_num_fest, 1)
            if db.session.query(func.min(Data.festival_age)).scalar() is not None:
                c_min_age_first = db.session.query(func.min(Data.festival_age)).scalar()
            else:
                c_min_age_first = None
            if db.session.query(func.max(Data.festival_age)).scalar() is not None:
                c_max_age_first = db.session.query(func.max(Data.festival_age)).scalar()
            else:
                c_max_age_first = None
            if db.session.query(func.avg(Data.festival_age)).scalar() is not None:
                c_avg_age_first = db.session.query(func.avg(Data.festival_age)).scalar()
                c_avg_age_first = round(c_avg_age_first, 1)
            else:
                c_avg_age_first = None
            c_yes = db.session.query(Data).filter(Data.yesno_2021=="yes").count()
            c_yes = str(round(float(100 * c_yes / c_number_entries), 2))
            c_no = db.session.query(Data).filter(Data.yesno_2021=="no").count()
            c_no = str(round(float(100 * c_no / c_number_entries), 2))

            send_email_en(email, age, gender, music_genre, festival_number, festival_age,
                          festival_name, festival_music_genre, yesno_2021, festival_name_2021,
                          c_number_entries, c_min_age, c_max_age, c_avg_age, c_males, c_females,
                          c_other, c_min_num_fest, c_max_num_fest, c_avg_num_fest, c_min_age_first,
                          c_max_age_first, c_avg_age_first, c_yes, c_no)

            print(email, age, gender, music_genre, festival_number, festival_age, festival_name, festival_music_genre,
                   yesno_2021, festival_name_2021)
            return render_template("en-success.html")
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