import tkinter as tk
from downloader import convert


window = tk.Tk()
window.title("Youtube to mp3")
window.geometry("700x100")


# youtube url entry
url_entry = tk.Entry(window,
                    font="Calibri 15",
                    width=50)
url_entry.pack()

# confirm button
confirm_button = tk.Button(window, 
                            text="CONVERT",
                            width=40, height=2,
                            command=lambda:convert(url_entry))
confirm_button.pack()




# activate infinite loop
window.mainloop()


