import tkinter
import tkinter.messagebox
import tkinter.filedialog
 
from PIL import Image, ImageTk, ImageDraw
 
 
class MainWindow():
    def __init__(self, root):
        self.root = root
        self.create_menu()
 
        self.image = None
        self.photo = None
 
        self.display = tkinter.Canvas(root, width=500, height=450, bg="white")
        self.display_img = self.display.create_image(0, 0, tag="group1")
        self.display.pack()
 
    def create_menu(self):
        menu = tkinter.Menu(self.root)
 
        self.file_menu = tkinter.Menu(menu)
        menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", command=self.save, state='disabled')
        self.file_menu.add_command(label="Close", command=self.close)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)
 
        self.edit_menu = tkinter.Menu(menu)
        menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Gray", command=self.grey, state='disabled')
 
        self.root.config(menu=menu)
 
    def open(self):
        filename = tkinter.filedialog.askopenfilename()
        if filename:
            self.image = Image.open(filename)
            self.photo = ImageTk.PhotoImage(self.image)
            self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
 
            self.file_menu.entryconfig("Save", state='active')
            self.edit_menu.entryconfig("Gray", state='active')

    def close(self):
        if tkinter.messagebox.askyesno('Verify', 'Really clode image?'):
            self.display.itemconfigure(self.display_img, image="", anchor="nw")
        else:
            tkinter.messagebox.showinfo('No', 'close has been cancelled')
 
    def exit(self):
        if tkinter.messagebox.askyesno('Verify', 'Really quit?'):
            self.root.destroy()
        else:
            tkinter.messagebox.showinfo('No', 'Quit has been cancelled')
 
    def save(self):
        path = tkinter.filedialog.asksaveasfilename()
        if path:
            try:
                self.image.save(path)
            except KeyError:
                tkinter.messagebox.showerror('error', 'no extention')
 
    def grey(self):
        draw = ImageDraw.Draw(self.image)
        pix = self.image.load()
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                average = (pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) // 3
                draw.point((i, j), (average, average, average))
 
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
 
 
root = tkinter.Tk()
window = MainWindow(root)
root.geometry('500x450')
root.mainloop()
