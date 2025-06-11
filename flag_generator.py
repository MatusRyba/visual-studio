from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

def create_flag(w, h):
    img = Image.new("RGB", (w, h), "yellow")
    draw = ImageDraw.Draw(img)
    sh = h // 3
    draw.rectangle([0, 0, w, sh], fill="black")
    draw.rectangle([0 ,2*sh , w, h], fill="red")
    return img

def main():
    root = tk.Tk()
    c = tk.Canvas(root, width=600, height=400, bg="lightgray")
    c.pack()
    imgs = []
    def click(e):
        flag = ImageTk.PhotoImage(create_flag(60, 40))
        imgs.append(flag)
        c.create_image(e.x, e.y, image=flag, anchor=tk.CENTER)
    c.bind("<Button-1>", click)
    root.mainloop()

if __name__ == "__main__":
    main()
