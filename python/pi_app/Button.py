import requests
import Config


class Button(object):

    def __init__(self, page, number):
        self.page = page
        self.number = number

    def press(self):
        requests.get("http://{}:{}/press/bank/{}/{}"
                     .format(Config.companion_ip, Config.companion_port, self.page, self.number))
