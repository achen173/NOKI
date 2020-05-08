import os
import random
import time
import sys
from metadata.docx_parser import Alan
import zipfile
import xml.etree.ElementTree as ET
import re

logo = ("""

\033[1;31m

                     ███▄    █ ▒█████ ▓ █   ██▒ ▒██▒
                      ██ ▀█   █ ██▒  ██▒█░ █▒░   ▒██▒
                     ▓██  ▀█ ██▒██░  ██░███▒░    ▒██▒
                     ▓██▒  ▐▌██▒██   ██░██ █▒▒   ░██░
                     ▒██░   ▓██░ ████▓▒░█░  █░   ▒██░
                     ▒██░   ▓██░ ▒░▒░▒░ █░   ██░░░██░
                      ▒░   ▒ ▒   ░ ▒ ▒░ ░░    ░░ ▒░
                      ░░   ░ ▒░  ░ ░ ▒   ░    ░  ░▒v0.0.1
                       ░             ░           ░  
            "The quieter you become, the more you are able to hear…"

\033[1;m
            \033[1;31mNOKI v0.0.1\033[94m

    ✓ The author shall not be liable for any damage and/or misuse of information.
    ✓ NOKI shall only be used to expand knowledge, not for unlawful action.
    ✓ Always remember, Performing any hacks without consent is illegal ..!

            Author:  Alan Chen
            Github:  https://github.com/achen173
            Website: https://www.linkedin.com/in/alan-chen-3a340a166/

            \033[1;31mHi there, Welcome to NOKI's Realm, Shall we have some fun..?\033[0m
        """)

print("\n\n\n\n\n", logo)

time.sleep(0.1)
lib_list = {"help": "list of valid commands",
            "metadata":"parsing file(docx/pptx/xlsx)",
            "aircrack-ng":"wireless password cracking",
            "exit":"exit"
     }
def libraries(command):

    return command not in lib_list.keys()

def showdam():
    counter = 1
    try:
        counter = counter + 1
        print("\n \033[1;31mType help to list current capabilities\033[0m ")
        while(True):
            time.sleep(0.1)
            command = input("\n[~] \033[92mYour wish is my command > \033[0m ").split()
            if(len(command) == 0 or len(command) > 2 or libraries(command[0])):  # not 2 or cannot find first command
                print ("\n\t \033[1;91mInvalid Command \033[0m ")
            elif(command[0] == "help"):
                for item in lib_list:
                    print("\t\033[1;91m{:<20}  {:<35}\033[0m".format(item, lib_list[item]))
            elif(command[0] == "metadata"):
                temp = Alan()
                method_to_call = getattr(temp, "metadata")
                result = method_to_call(command[1])
            elif(command[0] == "exit"):
                break
            else:
                print ("\n\t \033[1;91mInvalid Command \033[0m ")


    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("\n\n\t\033[1;91mNOKI's Realm I like to See Ya, Hacking \033[0m😃\n\n")

def metadata(filename):
    try:
        zf = zipfile.ZipFile(filename)
        for name in zf.namelist():
            if 'docProps/app.xml' in name:
                root = ET.fromstring(zf.read(name))
                for child in root:
                    if('Application' in str(re.sub(r'\{[^()]*\}', '', child.tag))):
                        if('Microsoft Office Word' in child.text):
                            main(filename)
    except:
        print("Error with input file")


# =====# Main #===== #
if __name__ == "__main__":
    showdam()
    # print ("\n\t \033[1;91mN00b! N00b! N00b! " + "Testing \033[0m ")