from email.mime.text import MIMEText
import smtplib

def send_email_en(email, age, gender, music_genre, festival_number, festival_age,
                  festival_name, festival_music_genre, yesno_2021, festival_name_2021,
                  c_number_entries, c_min_age, c_max_age, c_avg_age, c_males, c_females,
                  c_min_num_fest, c_max_num_fest, c_avg_num_fest, c_min_age_first,
                  c_max_age_first, c_avg_age_first, c_yes, c_no):
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
        message = message + "- You want to go to \"" + festival_name_2021 + "\" festival<br />"
    else:
        message = message + "- You don't want to any festival. You're boring! haha<br />"

    message = message + "<br />Survey results are the following:<br /> \
    - Number of entries: " + str(c_number_entries) + "<br /> \
    - Age:<br /> \
    &emsp;&emsp;· Minimum: " + str(c_min_age) + "<br /> \
    &emsp;&emsp;· Maximum: " + str(c_max_age) + "<br /> \
    &emsp;&emsp;· Average: " + str(c_avg_age) + "<br /> \
    - Gender:<br /> \
    &emsp;&emsp;· % males: " + str(c_males) + " %<br /> \
    &emsp;&emsp;· % females: " + str(c_females) + " %<br /> \
    - Number of festivals:<br /> \
    &emsp;&emsp;· Minimum: " + str(c_min_num_fest) + "<br /> \
    &emsp;&emsp;· Maximum: " + str(c_max_num_fest) + "<br /> \
    &emsp;&emsp;· Average: " + str(c_avg_num_fest) + "<br /> \
    - Age first festival:<br /> \
    &emsp;&emsp;· Minimum: " + str(c_min_age_first) + "<br /> \
    &emsp;&emsp;· Maximum: " + str(c_max_age_first) + "<br /> \
    &emsp;&emsp;· Average: " + str(c_avg_age_first) + "<br /> \
    - Wanna go to a festival in 2021:<br /> \
    &emsp;&emsp;· % yes: " + str(c_yes) + "%<br /> \
    &emsp;&emsp;· % no: " + str(c_no) + "%<br /> \
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