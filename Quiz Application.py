import tkinter
from tkinter import Tk, Frame, Label, Button



class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!",fg="red")
            right += 1
        else:
            label = Label(view, text="Wrong!",fg="red")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question,fg="red",bg="cyan",font="Times 16 bold").pack()
        Button(view, text=self.answers[0], command=lambda *args:        self.check("A", view),fg="white",bg="green",font="Times 12 bold").pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view),fg="white",bg="green",font="Times 12 bold").pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view),fg="white",bg="green",font="Times 12 bold").pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view),fg="white",bg="green",font="Times 12 bold").pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + "\n questions answered right",bg="blue",fg="white",font="Times 18 bold").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
button = Button(window, text="Start", command=askQuestion,fg="white",bg="green",font="Times 20 bold")
button.pack()
window.title("Quiz Application")
window.configure(background="cyan")
window.mainloop()