import tkinter as tk

from Model import settings, Hunting, TradeSearch
from View import Login, Homepage


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("600x400")
        self.title("Welcome Pokemon Legends Bot : A Bossbot Production")
        self.resizable(height=False, width=False)

        self.frames = {}

        self.main_frame = tk.Frame(self)
        self.main_frame.place(x=0, y=0, width=600, height=400)

        for frames in (Login.LoginView, Homepage.HomepageView):
            frame = frames(parent=self.main_frame, controller=self)
            frame_name = frames.__name__
            self.frames[frame_name] = frame

        self.show_frame("LoginView")
        self.protocol(name="WM_DELETE_WINDOW", func=self.on_exit)

    def show_frame(self, frameName):
        self.frames[frameName].tkraise()

    def on_exit(self):
        # Closing Browser
        if settings.firefoxDriver is not None:
            settings.firefoxDriver.quit()

        self.destroy()


if __name__ == "__main__":
    settings.initialize()
    Hunting.initialize()
    TradeSearch.initialize()

    app = Application()
    app.mainloop()
