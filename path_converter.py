"""
This program interacts with the user through the main function to get a filepath
, determines the platform of their system, compares the two platforms and 
responds accordingly to convert between windows and mac or vice versa if 
necessary.  Finally it prints out a response to the user.

Functions:
- Windows to Mac converter
- Mac to Windows converter
- Main function

Author: Jimmy Shultz
Date: 2/24/2024
Version: 1.0
"""

import platform

def windows_to_mac(filepath):
    """
    Takes a given absolute file path in Windows format and changes it to Mac
    input: string of a windows filepath
    output: string of the same filepath in mac format
    """
    #Remove the drive name
    filepath = filepath[2:]

    #Reverse the slashes
    filepath = filepath.replace("\\", "/")

    #Remove quotations and replace with a slash
    filepath = filepath.replace("\"", "")
    filepath = filepath.replace(" ", "\\ ")

    return filepath

def mac_to_windows(filepath):
    """
    Takes a given absolute file path in Mac format and changes it to Windows
    input: string of a mac filepath
    output: string of the same filepath in windows format
    """

    filepath_as_list = filepath.split("/")
    converted_filepath_as_list = []
    for section in filepath_as_list:
        if "\\" in section:
            section = section.replace("\\ ", " ")
            section = "\"" + section + "\""
        converted_filepath_as_list.append(section)
    filepath = "\\".join(converted_filepath_as_list)

    #Add on the C drive
    filepath = "C:" + filepath

    return filepath

def main():
    """
    Main function that runs the program to interact with the user.
    """

    capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                       "W", "X", "Y", "Z"]

    #find out the platform system platform.system()
    type_of_platform = platform.system()
    if type_of_platform == "Darwin":
        print("You are using a Mac.")
    elif type_of_platform == "Windows":
        print("You are using a Windows operating system.")
    
    #ask user for the file path
    user_filepath = input("Please enter the full file path name you want to "
                          "convert to your current OS: ")
    
    #determine if file path is MacOS or Windows
    if user_filepath[0] == "/":
        type_of_filepath = "Darwin"
    elif user_filepath[0] in capital_letters:
        type_of_filepath = "Windows"
    else:
        type_of_filepath = ""
    
    #if system is MacOS and file path is Windows
        #convert file path to MacOS
        #display to user
    if type_of_platform == "Darwin":
        if type_of_filepath == "Darwin":
            print("The filepath you gave me already matches your MacOS as "
                  "written: ", user_filepath)
        elif type_of_filepath == "Windows":
            converted_filepath = windows_to_mac(user_filepath)
            print("When your filepath is converted from Windows to Mac it "
                  "becomes: ", converted_filepath)
        else:
            print("The file path you've submitted is not valid Windows or "
                  "MacOS.")
    elif type_of_platform == "Windows":
        if type_of_filepath == "Windows":
            print("The filepath you gave me already matches your Windows "
                  "operating system as written: ", user_filepath)
        elif type_of_filepath == "Darwin":
            converted_filepath = mac_to_windows(user_filepath)
            print("When your filepath is converted from Mac to Windows it "
                  "becomes: ", converted_filepath)
        else:
            print("The file path you've submitted is not valid Windows or "
                  "MacOS.")
    else:
        print("Your system is not Windows or MacOS.")

if __name__ == "__main__":
    main()