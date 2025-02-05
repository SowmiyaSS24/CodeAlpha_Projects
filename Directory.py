import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = self.choose_word()
        self.guessed_letters = set()
        self.attempts = 6

        self.label_word = tk.Label(root, text=self.display_word(), font=("Arial", 24), bg='#d3d3d3')
      
        self.label_word.pack(pady=20)
        
        self.label_info = tk.Label(root, text=f"Attempts left: {self.attempts}", font=("Arial", 14), fg='blue')
        self.label_info.pack()
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_guess)
        
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess, font=("Arial", 14), bg='lightblue')
        self.guess_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg='green')
        self.result_label.pack()
    
    def choose_word(self):
        words = ["Eat", "galaxy", "matrix", "joyful", "staff","strength","cycle"]
        return random.choice(words)
    
    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    
    def check_guess(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Invalid input. Enter a single letter.", fg='red')
            return
        
        if guess in self.guessed_letters:
            self.result_label.config(text="You already guessed this letter!", fg='orange')
            return
        
        self.guessed_letters.add(guess)
        
        if guess not in self.word:
            self.attempts -= 1
            self.label_info.config(text=f"Attempts left: {self.attempts}")
            
        self.label_word.config(text=self.display_word())
        
        if all(letter in self.guessed_letters for letter in self.word):
            self.result_label.config(text="Congratulations! You guessed the word!", fg='green')
            self.entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)
        elif self.attempts <= 0:
            self.result_label.config(text=f"Game Over! The word was {self.word}", fg='red')
            self.entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
