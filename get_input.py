from termcolor import colored


class HandleUserInput:
    def get_input(self):
        message_to_write = input("Do you have a specific message in mind, that you want to use?"
                                 "If so, please type it in now \n"
                                 "If not please type 'x' and the program is going to use a default one: ")
        how_long_to_wait = int(input("How long should we wait between the sessions of writing?\n"
                                     "Please keep in mind that shorter the pause, higher the risk of"
                                     "google banning your account. So choose the number wisely.\n "
                                     "Type the INTEGER (only in seconds) here: "))

        return message_to_write, how_long_to_wait

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
        else: return False

