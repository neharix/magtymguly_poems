import tkinter as tk
from random import shuffle

names = (
    "Gürgeniň",
    "Gerekdir",
    "Ýaşymyz",
    "Öňi-ardy bilinmez",
    "Gökleň",
    "Reýgan eýledi",
    "Pukaraýam",
    "Türkmen binasy",
    "Türkmeniň",
    "Depe nedir, düz nedir",
    "Meýdan ýoluksa",
    "Eýlär",
    "Görüň",
    "Aňlamaz",
    "Gerekdir",
    "Baş üstüne",
    "Gerek",
    "Oglum - Azadym",
    "Neýläýin",
    "Bilmezmiň",
    "Islärin",
    "Joşa düşüp sen",
    "Ýyglap geçer halymga",
    "Baradyr",
    "Galyp men",
    "Daşlar bile",
)


class Poem:
    def __init__(self, index: int):
        self.name = names[index]
        with open(f"poems/{index + 1}.txt", "r", encoding="utf-8") as file:
            self.content = file.read()

    def __str__(self):
        return self.name


poems = [Poem(index) for index in range(26)]
shuffle(poems)


def change_content(tab_number):
    root.title(f"{poems[tab_number].name} | Goşgy №{tab_number + 1}")
    content_label.delete(1.0, tk.END)
    content_label.insert(tk.END, poems[tab_number].content)


root = tk.Tk()
root.title("Magtymguly's poems")

button_frame = tk.Frame(root, width=150, bg="lightgrey")
button_frame.pack(side="left", fill="y")

content_frame = tk.Frame(root)
content_frame.pack(side="right", fill="both", expand=True)

content_label = tk.Text(content_frame, wrap="word", font=("Arial", 18))
content_label.pack(expand=True, side=tk.LEFT, fill=tk.Y)

sb_v = tk.Scrollbar(content_frame, command=content_label.yview)
sb_v.pack(side=tk.RIGHT, fill=tk.Y)
content_label.config(yscrollcommand=sb_v.set)

for i in range(26):
    button = tk.Button(
        button_frame,
        text=f"Goşgy {i + 1}",
        command=lambda i=i: change_content(i),
    )
    button.pack(pady=2, padx=5, fill="x")

root.mainloop()
