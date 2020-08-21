import threading
import time

from flask import Flask, request, render_template, jsonify
from send_mail import send_email
from config import mail_to, subject

letters = []
number_of_letters = 10


def worker(text):
    send_email(mail_to, subject, text)


def send_parameters():
    text = request.form.get('text')
    timer = int(request.form.get('timer'))
    letters.append({"text": text, "timer": timer})
    t = threading.Timer(timer, worker, args=(text,))
    t.start()
    return jsonify({"text": text, "timer": timer}), 201


def show_last_tasks():
    return letters[-number_of_letters:]


