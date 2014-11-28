#!/usr/bin/env

import praw
import functions
    

if __name__ == "__main__":
    print("Logged in, starting search...")
    while True:
        try:
            functions.scanComments()
        except Exception as error_with_functions:
            print("Error: ", str(error_with_functions))









