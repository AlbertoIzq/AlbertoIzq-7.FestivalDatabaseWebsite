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
    message_list = []

    message_list.append("¡Buenas!")
    message_list.append("")
    message_list.append("Gracias por participar en la encuesta. Los datos que has introducido son los siguientes:")
    message_list.append("- Correo electrónico: <strong>{}</strong>".format(email))
    message_list.append("- Edad: <strong>{}</strong> años".format(str(age)))
    if gender == "male":
        message_list.append("- Género: <strong>hombre</strong>")
    elif gender == "female":
        message_list.append("- Género: <strong>mujer</strong>")
    else:
       message_list.append("- Género: <strong>otro</strong>")
    message_list.append("- Género músical favorito: <strong>{}</strong>".format(music_genre))
    message_list.append("- Festivales en los que has estado: <strong>{}</strong>".format(str(festival_number)))
    if festival_age == None:
        message_list.append("- Edad en tu primer festival: <strong>-</strong> años")
    else:
       message_list.append("- Edad en tu primer festival: <strong>{}</strong> años".format(str(festival_age)))
    message_list.append("- Festival favorito: <strong>{}</strong>".format(festival_name))
    message_list.append("- Género musical favorito para festivales: <strong>{}</strong>".format(festival_music_genre))
    if yesno_2021 == "yes":
        message_list.append("- Quieres ir al festival \"<strong>{}</strong>\" en <strong>2021</strong>".format(festival_name_2021))
    else:
         if gender == "female":
            message_list.append("- <strong>No quieres ir</strong> a ningún festival en <strong>2021</strong>. ¡Eres una aburrida! jaja")
         else:
            message_list.append("- <strong>No quieres ir</strong> a ningún festival en <strong>2021</strong>. ¡Eres un aburrido! jaja")
    message_list.append("")

    message_list.append("Resultados de la encuesta:")
    message_list.append("- Personas que han participado: {}".format(str(c_number_entries)))
    message_list.append("- Edad:")
    message_list.append("&emsp;&emsp;· Mínima: {} años".format(str(c_min_age)))
    message_list.append("&emsp;&emsp;· Máxima: {} años".format(str(c_max_age)))
    message_list.append("&emsp;&emsp;· Media: {} años".format(str(c_avg_age)))
    message_list.append("- Género:")
    message_list.append("&emsp;&emsp;· % hombres: {}%".format(str(c_males)))
    message_list.append("&emsp;&emsp;· % mujeres: {}%".format(str(c_females)))
    message_list.append("&emsp;&emsp;· % otros: {}%".format(str(c_other)))
    message_list.append("- Número de festivales:")
    message_list.append("&emsp;&emsp;· Mínimo: {}".format(str(c_min_num_fest)))
    message_list.append("&emsp;&emsp;· Máximo: {}".format(str(c_max_num_fest)))
    message_list.append("&emsp;&emsp;· Media: {}".format(str(c_avg_num_fest)))
    message_list.append("- Edad en el primer festival:")
    if c_min_age_first == None:
        message_list.append("&emsp;&emsp;· Mínima: - años")
    else:
        message_list.append("&emsp;&emsp;· Mínima: {} años".format(str(c_min_age_first)))
    if c_max_age_first == None:
        message_list.append("&emsp;&emsp;· Máxima: - años")
    else:
        message_list.append("&emsp;&emsp;· Máxima: {} años".format(str(c_max_age_first)))
    if c_avg_age_first == None:
        message_list.append("&emsp;&emsp;· Media: - años")
    else:
        message_list.append("&emsp;&emsp;· Media: {} años".format(str(c_avg_age_first)))
    message_list.append("- Quieren ir a un festival en 2021:")
    message_list.append("&emsp;&emsp;· % sí: {}%".format(str(c_yes)))
    message_list.append("&emsp;&emsp;· % no: {}%".format(str(c_no)))
    message_list.append("")

    message_list.append("Saludos,")
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