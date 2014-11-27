#!/usr/bin/env

from functions import *
    

if __name__ == "__main__":
    print("Logged in, starting search...")
    while True:
        try:
            scanComments()
        except Exception as error_with_functions:
            print("Error: ", str(error_with_functions))









