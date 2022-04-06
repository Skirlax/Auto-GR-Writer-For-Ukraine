import time

from termcolor import colored


class HandleUserInput:
    def get_input(self):
        print("You can edit the message you want to add in the text file called"
                                 " 'message.txt' in the same directory as this script.")
        time.sleep(1)
        how_long_to_wait = int(input("How long should we wait between the sessions of writing?\n"
                                     "Please keep in mind that shorter the pause, higher the risk of"
                                     "google banning your account. So choose the number wisely.\n "
                                     "Type the INTEGER (only in seconds) here: "))

        return how_long_to_wait

    def check_input(self, elements):
        for x in elements:
            if x == "":
                raise Exception(colored("Fields CANNOT be empty!", "cyan"))

    def login_to_goole_prompt(self):
        print(colored(f"Now please login to google by yourself, so google won't find out, that we're using a bot."
                      f"After you've successfully logged in, please type: (y)", "green"))
        logged_in = input(colored("Are you logged in? (y): ", "red"))
        if logged_in == "y":
            return True
        else:
            return False
        
    def ask_to_find_new_places(self):
        print(colored("Do you want to find new places? (y/n): ", "green"))
        answer = input(colored("(y/n): ", "red"))
        if answer == "y":
            key = input(colored("API key: ", "red"))
            return key
        else:
            return False
