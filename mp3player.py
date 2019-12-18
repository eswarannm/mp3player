from Tkinter import *
import Tkinter as tk
from pygame import mixer
from PIL import Image
from PIL import ImageTk
import tkFont


root = tk.Tk()
mixer.init()
root.title("Music Player")
root.geometry("500x1000")


helv40 = tkFont.Font(family='Helvetica', size=40, weight='bold')
helv28 = tkFont.Font(family='Helvetica', size=20, weight='bold')
helv15 = tkFont.Font(family='Helvetica', size=15, weight='bold')

t = Label(root, text="FINE LINE", font=helv40, fg ="#85C1E9")
t.pack()


image = Image.open("image.png")
image = image.resize((170, 170))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.img = photo 
label.pack()


player = Label(root, text="Click the dropdown menu to choose a song!", font=helv28, fg ="#D853A1")
player.pack()

variable = StringVar(root)

song = OptionMenu(root, variable, "Golden.wav", "Watermelon Sugar.wav", "Adore You.wav", "Lights Up.wav","Cherry.wav", "Falling.wav", "To Be So Lonely.wav", "She.wav", "Sunflower, Vol. 6.wav", "Canyon Moon.wav", "Treat People With Kindness.wav", "Fine Line.wav")
song.configure(width=30)
song.pack()


def play_music():
	mixer.music.load(variable.get())
	mixer.music.play()

def stop_music():
	mixer.music.stop()


pause=False

def pausesong():
    global pause
    if pause == False:
        mixer.music.pause()
        pause = True
    else:
        mixer.music.unpause()
        pause = False


playbtn = Button(root, text="PLAY",  command=play_music, font=helv15)
stopbtn = Button(root, text="STOP", command=stop_music, font=helv15)
pausebtn = Button(root, text="PAUSE/UNPAUSE", command = pausesong, font=helv15)
playbtn.pack()
pausebtn.pack()
stopbtn.pack()

global lyrics 
lyrics = ['know that youre trying to be friends', 'maybe we can find a place to feel good']
global answers
answers = ['know you mean it', 'and we can treat people with kindness']
global counter
counter = 0
def add_counter():
	global counter
	counter += 1
	return counter

def start(first_half, real_answer):
	def submit():
		answer = ans.get()
		new_answer = answer.lower()
		if new_answer == real_answer:
			m = Label(root, text = "You got it! Good job! :)")
			m.pack()
		else:
			n = Label(root, text = "The lyric was: " + real_answer)
			n.pack()

	q = tk.Label(root, text= first_half)
	q.pack()
    
	ans = tk.Entry(root, width=40)
	ans.pack()
	sub = Button(root, text="SUBMIT", command=lambda:submit(), font=helv15)
	sub.pack()
	answer1, answer2 = text_display(counter)
	startButton = Button(root, command=lambda:start(answer1, answer2), text="NEXT", font=helv15)
	startButton.pack()
	if (counter < len(lyrics)):
		add_counter();

    
def text_display(counter):
	return lyrics[counter], answers[counter] 

greet = Label(root, text="Finish the lyric!", font=helv28 , fg ="#85C1E9")
greet.pack()
startButton = Button(root, command=lambda:start('I know that youre scared','because hearts get broken'), text="START", font=helv15)
startButton.pack()




root.mainloop()
