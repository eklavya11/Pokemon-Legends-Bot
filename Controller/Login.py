import threading
import time
import win32gui

from selenium import webdriver

import Model.settings
import Model.tracer


def login(username, password, rememberme, view_controller):
    # Process Remember Me
    if rememberme:
        pass  # we have to update login credentials
    else:
        pass
        # we have to delete login credentials if there is any

    # Check Credentials
    print("Credentials Checked")

    # Switch Window
    # print("Going to visit the next page ")
    # view_controller.controller.show_frame("HomepageView")
    thread2 = threading.Thread(target=lambda: change_window_to_be_called_by_thread(view_controller))
    thread2.start()


    # Do Login
    thread1 = threading.Thread(target=lambda: login_to_be_called_by_thread(username, password, view_controller))
    thread1.start()


def login_to_be_called_by_thread(username, password, view_controller):
    profile = webdriver.FirefoxProfile(Model.settings.profileDirectory)
    Model.tracer.log("Profile Creation has been completed.")

    Model.settings.firefoxDriver = webdriver.Firefox(profile)
    Model.tracer.log("Browser has been opened.")

    Model.settings.firefoxDriver.get("https://www.pokemonlegends.com/")
    Model.settings.windowHandle1 = win32gui.FindWindow(None,
                                                       "Pokémon Legends - Play Pokemon Online. "
                                                       "Online MMORPG Pokemon Game - Mozilla "
                                                       "Firefox")
    Model.tracer.log("Site Pokemon Legends has been opened. Going to sleep for 1 sec\n")
    time.sleep(1)

    Model.settings.firefoxDriver.find_element_by_id("user-email").send_keys(username)
    Model.settings.firefoxDriver.find_element_by_id("user-pw").send_keys(password)
    Model.settings.firefoxDriver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div/div/div[1]/div[1]/form/div[4]/button").click()

    Model.tracer.log("Login Successful")
    Model.tracer.log("Received handle has the following title: " +
                     win32gui.GetWindowText(Model.settings.windowHandle1) + "\n")

    view_controller.set_login_status_true()


def change_window_to_be_called_by_thread(controller):
    while not controller.get_login_status():
        time.sleep(5)

    controller.controller.show_frame("HomepageView")
