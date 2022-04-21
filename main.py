import get_input
import write_reviews
from sys import exit
from time import sleep

gi = get_input.HandleUserInput()
wr = write_reviews.WriteGoogleReviews()


class MainRun:
    def run_all(self):
        wr.remove_dups()
        line_number = 0
        number_of_reviews_written = 0
        how_long_to_wait = gi.get_input()
        wr.login_to_maps()
        while True:
            place, url = wr.write_reviews(line_number)
            number_of_reviews_written += 1
            line_number += 1
            if number_of_reviews_written == 3:
                number_of_reviews_written = 0
                try:
                    print("Program is now going to wait for the time you gave us above, "
                          "so we can stay undetected"
                          "Press: 'Ctrl + c' anytime to exit")
                    wr.remove_places_from_list()
                    number_of_reviews_written = 0
                    sleep(how_long_to_wait)
                    # if key := gi.ask_to_find_new_places():
                    #     wr.search_for_places(key)
                except KeyboardInterrupt:
                    print("Exiting the program...")
                    wr.write_logs(place, url)
                    exit(0)
            wr.write_logs(place, url)


if __name__ == "__main__":
    MainRun().run_all()
