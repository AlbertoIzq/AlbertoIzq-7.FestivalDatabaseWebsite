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
    message_list = []

    message_list.append("Hey there!")
    message_list.append("")
    message_list.append("Thanks for your submission. You entered the following data:")
    message_list.append("- Email address: <strong>{}</strong>".format(email))
    message_list.append("- Age: <strong>{}</strong> years".format(str(age)))
    message_list.append("- Gender: <strong>{}</strong>".format(gender))
    message_list.append("- Favourite music genre: <strong>{}</strong>".format(music_genre))
    message_list.append("- Festivals you have been to: <strong>{}</strong>".format(str(festival_number)))
    if festival_age == None:
        message_list.append("- Age at your first festival: <strong>-</strong> years")
    else:
       message_list.append("- Age at your first festival: <strong>{}</strong> years".format(str(festival_age)))
    message_list.append("- Favourite festival: <strong>{}</strong>".format(festival_name))
    message_list.append("- Favourite music genre for festivals: <strong>{}</strong>".format(festival_music_genre))
    if yesno_2021 == "yes":
        message_list.append("- You want to go to \"<strong>{}</strong>\" festival in <strong>2021</strong>".format(festival_name_2021))
    else:
        message_list.append("- You <strong>don't want</strong> to go to any festival in <strong>2021</strong>. You're boring! haha")
    message_list.append("")

    message_list.append("Survey results are the following:")
    message_list.append("- Number of entries: {}".format(str(c_number_entries)))
    message_list.append("- Age:")
    message_list.append("&emsp;&emsp;· Minimum: {} years".format(str(c_min_age)))
    message_list.append("&emsp;&emsp;· Maximum: {} years".format(str(c_max_age)))
    message_list.append("&emsp;&emsp;· Average: {} years".format(str(c_avg_age)))
    message_list.append("- Gender:")
    message_list.append("&emsp;&emsp;· % males: {}%".format(str(c_males)))
    message_list.append("&emsp;&emsp;· % females: {}%".format(str(c_females)))
    message_list.append("&emsp;&emsp;· % other: {}%".format(str(c_other)))
    message_list.append("- Number of festivals:")
    message_list.append("&emsp;&emsp;· Minimum: {}".format(str(c_min_num_fest)))
    message_list.append("&emsp;&emsp;· Maximum: {}".format(str(c_max_num_fest)))
    message_list.append("&emsp;&emsp;· Average: {}".format(str(c_avg_num_fest)))
    message_list.append("- Age first festival:")
    if c_min_age_first == None:
        message_list.append("&emsp;&emsp;· Minimum: - años")
    else:
        message_list.append("&emsp;&emsp;· Minimum: {} años".format(str(c_min_age_first)))
    if c_max_age_first == None:
        message_list.append("&emsp;&emsp;· Maximum: - años")
    else:
        message_list.append("&emsp;&emsp;· Maximum: {} años".format(str(c_max_age_first)))
    if c_avg_age_first == None:
        message_list.append("&emsp;&emsp;· Average: - años")
    else:
        message_list.append("&emsp;&emsp;· Average: {} años".format(str(c_avg_age_first)))
    message_list.append("- Wanna go to a festival in 2021:")
    message_list.append("&emsp;&emsp;· % yes: {}%".format(str(c_yes)))
    message_list.append("&emsp;&emsp;· % no: {}%".format(str(c_no)))
    message_list.append("")

    message_list.append("Regards,")
    message_list.append("")

    message_list.append("Alberto")

    message = ""
    for msg in message_list:
        message = message + msg + "<br />"   

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
    - Edad: <strong>{}</strong> años<br />".format(str(age))

    if gender == "male":
        message = message + "- Género: <strong>hombre</strong><br />"
    elif gender == "female":
        message = message + "- Género: <strong>mujer</strong><br />"
    else:
        message = message + "- Género: <strong>otro</strong><br />"

    message = message + "- Género músical favorito: <strong>{}</strong><br />".format(music_genre) + "\
    - Festivales en los que has estado: <strong>{}</strong><br />".format(str(festival_number))

    if festival_age == None:
        message = message + "- Edad en tu primer festival: <strong>-</strong> años<br />"
    else:
        message = message + "- Edad en tu primer festival: <strong>{}</strong> años<br />".format(str(festival_age))

    message = message + "- Festival favorito: <strong>{}</strong><br />".format(festival_name) +  "\
    - Género musical favorito para festivales: <strong>{}</strong><br />".format(festival_music_genre)

    if yesno_2021 == "yes":
        message = message + "- Quieres ir al festival \"<strong>{}</strong>\" en <strong>2021</strong><br />".format(festival_name_2021)
    else:
        if gender == "female":
            message = message + "- <strong>No quieres ir</strong> a ningún festival en <strong>2021</strong>. Eres una aburrida! jaja<br />"
        else:
            message = message + "- <strong>No quieres ir</strong> a ningún festival en <strong>2021</strong>. Eres un aburrido! jaja<br />"

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
    - Edad en el primer festival:<br />"

    if c_min_age_first == None:
        message = message + "&emsp;&emsp;· Mínima: - años<br />"
    else:
        message = message + "&emsp;&emsp;· Mínima: {} años<br />".format(str(c_min_age_first))

    if c_max_age_first == None:
        message = message + "&emsp;&emsp;· Máxima: - años<br />"
    else:
        message = message + "&emsp;&emsp;· Máxima: {} años<br />".format(str(c_max_age_first))

    if c_avg_age_first == None:
        message = message + "&emsp;&emsp;· Media: - años<br />"
    else:
        message = message + "&emsp;&emsp;· Media: {} años<br />".format(str(c_avg_age_first))

    message = message + "- Quieren ir a un festival en 2021:<br /> \
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