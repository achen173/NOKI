from tqdm import tqdm
import os
import zipfile
import sys

def attack_zip(zip_file, wordlist='./password_list/password-list-top-100000.txt'):
    zip_file = zipfile.ZipFile(zip_file)
    n_words = len(list(open(wordlist, "rb")))
    print("\n\t\033[1;91mTotal passwords to test: {}\033[0m".format(n_words))
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("\n\t\033[1;91m[+] Password found: {}\033[0m", word.decode().strip())
                wordlist.close()
                return
    print("\t\033[1;91m[!] Password not found, try other wordlist \033[0m")
