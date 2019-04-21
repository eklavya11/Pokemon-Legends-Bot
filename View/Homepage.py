import tkinter as tk
from tkinter import ttk

from View import Hunting, TradeSearch


class HomepageView(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller
        self.place(x=0, y=0, width=600, height=400)

        self.tabpane = ttk.Notebook(self)
        self.tabpane.place(x=0, y=0, width=600, height=400)

        # tab1 = tk.Frame(self.tabpane)
        # self.tabpane.add(tab1,text="Tab 1")

        hunting_tab = Hunting.HuntingView(controller, self.tabpane)
        self.tabpane.add(hunting_tab, text=" Hunting ")

        trade_tab = TradeSearch.TradesearchView(controller, self.tabpane)
        self.tabpane.add(trade_tab, text=" Trade Search ")

