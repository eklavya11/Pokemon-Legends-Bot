import random
import threading
import time
import winsound

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import Controller.keyboard
import Model.settings
import Model.tracer


def start_hunting(parent, alignement, hunt_list, ignore_list):
    print("Alignment: " + str(alignement))
    if hunt_list.__len__() != 0:
        string = "Hunting List contains: "
        for poke in hunt_list:
            string = string + poke
            string = string + " "
        print(string)

    if ignore_list.__len__() != 0:
        string = "Ignore List contains: "
        for poke in ignore_list:
            string = string + poke
            string = string + " "
        print(string)

    thread_hunt = threading.Thread(
        target=lambda: start_hunting_to_be_called_by_thread(parent, alignement, hunt_list, ignore_list))
    thread_hunt.start()


def start_hunting_to_be_called_by_thread(parent, alignment, hunt_list, ignore_list):
    firefox_diver = Model.settings.firefoxDriver
    window_handle = Model.settings.windowHandle1

    while parent.hunting_running.get():

        if alignment == "Left":
            Controller.keyboard.go_left(window_handle)
        elif alignment == "Right":
            Controller.keyboard.go_right(window_handle)
        elif alignment == "Up":
            Controller.keyboard.go_up(window_handle)
        else:
            Controller.keyboard.go_down(window_handle)

        random_int = random.randint(0, 10)

        Controller.keyboard.hold_key(window_handle, 90)  # Z-button hold

        if alignment == "Left" or alignment == "Right":
            Controller.keyboard.go_left(window_handle)
            Controller.keyboard.go_left(window_handle)
            Controller.keyboard.go_right(window_handle)
            Controller.keyboard.go_right(window_handle)

            if random_int % 2 == 0:
                Controller.keyboard.go_left(window_handle)
                Controller.keyboard.go_right(window_handle)
        else:
            Controller.keyboard.go_up(window_handle)
            Controller.keyboard.go_up(window_handle)
            Controller.keyboard.go_down(window_handle)
            Controller.keyboard.go_down(window_handle)

            if random_int % 2 == 0:
                Controller.keyboard.go_up(window_handle)
                Controller.keyboard.go_down(window_handle)

        Controller.keyboard.release_key(window_handle, 90)  # Z-button releases

        if has_any_poke_encountered(firefox_diver) and has_desired_pokemon_encountered(firefox_diver, hunt_list,
                                                                                       ignore_list):
            parent.pause_hunting()


def has_any_poke_encountered(firefoxdriver):
    for i in range(20):
        try:
            my_text = firefoxdriver.find_element_by_css_selector("#mws-explore-encounter").text
            if 'You have' in my_text:
                return True
            elif 'No Pokemon' in my_text:
                return False
            elif 'Loading' in my_text:
                time.sleep(0.25)
                continue
        except StaleElementReferenceException:
            time.sleep(0.25)
        except NoSuchElementException:
            Model.tracer.log("Fatal Error Received in Thread->has_any_poke_encountered(). Exiting Process")
            exit(0)
    return False


def has_desired_pokemon_encountered(firefoxdriver, hunting_list, ignore_list):
    encountered_text = firefoxdriver.find_element_by_css_selector("#mws-explore-encounter").text

    if 'Gible' in encountered_text or 'Bagon' in encountered_text:
        winsound.Beep(2000, 200)
        return True
    elif 'Shiny' in encountered_text:
        Model.tracer.log(encountered_text)
        for ignore in ignore_list:
            if ignore in encountered_text:
                return False
        winsound.Beep(2000, 200)
        return True
    else:
        for hunt in hunting_list:
            if hunt in encountered_text:
                winsound.Beep(2000, 200)
                return True

    return False
