from flask import Flask, render_template, request
from serv import send_parameters, show_last_tasks
from send_mail import send_email
from config import MAIL, PASS, mail_to, subject


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/response", methods=['POST'])
def parameters():
    if request.method == 'POST':
        text = request.form.get('text')
        send_email(mail_to=mail_to, subject=subject, text=text)
    response = send_parameters()
    return response


@app.route("/last_tasks", methods=['GET'])
def last_tasks():
    emails = show_last_tasks()
    return render_template("last_emails_list.html", emails=emails)


if __name__ == '__main__':
    app.run(debug=True)
