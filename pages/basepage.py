from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser, url, waits):
        self.browser = browser
        self.browser.implicitly_wait(waits)
        self.url = url

    def go_to_site(self, locator):
        self.browser.get(self.url)
        self.browser.find_element(*locator).click()
        

    def create_action_chains(self):
        return ActionChains(self.browser)