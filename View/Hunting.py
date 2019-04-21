import tkinter as tk
from tkinter import ttk

import Controller.Hunting
from Model import Hunting


class HuntingView(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.controller = controller

        self.hunting_running = tk.BooleanVar()
        self.hunting_running.set(False)

        # ki map select krse setar vittitey Pokemon List update hobe.
        self.chosen_map = tk.StringVar()
        self.chosen_map.set(Hunting.map_list[0])
        self.chosen_map.trace("w", callback=self.update_list_of_pokemons_in_that_map)

        self.chosen_pokemon = tk.StringVar()
        self.chosen_pokemon.set(Hunting.pokemons_in_that_map[0][0])

        self.catch_pokemon = tk.BooleanVar()

        self.alignment = tk.StringVar()
        self.alignment.set("Left")

        self.current_hunt_pokemon = tk.StringVar()
        self.current_ignore_pokemon = tk.StringVar()

        tempx = 140
        tempy = 60

        tk.Label(self, text="         Choose Map:").place(x=tempx, y=tempy)
        ttk.Combobox(self, textvariable=self.chosen_map, values=Hunting.map_list).place(x=tempx + 105, y=tempy)

        tk.Label(self, text="Choose Pokemon:").place(x=tempx, y=tempy + 25)
        self.option_choose_pokemon = ttk.Combobox(self, textvariable=self.chosen_pokemon,
                                                  values=Hunting.pokemons_in_that_map[0])
        self.option_choose_pokemon.place(x=tempx + 105, y=tempy + 25)

        tk.Label(self, text="Choose Alignment:").place(x=tempx - 5, y=tempy + 50)
        tk.Radiobutton(self, text="Left", variable=self.alignment, value="Left").place(x=tempx + 105, y=tempy + 50)
        tk.Radiobutton(self, text="Right", variable=self.alignment, value="Right").place(x=tempx + 155, y=tempy + 50)
        tk.Radiobutton(self, text="Up", variable=self.alignment, value="Up").place(x=tempx + 205, y=tempy + 50)
        tk.Radiobutton(self, text="Down", variable=self.alignment, value="Down").place(x=tempx + 255, y=tempy + 50)

        tempx1 = tempx + 30
        tempy1 = tempy + 100

        ttk.Button(self, text=" Add To Ignore List ", command=self.add_to_ignore_list).place(x=tempx1 + 5,
                                                                                             y=tempy1 - 25)
        ttk.Button(self, text=" Add To Hunt List ", command=self.add_to_hunt_list).place(x=tempx1 + 10 + 150,
                                                                                         y=tempy1 - 25)

        self.ignorelist = tk.Listbox(self, height=3)
        self.ignorelist.place(x=tempx1, y=tempy1)

        self.huntlist = tk.Listbox(self, height=3)
        self.huntlist.place(x=tempx1 + 150, y=tempy1)

        tk.Label(self, text="*Pokemons inside the Ignore List will be ignored even if it is Shiny").place(x=tempx1 - 35,
                                                                                                          y=tempy1 + 80)
        tk.Label(self, text="*Pokemons inside the Hunt List will be notified even if it is Normal").place(x=tempx1 - 35,
                                                                                                          y=tempy1 + 100)
        ttk.Button(self, text="Remove", command=self.remove_from_ignore_list).place(x=tempx1 + 25, y=tempy1 + 55)
        ttk.Button(self, text="Remove", command=self.remove_from_hunt_list).place(x=tempx1 + 170, y=tempy1 + 55)

        # self.huntlist.insert(tk.END, "test1")
        # self.huntlist.insert(tk.END, "test2")

        # test = self.huntlist.get(0,tk.END)
        # for f in test:
        #     print(f)

        self.control_button = ttk.Button(self, text="Start", command=self.hunting)
        self.control_button.place(x=tempx1 + 100, y=tempy1 + 140)

    def update_list_of_pokemons_in_that_map(self, *args):

        if self.chosen_map.get() in Hunting.map_list:
            map_index = Hunting.map_list.index(self.chosen_map.get())
            self.option_choose_pokemon['values'] = Hunting.pokemons_in_that_map[map_index]
            self.chosen_pokemon.set(Hunting.pokemons_in_that_map[map_index][0])
            self.ignorelist.delete(0, tk.END)
            self.huntlist.delete(0, tk.END)
        else:
            self.option_choose_pokemon['values'] = []
            self.chosen_pokemon.set("")

    def add_to_hunt_list(self):
        map_index = Hunting.map_list.index(self.chosen_map.get())
        if self.chosen_pokemon.get() in Hunting.pokemons_in_that_map[map_index]:
            self.huntlist.insert(tk.END, self.chosen_pokemon.get())
        else:
            print("Wrong Pokemon Name")

    def add_to_ignore_list(self):
        map_index = Hunting.map_list.index(self.chosen_map.get())
        if self.chosen_pokemon.get() in Hunting.pokemons_in_that_map[map_index]:
            self.ignorelist.insert(tk.END, self.chosen_pokemon.get())
        else:
            print("Wrong Pokemon Name")

    def remove_from_hunt_list(self):
        if self.huntlist.curselection():
            self.huntlist.delete(tk.ANCHOR)
        else:
            print("No pokemon to remove from Hunt List")

    def remove_from_ignore_list(self):
        if self.ignorelist.curselection():
            self.ignorelist.delete(tk.ANCHOR)
        else:
            print("No pokemon to remove from Ignore List")

    def get_hunting_list(self):
        return self.huntlist.get(0, tk.END)

    def get_ignore_list(self):
        return self.ignorelist.get(0, tk.END)

    def hunting(self):
        if self.control_button['text'] == "Start":
            self.start_hunting()
        else:
            self.pause_hunting()

    def start_hunting(self):
        print("Hunting has been started")

        self.control_button['text'] = "Pause"
        self.hunting_running.set(True)
        Controller.Hunting.start_hunting(self, self.alignment.get(), self.get_hunting_list(), self.get_ignore_list())

    def pause_hunting(self):
        print("Hunting has been paused")

        self.control_button['text'] = "Start"
        self.hunting_running.set(False)
