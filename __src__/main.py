import os
try: 
  import dankware
  import tabulate
  import rich
  import requests
  import translatepy
  import subprocess
  import pygame
except ImportError:
  print("Trying to Install all required modules...\n")
  os.system('python -m pip install -r requirements.txt')

import time

from rich.align import Align
from rich.console import Console
from translatepy import Translator
from tabulate import tabulate
from dankware import cls, clr, title, get_duration, multithread, err, rm_line
from dankware import white, white_bright, green, green_bright, red, red_normal
from pygame import mixer

def intro():
  mixer.init()
  mixer.music.load('__assets__/intro.mp3') 
  mixer.music.set_volume(0.010)
  mixer.music.play()
def error_handler(str: str):
  cls()
  banner = """
 ██████████                                        ███
░░███░░░░░█                                       ░███
 ░███  █ ░  ████████  ████████   ██████  ████████ ░███
 ░██████   ░░███░░███░░███░░███ ███░░███░░███░░███░███
 ░███░░█    ░███ ░░░  ░███ ░░░ ░███ ░███ ░███ ░░░ ░███
 ░███ ░   █ ░███      ░███     ░███ ░███ ░███     ░░░ 
 ██████████ █████     █████    ░░██████  █████     ███
░░░░░░░░░░ ░░░░░     ░░░░░      ░░░░░░  ░░░░░     ░░░ 
                                                      
                                                      
                                                      """
  err = str
  console = Console(highlight=False)
  console.print(Align.center(banner), style="blink red")
  console.print(Align.center(err), style="red")

def synapse_banner():
    cls()
    banner = """
  █████████                                                            
 ███░░░░░███                                                           
░███    ░░░  █████ ████ ████████    ██████   ████████   █████   ██████ 
░░█████████ ░░███ ░███ ░░███░░███  ░░░░░███ ░░███░░███ ███░░   ███░░███
 ░░░░░░░░███ ░███ ░███  ░███ ░███   ███████  ░███ ░███░░█████ ░███████ 
 ███    ░███ ░███ ░███  ░███ ░███  ███░░███  ░███ ░███ ░░░░███░███░░░  
░░█████████  ░░███████  ████ █████░░████████ ░███████  ██████ ░░██████ 
 ░░░░░░░░░    ░░░░░███ ░░░░ ░░░░░  ░░░░░░░░  ░███░░░  ░░░░░░   ░░░░░░  
              ███ ░███                       ░███                      
             ░░██████                        █████                     
              ░░░░░░                        ░░░░░                      """
    console = Console(highlight=False)
    console.print(Align.center(banner), style="blink red")

def DoS():
    cls()
    title("DoS Tool")
    banner = """
 ██████████             █████████     ███████████                   ████ 
░░███░░░░███           ███░░░░░███   ░█░░░███░░░█                  ░░███ 
 ░███   ░░███  ██████ ░███    ░░░    ░   ░███  ░   ██████   ██████  ░███ 
 ░███    ░███ ███░░███░░█████████        ░███     ███░░███ ███░░███ ░███ 
 ░███    ░███░███ ░███ ░░░░░░░░███       ░███    ░███ ░███░███ ░███ ░███ 
 ░███    ███ ░███ ░███ ███    ░███       ░███    ░███ ░███░███ ░███ ░███ 
 ██████████  ░░██████ ░░█████████        █████   ░░██████ ░░██████  █████
░░░░░░░░░░    ░░░░░░   ░░░░░░░░░        ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ 
                          powered by slowloris
                                                                         """
    console = Console(highlight=False)
    console.print(Align.center(banner), style="blink red")

    functions = """
[1] Start Tool      [0] Exit"""
    
    table = [[functions]]
    output = tabulate(table, tablefmt='grid')
    console.print(Align.center(output), style="red")

    x = input(clr("\n  > Choice: "))
    if x == "0":
      main()
    elif x == "1":
        ipordomain = input(clr("\n  > IP Address: "))
        port = input(clr("\n  > Port (80): "))
        sockets = input(clr("\n  > Sockets: "))

        print("Starting DoS Attack!\nUse CTRL + C to stop!")
        if port == "80" or port == None or port == "":
          os.system(f"py slowloris.py {ipordomain} -p 80 -s {sockets}")
        else:
           os.system(f"py slowloris.py {ipordomain} -p {port} -s {sockets}")
    else:
       print("Option doesn't exist!")
       time.sleep(2)
       DoS()

def synapse_motm():
  headers = {"User-Agent": f"synapse"}
  motm = requests.get(f"https://raw.githubusercontent.com/codestantindev/synapse/main/__src__/motd.txt", headers=headers, timeout=3).content.decode()
  table = [[motm]]
  output = tabulate(table, tablefmt='grid')
  console = Console(highlight=False)
  console.print(Align.center(output), style="red")
     
def synapse_functions():
    functions = f"""
[1] OS Tools      [2] Discord Tools

[3] DoS Tool      [4] Cracking Tools

           [0] Exit"""
    table = [[functions]]
    output = tabulate(table, tablefmt='grid')
    console = Console(highlight=False)
    console.print(Align.center(output), style="red")
    x = input(clr("\n  > Choice: ") + red)
    
    if x.isdigit():
      if x == "0":
        exit()

      if x == "1":
        error_handler("Work in progress!")
        time.sleep(2)
        main()

      if x == "2":
        error_handler("Work in progress!")
        time.sleep(2)
        main()

      if x == "3":
        DoS()

      if x == "4":
        error_handler("Work in progress!")
        time.sleep(2)
        main()
      else:
        main()
    elif x == "":
      main()
    else:
      error_handler("Please input a valid number!")
      time.sleep(2)
      main()

def main():
  title("Synapse Python Tool")
  intro()
  synapse_banner()
  synapse_motm()
  synapse_functions()

main()