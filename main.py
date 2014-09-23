#!/usr/bin/env

from functions import *
    

if __name__ == "__main__":
    print("Logged in, starting search...")
    while True:
        try:
            scanComments()
        except Exception as e:
            print("Error: ", str(e))









