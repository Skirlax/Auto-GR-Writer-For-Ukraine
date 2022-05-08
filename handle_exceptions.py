import selenium.common.exceptions as selenium_exceptions


class Exceptions:
    def __init__(self):
        pass

    def handle_exceptions(self, e):
        for x in selenium_exceptions.__dict__.values():
            if isinstance(e, x):
                print(e)
