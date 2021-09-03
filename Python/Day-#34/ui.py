from tkinter import * 
import quiz_brain
THEME_COLOR = "#375362"

TRUE_IMAGE = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#34\images\true.png"
FALSE_IMAGE = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#34\images\false.png"


class QuizTkInterface:
    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        self.answer = ""
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # self.canvas = Canvas()
        self.label = Label(text=f"score: {self.score}", font=("Fira Code", 10, "normal"), bg=THEME_COLOR, fg="white")
        self.label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_next = self.canvas.create_text(150, 125, width=280, text="some question",  font=("Fira Code", 12, "normal"), fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.true_PI = PhotoImage(file=TRUE_IMAGE)
        self.true_button = Button(image=self.true_PI, highlightthickness=0, command=self.true_pressed)
        self.true_button.config(padx=20, pady=20)
        self.true_button.grid(column=1, row=3)
        
        self.false_PI = PhotoImage(file=FALSE_IMAGE)
        self.false_button = Button(image=self.false_PI, highlightthickness=0, command=self.false_pressed)
        self.false_button.config(padx=20, pady=20)
        self.false_button.grid(column=2, row=3)

        self.get_next_quest()
        self.window.mainloop() 

    def get_next_quest(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_next, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question_next, text=q_text)
        else:
            self.canvas.itemconfig(self.question_next, text="You've reached end of the QUIZ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.feed_back(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feed_back(self.quiz.check_answer("False"))

    def feed_back(self, is_right):
        self.canvas.itemconfig(self.question_next, fill="white")
        if is_right == True:
            self.canvas.config(bg="SeaGreen")
            self.quiz.score += 1
        else:
            self.canvas.config(bg="OrangeRed")
    
        self.window.after(1000, self.get_next_quest)

