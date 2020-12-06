from email.mime.text import MIMEText
import smtplib

def send_email_en(email, age, gender, music_genre, festival_number, festival_age,
                        festival_name, festival_music_genre, yesno_2021, festival_name_2021): # count, etc.
    from_email = "test.alberto.py@gmail.com"
    from_password = "Python69+"
    to_email = email

    subject = "Music festivals survey - Results"
    message = "Hey there!<br /><br /> \
    Thanks for your submission. You introduced the following data:<br /> \
    - Email address: " + email + "<br /> \
    - Age: " + str(age) + "<br /> \
    - Gender: " + gender + "<br /> \
    - Favourite music genre: " + music_genre + "<br /> \
    - Festivals you have been to: " + str(festival_number) + "<br /> \
    - Age of your first festival: " + str(festival_age) + "<br /> \
    - Favourite festival: " + festival_name + "<br /> \
    - Favourite music genre for festivals: " + festival_music_genre + "<br />"

    if yesno_2021 == "yes":
        message = message + "- You want to go to \"" + festival_name_2021 + " festival<br />"
    else:
        message = message + "- You don't want to any festival. You're boring! haha<br />"

    message = message + "<br />Survey results are the following:<br /> \
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