from selenium import webdriver
from time import sleep


class Instabot:
    def __init__(self, user_name, pass_word, gc_name, msg):

        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')
        print("[CHROME WEBDRIVER SESSION STARTED]")

        # open Instagram.com [sleep is called to make sure website boots up with xpaths ready]
        self.driver.get("https://instagram.com")
        print("[INSTAGRAM OPENED]")
        sleep(3)

        # find the username&password text boxes and enter the login info @params
        self.driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[1]/div/label/input").send_keys(user_name)
        self.driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[2]/div/label/input").send_keys(pass_word)

        # click the login button
        self.driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button").click()
        print("[LOGGED IN!]")
        sleep(4)

        # click on the DMs icon
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        print("[THATS STRANGE]")

        # close any extra notifications
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)

        # Find group chat and wait for char to load (GET XPATH FOR GROUP CHAT) (THIS ONE'S FOR IZE CLAN)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div").click()
        sleep(4)

        # Find text box and enter msg
        self.driver.find_element_by_xpath("// *[ @ id = \"react-root\"] / section / div / div[2] / div / div / div[2] / div[2] / div / div[2] / div / div / \
                                     div[2] / textarea").send_keys(msg)

        # send the message
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()
        print("[MESSAGE SUCCESSFULLY SENT] Job well done my friend")

        # close the browser (program end)
        self.driver.quit()


user = 'dev.ap3'
pw = '<password>'
chatName = '<group chat name>'
message = '<message>'
bot = Instabot(user, pw, chatName, message)

