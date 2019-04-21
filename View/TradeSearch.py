import tkinter as tk


class TradesearchView(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.controller = controller

        self.chosen_pokemon = tk.StringVar()

        tk.Label(self, text="Not Implemented Yet", font=("Helvetica", 16)).place(x=185, y=145)

        # label_choose_pokemon = tk.Label(self, text="Choose Pokemon:")
        # label_choose_pokemon.place(x=tempx, y=tempy)
        #
        # option_choose_pokemon = ttk.Combobox(self, textvariable=self.chosen_pokemon,
        #                                      values=TradeSearch.pokemon)
        # option_choose_pokemon.place(x=tempx + 105, y=tempy)
