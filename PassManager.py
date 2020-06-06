import pyglet
import tkinter

pyglet.font.add_file('font 1.ttf')
pyglet.font.add_file('font 2.otf')
pyglet.font.add_file('font 3.otf')


class Master:

    def __init__(self):
        self.master = tkinter.Tk()
        self.master.geometry("415x432+600+200")
        self.master.title("PassManager")
        self.master.resizable(False, False)
        self._frame = None
        self.switch_frame(StartPage(self, self.master))

    def run_main_loop(self):
        self.master.mainloop()

    def switch_frame(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame
        self._frame.place(relwidth=1, relheight=1)


class Database:

    def __init__(self):
        self.content = []

    def database_check(self):
        try:
            with open("database.txt", 'r') as data:
                self.content = data.readlines()
                if not self.content:
                    return False
                else:
                    return True
        except FileNotFoundError:
            with open("database.txt", 'w') as _:
                return False

    @staticmethod
    def append_content(password, platform=None):
        with open("database.txt", "a") as db:
            print("Platform: {} \tPass: {}".format(platform, password), file=db)

    def viewContent(self):
        with open("database.txt", 'r') as data:
            outputString = " "
            self.content = data.readlines()
            for line in self.content:
                outputString += line
            return outputString


def StartPage(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='#A44242')
    data = Database()
    if data.database_check():
        tkinter.Label(frame, text="Welcome Back!", font="{Stabillo Medium} 40", fg="white", background='#A44242'). \
            grid(row=0, column=0, columnspan=2, pady=10)
        tkinter.Label(frame, text="Master Password ", background='#A44242', font="MOMCAKE 25", fg="white"). \
            grid(row=2, column=0)
        masterPass = tkinter.Entry(frame, background='#A44242', font="ABeeZee 25", fg="white",
                                   relief='groove', borderwidth=5)
        masterPass.grid(row=3, column=0, pady=15)

        def CheckPass():
            with open("database.txt", "r") as db:
                content = db.readline().strip("\n")
                if content == "Master Key: " + masterPass.get():
                    in_self.switch_frame(showPage(in_self, root))
                else:
                    tkinter.Label(frame, text="Please try again :(", background='#A44242', font="MOMCAKE 25",
                                  fg="white"). \
                        grid(row=4, column=0, pady=10)

        tkinter.Button(frame, width=10, text="OK", background='#A44242', font="MOMCAKE 25", fg="white",
                       command=CheckPass). \
            grid(row=5, column=0)

    else:
        tkinter.Label(frame, text="Get Started!", font="{Stabillo Medium} 50", fg="white", background='#A44242').grid \
            (row=0, column=0, columnspan=2, padx=75)
        tkinter.Button(frame, text="Create Account", font="{Stabillo Medium} 30", fg="white", background='#A44242',
                       command=lambda:
                       in_self.switch_frame(GetStarted(in_self, root))).grid(row=1, column=0, pady=80, padx=80)

    return frame


def GetStarted(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='#A44242')
    tkinter.Label(frame, text="Name", font="{Stabillo Medium} 40", fg="white", background='#A44242'). \
        grid(row=1, column=1)
    tkinter.Entry(frame, background='#A44242', font="ABeeZee 25", fg="white").grid(row=2, column=1)
    tkinter.Label(frame, text="New Master Password", font="{Stabillo Medium} 40", fg="white",
                  background='#A44242').grid(row=3, column=1)
    store_master = tkinter.Entry(frame, background='#A44242', font="ABeeZee 25", fg="white")
    store_master.grid(row=4, column=1)
    tkinter.Button(frame, text="Save", font="{Stabillo Medium} 40", fg="white", background='#A44242',
                   command=lambda: store_and_redirect()).grid(row=5, column=1)

    def store_and_redirect():
        with open("database.txt", "a") as db:
            print("Master Key: " + store_master.get(), file=db)
        in_self.switch_frame(StartPage(in_self, root))

    return frame


def showPage(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='#A44242')
    show_text = tkinter.Text(root, height=15, width=34, font="ABeeZee 15", fg="white", background='#A94949'
                             , borderwidth=3)
    show_text.grid(row=1, column=0)
    DataBase = Database()
    show_text.insert(tkinter.END, DataBase.viewContent())
    tkinter.Button(root, text="Add Password", font="{Stabillo Medium} 30", fg="white", background='#A44242',
                   command=lambda: in_self.switch_frame(AddPass(in_self, root))).grid \
        (row=2, column=0, sticky="sw")
    return frame


def AddPass(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='#A44242')
    tkinter.Label(frame, text="Platform", font="{Stabillo Medium} 40", fg="white", background='#A44242'). \
        grid(row=0, column=0)
    plat = tkinter.Entry(frame, background='#A44242', font="ABeeZee 25", fg="white")
    plat.grid(row=1, column=0, pady=10)
    tkinter.Label(frame, text="Password", font="{Stabillo Medium} 40", fg="white", background='#A44242'). \
        grid(row=2, column=0, pady=10)
    _pass = tkinter.Entry(frame, background='#A44242', font="ABeeZee 25", fg="white")
    _pass.grid(row=3, column=0, pady=10)
    tkinter.Button(frame, width=10, text="Save", font="{Stabillo Medium} 30", fg="white", background='#A44242',
                   command=lambda: addPassFunc()).grid(row=4, column=0, pady=10)

    def addPassFunc():
        data = Database()
        data.append_content(platform=plat.get(), password=_pass.get())
        in_self.switch_frame(showPage(in_self, root))

    return frame


master = Master()
master.run_main_loop()
