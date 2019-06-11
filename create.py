import sys
import os

# get password while displaying nothing
import getpass

# for github stuff
from github import Github

def create():
    current_working_directory = os.getcwd()
    repoName = str(sys.argv[1])
    try:
        username = input("Username : ")
        password = getpass.getpass(prompt="Password : ")
        try:
            user = Github(username, password).get_user()
            try:
                os.makedirs(current_working_directory+"/"+repoName)
                repo = user.create_repo(repoName)
                print("Succesfully created repository '"+ repoName+"'")
            except:
                print("Couldn't ceate a github repository with name '"+repoName+"'")
                os.rmdir(repoName)
        except:
            print("Github Authorization Failed.")
    except OSError as e:
        print(e)
        print("Project Initialization failed...")
if  __name__ == "__main__":
    create()