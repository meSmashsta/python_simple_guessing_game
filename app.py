import tkinter as tk
import ctypes
import json
import random
from player import Player

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs, bg="light sky blue")

    def show(self):
        self.lift()

class Page1(Page):
    animals = ["cat", "tiger", "lion", "capibara", "giraffe", "elephant",
               "meerkat", "puffin", "owl", "donkey", "turkey", "sheep",
               "reindeer", "leopard", "swan", "kangaroo", "rooster", "whale",
               "shark", "moose", "panda", "horse", "dog", "fish", "alligator",
               "fox", "deer", "duck", "snake", "camel", "zebra", "eagle", "wolf",
               "crab", "monkey", "octopus", "hedgehog", "mole", "squirrel", "raccoon"
               , "koala", "goat", "chimpanzee"]

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.animals, "Animals")

class Page2(Page):
    places = ["america", "japan", "china", "philippines", "korea", "paris",
            "los angeles", "europe", "new york", "singapore", "alaska",
            "dubai", "new zealand", "thailand", "myanmar", "brazil", "hong kong"]
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.places, "Places")

class Page3(Page):
    things = ["cabinet", "flower base", "curtain", "shirt", "short", "calendar",
                "rosary", "electric fan", "table", "chair", "glass", "phone", "laptop",
                "soap", "pen", "pencil", "paper", "sandals", "shoes", "umbrella", "key", "mask",
                "shield", "toothbrush", "speaker", "clip", "clock", "door", "window", "hat"]

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.things, "Things")

class Page4(Page):
    words = ["loop", "positive", "negative", "rainbow", "computer",
             "science", "programming", "breakfast", "problem", "belief",
             "culture", "crystal", "cable", "transaction", "condition",
             "bundle", "education", "love", "die", "operation", "negative"
             "mathematics", "player", "condition", "reverse",
             "water", "board", "laptop", "apple", "juice", "television",
             "cloud", "fork", "engineering", "pool", "clove"]
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.words, "Random Words", 50)


class Page5(Page):
    words = ["loop", "positive", "negative", "rainbow", "computer",
             "science", "programming", "breakfast", "problem", "belief",
             "culture", "crystal", "cable", "transaction", "condition",
             "bundle", "education", "love", "die", "operation", "negative"
                                                                "mathematics", "player", "condition", "reverse",
             "water", "board", "laptop", "apple", "juice", "television",
             "cloud", "fork", "engineering", "pool", "clove"]

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.words, "Random Words", 50)


class Page6(Page):
    words = ["loop", "positive", "negative", "rainbow", "computer",
             "science", "programming", "breakfast", "problem", "belief",
             "culture", "crystal", "cable", "transaction", "condition",
             "bundle", "education", "love", "die", "operation", "negative"
                                                                "mathematics", "player", "condition", "reverse",
             "water", "board", "laptop", "apple", "juice", "television",
             "cloud", "fork", "engineering", "pool", "clove"]

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        QuestionForm(self, self.words, "Random Words", 50)

class QuestionForm():
    def __init__(self, page, words, title, score = 25):
        self.page = page
        self.words = words
        self.score = score
        
        label = tk.Label(self.page, text=title, font="Helvetica 18 bold")
        label.place(x=20, y=60, relx=.5, anchor="center")

        lblScore = tk.Label(self.page, text="Score:")
        lblScore.place(x=20, y=20)
                
        lblActualScore = tk.Label(self.page, text=App.player.score)
        lblActualScore.place(x=60, y=20)
        
        def onScoreChange(score):
            lblActualScore['text'] = score
        
        App.player.scoreSubject.subscribe(onScoreChange)

        self.selectedWord = random.choice(self.words)
        self.randomWord = "".join(random.sample(self.selectedWord, len(self.selectedWord)))
        
        lblDisplay = tk.Label(self.page, text=self.randomWord, font="Helvetica 14 bold underline")
        lblDisplay.place(x=20, y=100, relx=.5, anchor="center")
        
        lblAnswer = tk.Label(self.page, text="Answer")
        lblAnswer.place(x=-20, y=140, relx=.5, anchor="center")
        
        entryAnswer = tk.Entry(self.page)
        entryAnswer.place(x=20, y=180, relx=.5, anchor="center")
        def onSubmit():
            if (entryAnswer.get() == self.selectedWord):
                ctypes.windll.user32.MessageBoxW(0, "Congrats on guessing the correct word!", 'Correct answer!')
                entryAnswer.delete(0, 'end')
                App.player.addScore(self.score)
                self.selectedWord = random.choice(self.words)
                self.randomWord = "".join(random.sample(self.selectedWord, len(self.selectedWord)))
                lblDisplay['text'] = self.randomWord
            else:
                ctypes.windll.user32.MessageBoxW(0, "Nice try! Try again!", 'Try Again')
                        
        btnSubmit = tk.Button(self.page, text="Submit", command=onSubmit)
        btnSubmit.place(x=20, y=220, relx=.5, anchor="center")

class App(tk.Frame):
    player = Player()
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Animals", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Places", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Things", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Random  Words", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Tutorial", command=p5.lift)
        b6 = tk.Button(buttonframe, text="About", command=p6.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="right")
        b6.pack(side="right")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()