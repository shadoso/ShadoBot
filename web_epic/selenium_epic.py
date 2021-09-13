from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from time import sleep


class ShadoDriver:
    def __init__(self, url):
        options = Options()
        options.headless = True
        self.url = url
        self.firefox = webdriver.Firefox(service_log_path=os.devnull, executable_path="/home/bismutto/PycharmProjects"
                                                                                      "/ShadoBot/geko/geckodriver",
                                         options=options)

    def open(self):
        self.firefox.get(self.url)

    def close_it(self):
        self.firefox.quit()

    def scree_it(self):
        sleep(0.7)
        self.firefox.find_element_by_xpath("/html/body/div[1]/div/div[4]/main/div[2]/div[3]/div/div/div/div["
                                           "2]/span/div/div/section").screenshot("free_game.png")


if __name__ == '__main__':
    web = ShadoDriver("https://www.epicgames.com/store/pt-BR/free-games")
    web.open()
    web.scree_it()
    web.close_it()
