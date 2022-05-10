import get_input
import write_reviews

from sys import exit
from time import sleep
from datetime import datetime

gi = get_input.HandleUserInput()
wr = write_reviews.WriteGoogleReviews()


class MainRun:
    def run_all(self):
<<<<<<< HEAD
        line_number = 0
=======
>>>>>>> kamil
        number_of_reviews_written = 0
        how_long_to_wait = gi.get_input()
        wr.login_to_maps()
        while place := wr.read_places(0):

            if url := wr.write_reviews(place):
                number_of_reviews_written += 1
                try:
                    wr.write_logs(place, url,"OK", number_of_reviews_written)
                    print("review " + str(number_of_reviews_written) + " written for: " + place + " " + datetime.now().strftime("%Y-%m-%d %H-%M"))
                except Exception as inst:
                    wr.write_errorlog("Error writing log for: " + place, inst)
            else:
                wr.write_logs(place, url, "Error", number_of_reviews_written)
            wr.remove_places_from_list()

            if number_of_reviews_written > 0 and number_of_reviews_written % 3 == 0:
                try:
                    print("Program is now going to wait for the time you gave us above, "
                          "so we can stay undetected"
                          "Press: 'Ctrl + c' anytime to exit")
                    sleep(how_long_to_wait)
                    # if key := gi.ask_to_find_new_places():
                    #     wr.search_for_places(key)
                except KeyboardInterrupt:
                    print("Exiting the program...")
                    wr.write_logs(place, url)
                    exit(0)



if __name__ == "__main__":
    MainRun().run_all()
