BACKGROUND_COLOR = "#B1DDC6"
import tkinter as tk
import pandas as pd
import random

root = tk.Tk()
df = pd.read_csv("data/french_words.csv")
# df_learn = pd.read_csv("Need_To,Learn.csv")
df_dict =df.to_dict(orient="records")
globe_word = random.choice(df_dict)

def next():
    global globe_word, timer
    root.after_cancel(timer)
    globe_word = random.choice(df_dict)
    canva.itemconfig(bg_image, image=card_front)
    canva.itemconfig(title, fill="black", text="French")
    canva.itemconfig(words, fill="black", text=globe_word["French"])

    timer = root.after(3000, change_to_bgfront)



def change_to_bgfront():
    canva.itemconfig(bg_image, image=card_back)
    canva.itemconfig(title, fill="black", text="English")
    canva.itemconfig(words, fill="Black" ,text=globe_word["English"])

def user_know():
    # data = {
    #     "French": globe_word['French'],
    #     "English": globe_word['English']
    # }
    known_data = pd.DataFrame([globe_word])
    print(known_data)
    # known_data.to_csv("Know_Word.csv", mode="a", index=True)
    df_dict.remove(globe_word)
    next()






















card_back = tk.PhotoImage(file="images/card_back.png")
card_front= tk.PhotoImage(file="images/card_front.png")
correct = tk.PhotoImage(file="images/right.png")
wrong = tk.PhotoImage(file="images/wrong.png")


root.title("Flashcard")
root.config(padx=50, pady=60, bg=BACKGROUND_COLOR)




canva = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_image = canva.create_image(400,526/2, image=card_front)


title = canva.create_text(400, 150, text="French", font=("Arial",40,"italic"))
words = canva.create_text(400, 263, text=f"{globe_word['French']}", font=("Arial",60,"bold"))
canva.grid(column=0,row=0, columnspan=2)

timer = root.after(3000,change_to_bgfront)
correct_button = tk.Button(image=correct, highlightthickness=0, bg=BACKGROUND_COLOR, command=user_know)
correct_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next)
wrong_button.grid(column=0, row=1)







root.mainloop()