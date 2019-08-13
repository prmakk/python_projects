import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import time
import datetime

def say(words):
	engine = pyttsx3.init()
	engine.say("приветствую, повелитель! жду ваших приказов.")
	engine.runAndWait()

say("Привет,спроси что то")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	
	try:
		zadanie = r.recognize_google(audio).lower()
		print("Вы сказали: " + zadanie)
	except sr.UnknownValueError:
		say("Я Вас не поняла")
		zadanie =  command()

	return zadanie

def makeSomething(zadanie):
	if 'open youtube' in zadanie:
		engine = pyttsx3.init()
		engine.say("открываю ютуб")
		engine.runAndWait()
		url = 'https://youtube.com'
		webbrowser.open(url)
	elif 'open vk' in zadanie:
		engine = pyttsx3.init()
		engine.say("открываю вэка")
		engine.runAndWait()
		url = 'https://vk.com'
		webbrowser.open(url)
	elif 'open w' in zadanie:
		engine = pyttsx3.init()
		engine.say("открываю погоду")
		engine.runAndWait()
		url = 'https://www.gismeteo.ua/weather-kryvyi-rih-4978/'
		webbrowser.open(url)
	elif 'open music' in zadanie:
		engine = pyttsx3.init()
		engine.say("открываю музыку")
		engine.runAndWait()
		url = 'https://www.youtube.com/watch?v=yJg-Y5byMMw'
		webbrowser.open(url)
	elif 'bye' in zadanie:
		engine = pyttsx3.init()
		engine.say("зовите ещё")
		engine.runAndWait()
		sys.exit()
	elif 'time' in zadanie:
		now = datetime.datetime.now()
		engine = pyttsx3.init()
		engine.say("сейчас " + str(now.hour) + ":" + str(now.minute))
		engine.runAndWait()
	elif 'how are you' in zadanie:
		now = datetime.datetime.now()
		engine = pyttsx3.init()
		engine.say('У Катрин всё хорошо, жду следующую команду')
		engine.runAndWait()

while True:
	makeSomething(command())