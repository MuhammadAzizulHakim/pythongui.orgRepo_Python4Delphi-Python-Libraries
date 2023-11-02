from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)

img = Image.open("C:/Users/ASUS/Pillow+ChatGPT/harbour-seal-pups.jpg")
photo = ImageTk.PhotoImage(img)

canvas.create_image(250, 250, image=photo)

canvas.pack()
root.mainloop()
