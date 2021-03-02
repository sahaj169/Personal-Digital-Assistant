import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import calendar
import random
import warnings
import pyautogui
import psutil 
import pyjokes 
from emailAndpassword import email
from emailAndpassword import password

warnings.filterwarnings('ignore')


name={
	'mike':'sahajghatiya531.sg@gmail.com',
	'monty':'sg5429@srmist.edu.in'
}


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wakeWord(text):
 	WAKE_WORDS= ['hey assistant','okay assistant','so assistant']
 	text = text.lower()
 	for phrase in WAKE_WORDS:
 		if phrase in text:
 			return True
# if the wake word isnt found in the text loop and so it returns false
 	return False

def getDate():
	now = datetime.datetime.now()
	my_date = datetime.datetime.today()
	date = str(my_date).split(" ")
	today_date = date[0]
	return f"{today_date}"

def getPerson(text):
	wordList = text.split()
	for i in range(0,len(wordList)):
		if i+3<=(len(wordList) - 1 ) and wordList[i].lower() == 'who' and wordList[i+1].lower == 'is':
			return wordList[i+2] + " "+ wordList[i+3]
	
def greeting(text):
	Greeting_inputs =['hi','hey','hola','greetings','wassup','hello'] 


	Greeting_Responses = ['howdy','whats good','hello','hey there']

	for word in text.split():
		if word.lower() in Greeting_inputs:
			return random.choice(Greeting_Responses) +' . '

		return ' '

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<=18:
		speak("Good Afternoon!")
	elif hour >= 18 and hour<24:
		speak("Good Evening!")
	else:
		speak("Good night sir")
	speak("I am your AI Assistance . Please tell me how may i help you")
	
def takeCommand():
# it takes microphone input from the user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source,duration=1)
		audio = r.listen(source)
		query = ''
		try:
			print("Recognizing...")
			query = r.recognize_google(audio,language ='en-in')
			print(f"User said: {query}\n")
		except sr.UnknownValueError:
			print("Google speech recognition could not understand the audio, unknown error")
			# speak("use terminal to enter your query")
			# query = str(input("Enter your Query: "))
		# except sr.RequestError as e:
		# 	print('Request results from Google Speech Recognition service error'+ e)
		# 	speak("use terminal to enter your query")
		# 	query = str(input("Enter your Query: "))
		return query

def sendEmail(to,content):
	# init gmail smtp
	server = smtplib.SMTP('smtp.gmail.com', 587)
	# identify to server
	server.ehlo()
	#encrypt session
	server.starttls()
	#login
	server.login(email,password)
	#send message
	server.sendmail(email,to,content)
	#close connection
	server.close()
c=0
def screenshot():
	global c
	c += 1
	img = pyautogui.screenshot()
	img.save(f"screenshot\\ss{c}.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())

r = 0
def respond_to_query(query):
	if(wakeWord(query) == True):
		wishMe()

	if 'wikipedia' in query:
		speak('Searching Wikipedia..')
		query = query.replace("wikipedia", "")
		if query:
			results = wikipedia.summary(query,sentences =2)
			speak("According to wikipedia")
			print(results)
			speak(results)
		else:
			speak("You Did not specified What Do you want to search on wikipedia ")

	elif 'open youtube' in query:
		
		webbrowser.get('chrome').open_new_tab("youtube.com")

	elif 'open google' in query:
		webbrowser.get('chrome').open_new_tab("google.com")

	elif 'open facebook' in query:
		webbrowser.get('chrome').open_new_tab("facebook.com")

	elif 'open linkedin' in query:
		webbrowser.get('chrome').open_new_tab("linkedin.com")

	elif 'open hackerrank' in query:
		webbrowser.get('chrome').open_new_tab("https://www.hackerrank.com/dashboard")

	elif 'open whatsapp' in query:
		webbrowser.get('chrome').open_new_tab("https://web.whatsapp.com/")

	elif 'open netflix' in query:
		webbrowser.get('chrome').open_new_tab("https://www.netflix.com/browse")

	elif 'play songs' in query:
		songs_dir = 'F:\\music'
		songs = os.listdir(songs_dir)
		print(songs)
		os.startfile(os.path.join(songs_dir,songs[0]))

	elif 'the time' in query:
		strtime = datetime.datetime.now().strftime("%H:%M:%S")
		speak(f'The time is {strtime}')
	elif 'date' in query:
		Tdate = getDate()
		speak(Tdate)
	elif 'open sublime' in query:
		codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
		os.startfile(codePath)

	elif 'remember that' in query:
		global r
		r+=1
		speak("What should I remember?")
		data = takeCommand()
		speak("you said me to remember that"+data)
		remember = open('memory.txt', 'a+')
		remember.write(f"{r}) {data} \n ")
		remember.close()

	elif 'open memory' in query:
		remember =open('memory.txt', 'r')
		speak("you said me to remember that" +remember.read())			

	elif 'screenshot' in query:
		screenshot()
		speak("Done!")

	elif 'c p u' in query:
		cpu()
	
	elif 'cpu' in query:
		cpu()

	elif 'joke' in query:
		jokes()


	elif 'entertainment' in query:
		codePath = "E:\\"
		os.startfile(codePath)

	elif 'google search' in query:
		speak("what do you want me to search")
		tosearch = takeCommand()
		webbrowser.get('chrome').open_new_tab('https://www.google.com/search?q=%s'%tosearch)

	elif 'how are you' in query:
		speak("I am great, how can i help you ")

	elif 'coronavirus' in query:
		webbrowser.get('chrome').open_new_tab("https://www.covid19india.org/")

	elif 'search in chrome' in query:
		speak("What should i search ?")
		chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
		search = takeCommand().lower()
		webbrowser.get(chromepath).open_new_tab(search+'.com')

	elif 'logout' in query:
		os.system("shutdown -l")

	elif 'shutdown' in query:
		os.system("shutdown /s /t 1")

	elif 'restart' in query:
		os.system("shutdown /r /t 1")

	elif 'send email' in query:
		try:
			speak("use terminal to enter the details")
			to = str(input("Enter senders email address: "))
			content = str(input("Enter the content you want to send:"))
			sendEmail(to,content)
			speak("Email has been send!")
		except Exception as e:
			print(e)
			speak("Sorry i am not able to send email due to some error")





	elif 'offline' in query:
		quit()

	# elif 'switch off' in query:
	# 	break

if __name__== "__main__":
	
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
	while True:
		query = takeCommand().lower()

	# logic for executing tasks based on query

		if 'keyboard' in query:
			speak("use terminal to enter your query")
			query = str(input("Enter your Query: "))
			respond_to_query(query)
		else:
			respond_to_query(query)
