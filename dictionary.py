from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("400×400")
def dict ():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

Label(root, text="Dicitionary", font=("Helvetica 20 bold"), fg="Green").pack(pady=10)

frame = Frame(root)
Label(frame, text="type word", font= ("Helvetica 15 bold" )).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = frame(root)
Label(frame1, text= "meaning:", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

frame2 = frame(root)
Label(frame2, text="synonyms: ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

frame3 = Frame(root)
Label(frame3, text="antonym: ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()

root.mainloop()