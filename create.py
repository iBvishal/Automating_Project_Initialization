import sys
import os

# get password while displaying nothing
import getpass

# for github stuff
from github import Github

def create():
    current_working_directory = os.getcwd()
    folderName = str(sys.argv[1])
    try:
        os.makedirs(current_working_directory + folderName)
        username = input("Username : ")
        password = getpass.getpass(prompt="Password : ")
        try:
            user = Github(username, password).get_user()
            repo = user.create_repo(folderName)
            print("Succesfully created repository "+ folderName)
        except e:
            print(e)
    except OSError as e:
        print(e)
        print("Project Initialization failed...")
if  __name__ == "__main__":
    create()