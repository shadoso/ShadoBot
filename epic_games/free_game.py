import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class FireFox:
    def __init__(self, url):
        options = Options()
        options.headless = True
        path = Service("/home/bismutoso/PycharmProjects/ShadoBot/geckdrive/geckodriver")
        self.url = url
        self.firefox = webdriver.Firefox(options=options, service=path)
        # self.firefox = webdriver.Firefox(service_log_path=os.devnull, service_args=path, options=options)

    def open(self):
        self.firefox.get(self.url)

    def close(self):
        self.firefox.quit()

    def screenshot(self):
        sleep(1.5)
        self.firefox.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/main"
                                           "/div[3]/div/div/div/div/div[2]").screenshot("free_game.png")


if __name__ == '__main__':
    web = FireFox("https://www.epicgames.com/store/pt-BR/free-games")
    web.open()
    web.screenshot()
    web.close()
