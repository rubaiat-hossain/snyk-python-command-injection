#!/usr/bin/env python3

import os
import subprocess

def exploit_user_controlled_input():
    # Vulnerability: Directly using user-controlled input to execute a command.
    command = input("Enter a command to execute: ")
    os.system(command)

def insecure_system_command():
    # Vulnerability: Using subprocess with shell=True and direct user input.
    command = input("Enter a command for subprocess: ")
    subprocess.run(command, shell=True)


def dynamic_command_construction():
    # Vulnerability: Dynamically constructing command without any checks.
    user_input = input("Enter a parameter: ")
    command = f"echo Printing {user_input}"
    os.system(command)

def misuse_of_eval():
    user_input = input("Enter a Python expression to evaluate: ")
    try:
        result = eval(user_input)
        print(f"Result:\n{result}")
    except Exception as e:
        print(f"Error:\n{e}")


if __name__ == "__main__":
    print("1. Exploit User-Controlled Inputs")
    print("2. Insecure System Commands/Subprocess Module")
    print("3. Dynamic Command Construction")
    print("4. Misuse of the eval() Function")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        exploit_user_controlled_input()
    elif choice == "2":
        insecure_system_command()
    elif choice == "3":
        dynamic_command_construction()
    elif choice == "4":
        misuse_of_eval()
    else:
        print("Invalid option!")
