from email.mime.text import MIMEText
import smtplib

def send_email_en(email, age, gender, music_genre, festival_number, festival_age,
                  festival_name, festival_music_genre, yesno_2021, festival_name_2021,
                  c_number_entries, c_min_age, c_max_age, c_avg_age, c_males, c_females,
                  c_other, c_min_num_fest, c_max_num_fest, c_avg_num_fest, c_min_age_first,
                  c_max_age_first, c_avg_age_first, c_yes, c_no):
    from_email = "test.alberto.py@gmail.com"
    from_password = "Python69+"
    to_email = email

    subject = "Music festivals survey - Results"
    message = "Hey there!<br /><br /> \
    Thanks for your submission. You introduced the following data:<br /> \
    - Email address: <strong>{}</strong><br />".format(email) + "\
    - Age: <strong>{}</strong> years<br />".format(str(age)) + "\
    - Gender: <strong>{}</strong><br />".format(gender) + "\
    - Favourite music genre: <strong>{}</strong><br />".format(music_genre) + "\
    - Festivals you have been to: <strong>{}</strong><br />".format(str(festival_number)) + "\
    - Age of your first festival: <strong>{}</strong> years<br />".format(str(festival_age)) +  "\
    - Favourite festival: <strong>{}</strong><br />".format(festival_name) +  "\
    - Favourite music genre for festivals: <strong>{}</strong><br />".format(festival_music_genre)

    if yesno_2021 == "yes":
        message = message + "- You want to go to \"<strong>{}</strong>\" festival in <strong>2021</strong><br />".format(festival_name_2021)
    else:
        message = message + "- You <strong>don't want</strong> to go to any festival in <strong>2021</strong>. You're boring! haha<br />"

    message = message + "<br />Survey results are the following:<br /> \
    - Number of entries: {}<br />".format(str(c_number_entries)) + "\
    - Age:<br /> \
    &emsp;&emsp;· Minimum: {} years<br />".format(str(c_min_age)) + "\
    &emsp;&emsp;· Maximum: {} years<br />".format(str(c_max_age)) + "\
    &emsp;&emsp;· Average: {} years<br />".format(str(c_avg_age)) + "\
    - Gender:<br /> \
    &emsp;&emsp;· % males: {}%<br />".format(str(c_males)) + "\
    &emsp;&emsp;· % females: {}%<br />".format(str(c_females)) + "\
    &emsp;&emsp;· % other: {}%<br />".format(str(c_other)) + "\
    - Number of festivals:<br /> \
    &emsp;&emsp;· Minimum: {}<br />".format(str(c_min_num_fest)) + "\
    &emsp;&emsp;· Maximum: {}<br />".format(str(c_max_num_fest)) + "\
    &emsp;&emsp;· Average: {}<br />".format(str(c_avg_num_fest)) + "\
    - Age first festival:<br /> \
    &emsp;&emsp;· Minimum: {} years<br />".format(str(c_min_age_first)) + "\
    &emsp;&emsp;· Maximum: {} years<br />".format(str(c_max_age_first)) + "\
    &emsp;&emsp;· Average: {} years<br />".format(str(c_avg_age_first)) + "\
    - Wanna go to a festival in 2021:<br /> \
    &emsp;&emsp;· % yes: {}%<br />".format(str(c_yes)) + "\
    &emsp;&emsp;· % no: {}%<br />".format(str(c_no)) + "\
    <br />Regards,<br /> Alberto"

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

def send_email_es(email, age, gender, music_genre, festival_number, festival_age,
                  festival_name, festival_music_genre, yesno_2021, festival_name_2021,
                  c_number_entries, c_min_age, c_max_age, c_avg_age, c_males, c_females,
                  c_other, c_min_num_fest, c_max_num_fest, c_avg_num_fest, c_min_age_first,
                  c_max_age_first, c_avg_age_first, c_yes, c_no):
    from_email = "test.alberto.py@gmail.com"
    from_password = "Python69+"
    to_email = email

    subject = "Encuesta sobre festivales de música - Resultados"
    message = "Buenas!<br /><br /> \
    Gracias por participar en la encuesta. Los datos que has introducido son los siguientes:<br /> \
    - Correo electrónico: <strong>{}</strong><br />".format(email) + "\
    - Edad: <strong>{}</strong> años<br />".format(str(age)) + "\
    - Género: <strong>{}</strong><br />".format(gender) + "\
    - Género músical favorito: <strong>{}</strong><br />".format(music_genre) + "\
    - Festivales en los que has estado: <strong>{}</strong><br />".format(str(festival_number)) + "\
    - Edad en tu primer festival: <strong>{}</strong> años<br />".format(str(festival_age)) +  "\
    - Festival favorito: <strong>{}</strong><br />".format(festival_name) +  "\
    - Género musical favorito para festivales: <strong>{}</strong><br />".format(festival_music_genre)

    if yesno_2021 == "yes":
        message = message + "- Quieres ir al festival \"<strong>{}</strong>\" en <strong>2021</strong><br />".format(festival_name_2021)
    else:
        message = message + "- <strong>No quieres ir</strong> a ningún festival en <strong>2021</strong>. Eres aburrid@! jaja<br />"

    message = message + "<br />Resultados de la encuesta:<br /> \
    - Personas que han participado: {}<br />".format(str(c_number_entries)) + "\
    - Edad:<br /> \
    &emsp;&emsp;· Mínima: {} años<br />".format(str(c_min_age)) + "\
    &emsp;&emsp;· Máxima: {} años<br />".format(str(c_max_age)) + "\
    &emsp;&emsp;· Media: {} años<br />".format(str(c_avg_age)) + "\
    - Género:<br /> \
    &emsp;&emsp;· % hombres: {}%<br />".format(str(c_males)) + "\
    &emsp;&emsp;· % mujeres: {}%<br />".format(str(c_females)) + "\
    &emsp;&emsp;· % otros: {}%<br />".format(str(c_other)) + "\
    - Número de festivales:<br /> \
    &emsp;&emsp;· Mínimo: {}<br />".format(str(c_min_num_fest)) + "\
    &emsp;&emsp;· Máximo: {}<br />".format(str(c_max_num_fest)) + "\
    &emsp;&emsp;· Media: {}<br />".format(str(c_avg_num_fest)) + "\
    - Edad en elprimer festival:<br /> \
    &emsp;&emsp;· Mínima: {} años<br />".format(str(c_min_age_first)) + "\
    &emsp;&emsp;· Máxima: {} años<br />".format(str(c_max_age_first)) + "\
    &emsp;&emsp;· Media: {} años<br />".format(str(c_avg_age_first)) + "\
    - Quieren ir a un festival en 2021:<br /> \
    &emsp;&emsp;· % sí: {}%<br />".format(str(c_yes)) + "\
    &emsp;&emsp;· % no: {}%<br />".format(str(c_no)) + "\
    <br />Saludos,<br /> Alberto"

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)