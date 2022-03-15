from lib2to3.pgen2 import driver
import os
from requests import auth
from requests.api import get
from datetime import datetime
from random import randint
import time
import threading
import sys
import requests
import pathlib
import platform
try:
    import cv2
except ImportError:
    os.system('python -m pip install opencv-python')
try:
    from dotenv import load_dotenv
except ImportError:
    os.system('python -m pip install python-dotenv')
try:
    import pyautogui
except ImportError:
    os.system('python -m pip install pyautogui')
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    os.system('python -m pip install selenium')
try:
    import numpy as np
except ImportError:
    os.system('python -m pip install numpy')
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.driver import Driver
except ImportError:
    os.system('python -m pip install webdriver_manager')


#Deteccion del SO
systemOS = platform.system()
def clearFunction():
    if(systemOS == "Linux"):
        os.system("clear")
    else:
        os.system("cls")
clearFunction()
print("Running on:", systemOS)

def getDriver():
    if(systemOS == "Linux"):
        driver = webdriver.Chrome("/usr/lib/chromium/chromedriver")
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://webventas.sofse.gob.ar/calendario.php')
    return driver

driver_loaded = getDriver()
# driver_loaded.find_element_by_class_name("web")
print(driver_loaded.find_element_by_class_name("modal_aceptar").click())