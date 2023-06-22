import tkinter as tk
from emoji import emojize

class VirtualKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.text_box = tk.Text(self.text_frame, height=7, width=60)
        self.text_box.pack()

        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.lower_keyboard_buttons()

    def lower_keyboard_buttons(self):
        self.caps_lock = False

        # First Row: 1234567890
        first_row = '1234567890'
        for i, char in enumerate(first_row):
            button = tk.Button(self.keyboard_frame, text=char, width=6,
                               command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=0, column=i)

        # Second Row: qwertyuiop
        second_row = 'qwertyuiop'
        for i, char in enumerate(second_row):
            button = tk.Button(self.keyboard_frame, text=char, width=6,
                               command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=1, column=i)

        # Third Row: asdfghjkl
        third_row = 'qasdfghjkl'
        for i, char in enumerate(third_row):
            if char == 'q':
                button = tk.Button(self.keyboard_frame, text='Tab', width=6,
                                   command=self.insert_tab)
            else:
                button = tk.Button(self.keyboard_frame, text=char, width=6,
                                   command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=2, column=i)

        # Fourth Row: zxcvbnm
        fourth_row = 'eqzxcvbnmw'
        for i, char in enumerate(fourth_row):
            if char == 'q':
                button = tk.Button(self.keyboard_frame, text='Caps', width=6,
                                   command=self.upper_keyboard_buttons)
            elif char == 'w':
                button = tk.Button(self.keyboard_frame, text='Return', width=6,
                                   command=self.insert_newline)
            elif char == 'e':
                button = tk.Button(self.keyboard_frame, text='Delete', width=6,
                                    command=self.delete_value)
            else:
                button = tk.Button(self.keyboard_frame, text=char, width=6,
                                   command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=3, column=i)

        # Fifth Row: Space Bar
        space_button = tk.Button(self.keyboard_frame, text='Space', width=24,
                                 command=lambda: self.text_box.insert(tk.END, ' '))
        space_button.grid(row=4, column=0, columnspan=12)
        
        emoji_button = tk.Button(self.keyboard_frame, text='Emoji', width=6,
                             command=self.emoji_keyboard_buttons)
        emoji_button.grid(row=4, column=0)

    def upper_keyboard_buttons(self):
        self.caps_lock = True

        # First Row: 1234567890
        first_row = '!@#$%^&*()'
        for i, char in enumerate(first_row):
            button = tk.Button(self.keyboard_frame, text=char, width=6,
                               command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=0, column=i)

        # Second Row: QWERTYUIOP
        second_row = 'QWERTYUIOP'
        for i, char in enumerate(second_row):
            button = tk.Button(self.keyboard_frame, text=char, width=6,
                               command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=1, column=i)

        # Third Row: ASDFGHJKL
        third_row = 'QASDFGHJKL'
        for i, char in enumerate(third_row):
            if char == 'Q':
                button = tk.Button(self.keyboard_frame, text='Tab', width=6,
                               command=self.insert_tab)
            else:
                button = tk.Button(self.keyboard_frame, text=char, width=6,
                               command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=2, column=i)

        # Fourth Row: QZXCVBNMW
        fourth_row = 'EQZXCVBNMW'
        for i, char in enumerate(fourth_row):
            if char == 'Q':
                button = tk.Button(self.keyboard_frame, text='Caps', width=6,
                                   command=self.lower_keyboard_buttons)
            elif char == 'W':
                button = tk.Button(self.keyboard_frame, text='Return', width=6,
                                   command=self.insert_newline)
            elif char == 'E':
                button = tk.Button(self.keyboard_frame, text='Delete', width=6,
                                    command=self.delete_value)
            else:
                button = tk.Button(self.keyboard_frame, text=char, width=6,
                                   command=lambda c=char: self.text_box.insert(tk.END, c))
            button.grid(row=3, column=i)

        # Fifth Row: Space Bar
        space_button = tk.Button(self.keyboard_frame, text='Space', width=24,
                                 command=lambda: self.text_box.insert(tk.END, ' '))
        space_button.grid(row=4, column=0, columnspan=6)
        
        emoji_button = tk.Button(self.keyboard_frame, text='Emoji', width=6,
                             command=self.emoji_keyboard_buttons)
        emoji_button.grid(row=4, column=0)
        
    def emoji_keyboard_buttons(self):
        # First Row: Emojis
        first_row_emojis = ['😀', '🤣', '😊', '😘', '😛', '🤭', '🤐', '😌', '😷', '🥵']
        for i, emoji in enumerate(first_row_emojis):
            emoji_char = emojize(emoji)
            button = tk.Button(self.keyboard_frame, text=emoji_char, width=6,
                           command=lambda c=emoji: self.text_box.insert(tk.END, c))
            button.grid(row=0, column=i)
        
        # Second Row: Emojis
        second_row_emojis = ['😂', '😇', '😜', '👀', '🤨', '😏', '🤒', '🥶', '🥳', '😲']
        for i, emoji in enumerate(second_row_emojis):
            emoji_char = emojize(emoji)
            button = tk.Button(self.keyboard_frame, text=emoji_char, width=6,
                           command=lambda c=emoji: self.text_box.insert(tk.END, c))
            button.grid(row=1, column=i)

        # Third Row: Emojis
        third_row_emojis = ['Tab', '😱', '😫', '😈', '🤬', '😭', '😣', '😤', '🥺', '✌️']
        for i, emoji in enumerate(third_row_emojis):
            if emoji == "Tab":
                button = tk.Button(self.keyboard_frame, text=emoji, width=6,
                               command=self.insert_tab)
            else:
                emoji_char = emojize(emoji)
                button = tk.Button(self.keyboard_frame, text=emoji_char, width=6,
                               command=lambda c=emoji: self.text_box.insert(tk.END, c))
            button.grid(row=2, column=i)
        
        # Fourth Row: Emojis
        fourth_row_emojis = ['Delete', 'Caps', '🙏', '💪', '🧠', '🫁', '🦴', '🧟‍♂️', '🙉', 'Return']
        for i, emoji in enumerate(fourth_row_emojis):
            if emoji == "Delete":
                button = tk.Button(self.keyboard_frame, text=emoji, width=6, command=self.delete_value)
            elif emoji == "Caps":
                button = tk.Button(self.keyboard_frame, text=emoji, width=6,
                               command=self.upper_keyboard_buttons)
            elif emoji == "Return":
                button = tk.Button(self.keyboard_frame, text=emoji, width=6, command=self.insert_newline)
            else:
                emoji_char = emojize(emoji)
                button = tk.Button(self.keyboard_frame, text=emoji_char, width=6,
                                   command=lambda c=emoji: self.text_box.insert(tk.END, c))
            button.grid(row=3, column=i)
    
        # Fifth Row: Space Bar
        space_button = tk.Button(self.keyboard_frame, text='Space', width=24,
                             command=lambda: self.text_box.insert(tk.END, ' '))
        space_button.grid(row=4, column=0, columnspan=12)
        
        emoji_button = tk.Button(self.keyboard_frame, text='abc', width=6,
                             command=self.lower_keyboard_buttons)
        emoji_button.grid(row=4, column=0)


    def insert_tab(self):
        self.text_box.insert(tk.INSERT, " " * 4)
        
    def delete_value(self):
        current_text = self.text_box.get("1.0", tk.END)
        updated_text = current_text[:-2]  # Remove the last character and newline character
        self.text_box.delete("1.0", tk.END)  # Clear the text box
        self.text_box.insert(tk.END, updated_text)  # Update the text box without the last character

    
    def insert_newline(self):
        self.text_box.insert(tk.END, '\n')

        # Check if the text exceeds 5 lines
        line_count = int(self.text_box.index('end-1c').split('.')[0])
        if line_count > 7:
            self.text_box.yview(tk.SCROLL, -1, "units")

root = tk.Tk()
root.geometry('550x400')
keyboard = VirtualKeyboard(root)
root.mainloop()
