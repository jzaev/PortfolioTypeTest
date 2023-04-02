import tkinter as tk
import time
import random


class TypingTestApp:
    SAMPLE_TEST_LIST = [
        "All's well that ends well.",
        "Actions speak louder than words.",
        "Don't count your chickens before they're hatched.",
        "Early to bed and early to rise, makes a man healthy, wealthy, and wise.",
        "Every cloud has a silver lining.",
        "Haste makes waste.",
        "If at first you don't succeed, try, try again.",
        "Laughter is the best medicine.",
        "Practice makes perfect.",
        "When in Rome, do as the Romans do.",
    ]

    # Constants
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    ENTRY_WIDTH = 60
    TIMER_UPDATE_MS = 1000

    def __init__(self, master, text_list=SAMPLE_TEST_LIST):
        self.master = master
        self.master.title("Typing Speed Test")

        self.sample_texts = text_list

        self.start_time = None
        self.words_typed = 0

        self.setup_widgets()

    def setup_widgets(self):
        self.master.minsize(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.master.maxsize(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)

        self.instruction_label = tk.Label(self.master, text="Type the text below:")
        self.instruction_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.sample_text_label = tk.Label(self.master, text=self.get_random_sample_text(), wraplength=300)
        self.sample_text_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.typing_area = tk.Entry(self.master, width=self.ENTRY_WIDTH)
        self.typing_area.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_typing)
        self.start_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.stop_button = tk.Button(self.master, text="Stop", command=self.finish_typing)
        self.stop_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=4, column=0, padx=10, pady=10, sticky="w", columnspan=2)

        self.timer_label = tk.Label(self.master, text="00:00")
        self.timer_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

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
        self.update_timer()

    def enter_pressed(self, event):
        typed_text = self.typing_area.get().strip()
        typed_words = typed_text.split()
        sample_words = self.sample_text_label.cget("text").split()

        correct_words = 0
        for t, s in zip(typed_words, sample_words):
            if t == s:
                correct_words += 1
            else:
                break

        if correct_words == len(sample_words):
            self.words_typed += len(typed_words)
            time_taken = time.time() - self.start_time
            words_per_minute = (self.words_typed / time_taken) * 60
            self.result_label.config(text=f"Your typing speed is: {words_per_minute:.2f} words per minute.")
            self.sample_text_label.config(text=self.get_random_sample_text())
            self.typing_area.delete(0, tk.END)
        else:
            self.result_label.config(text="Wrong word! Try again.")

    def finish_typing(self):
        self.master.after_cancel(self.update_timer_id)
        self.typing_area.unbind("<Return>")

    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        self.update_timer_id = self.master.after(self.TIMER_UPDATE_MS, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
