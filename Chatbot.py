from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp# to get sound from the bot
'''
engine= pp.init('dummy')

voices=engine.getProperty('voices')#list
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()
'''
bot= ChatBot("Bot")
bot.storage.drop()# to remove previously stored data
 
conversation=['hello',
              'hi there !',
              'what is your name ?',
              'My name is bot, I am created by Sujit',
              'how are you ?',
              'I am doing great these days',
              'thank you',
              'in which city you live ?',
              'i live in Delhi',
              'in which language you talk?',
              'I mostly talk in English',
              'goodbye',
              'See you later',
              'age',
              'I am 18 years old!',
              'whats on the menu',
              'We sell chocolate chip cookies for $2!',
              'when are you guys open',
              'We are open 7am-4pm Monday-Friday!']


trainer=ListTrainer(bot)
trainer.train(conversation)

def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END, "you: " + query)
    msgs.insert(END, "bot: " + str(answer_from_bot))
    #speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

main=Tk()

main.geometry("500x700")
main.title("My Chat Bot")
main.config(bg="light green")
main.iconbitmap(r'Calculator1.ico')
img=PhotoImage(file="Chat.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

# creating text field
textF=Entry(main, font=("Verdena", 20))
textF.pack(fill=X, pady=10)
# creating button
btn=Button(main, text="Ask From Bot", font=("Verdena", 20),bg="light yellow",fg='green',command= ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()
main.bind('<Return>',enter_function)



main.mainloop()


