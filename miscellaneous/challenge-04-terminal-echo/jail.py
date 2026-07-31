#!/usr/bin/env python3
import re
import sys

def main():
    print("========================================")
    print("||       TERMINAL ECHO ACTIVE         ||")
    print("========================================")
    print("Input sequence required.")
    print("WARNING: Alphanumeric characters are BANNED.")
    
    try:
        user_input = input(">>> ")
    except EOFError:
        return
        
    if len(user_input) > 1000:
        print("Sequence too long.")
        return

    # Ban all letters and numbers
    if re.search(r'[a-zA-Z0-9]', user_input):
        print("ACCESS DENIED: Illegal characters detected in sequence.")
        return
    
    print("Sequence Accepted. Executing...")
    try:
        # Evaluate the input
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("Execution failed:", e)

if __name__ == "__main__":
    main()
