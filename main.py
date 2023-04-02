import tkinter as tk
import time
import random


class TypingTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.sample_texts = ["All's well that ends well.",
                             "Actions speak louder than words.",
                             "Don't count your chickens before they're hatched.",
                             "Early to bed and early to rise, makes a man healthy, wealthy, and wise.",
                             "Every cloud has a silver lining.",
                             "Haste makes waste.",
                             "If at first you don't succeed, try, try again.",
                             "Laughter is the best medicine.",
                             "Practice makes perfect.",
                             "When in Rome, do as the Romans do."]

        self.start_time = None
        self.words_typed = 0

        self.setup_widgets()

    def setup_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Type the text below:")
        self.instruction_label.pack(pady=10)

        self.sample_text_label = tk.Label(self.master, text=self.get_random_sample_text(), wraplength=300)
        self.sample_text_label.pack()

        self.typing_area = tk.Entry(self.master)
        self.typing_area.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_typing)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def get_random_sample_text(self):
        return random.choice(self.sample_texts)

    def start_typing(self):
        self.sample_text_label.config(text=self.get_random_sample_text())
        self.typing_area.delete(0, tk.END)
        self.typing_area.focus()
        self.start_time = time.time()
        self.words_typed = 0
        self.result_label.config(text="")
        self.typing_area.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        typed_text = self.typing_area.get().strip()
        typed_words = typed_text.split()
        sample_words = self.sample_text_label.cget("text").split()

        correct_words = 0
        for typed_word, sample_word in zip(typed_words, sample_words):
            if typed_word == sample_word:
                correct_words += 1
            else:
                break

        if correct_words == len(sample_words):
            self.finish_typing()
        else:
            self.result_label.config(text="Wrong word! Try again.")

    def finish_typing(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        words_per_minute = (len(self.sample_text_label.cget("text").split()) / time_taken) * 60
        result_text = f"Your typing speed is: {words_per_minute:.2f} words per minute."
        self.result_label.config(text=result_text)
        self.typing_area.unbind("<Return>")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
