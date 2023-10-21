from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
from email.message import EmailMessage
app = Flask(__name__)

@app.route('/')
def index():
    start_date = datetime(2022,6,2) # start date of working as a Full time employee
    current_date = datetime.now() #current date of working 
    difference  = current_date - start_date
    difference_in_years = (difference.days + difference.seconds/86400)/365.2425
    total_exp=round(difference_in_years,1)

    return render_template('index.html',total_exp=total_exp,age=20,occupation='Student')

@app.route("/sendemail/", methods=['POST'])
def sendmail():
    if request.method=='POST':
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        your_name="Varigonda Sai Nirmal Vignu"
        your_email="nirmalvignu@gmail.com"
        your_password="tysr rbjm iryf rmra"

        # Logging in to our email account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)

        # Sender's and Receiver's email address
        sender_email = "nirmalvignu@gmail.com"
        receiver_email = "varigondanirmal1@gmail.com"

        msg = EmailMessage()
        msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
        msg['Subject'] = 'New Response on Personal Website'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
        except:
            pass
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)