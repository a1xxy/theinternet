from .basepage import BasePage
from locators.pagelocators import Locators as L
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AddRemoveElements(BasePage):
    def __init__(self, browser, url, waits, number=1):
        super().__init__(browser, url, waits)
        self.go_to_site(L.ADDREMOVE)
        self.number = number

    def add_element(self):
        element = self.browser.find_element(*L.ADDELEMENT)
        
        if self.number == 1:
            element.click()
            return element
        else:
            for i in range(self.number):
                element.click()
           
            return element
        
    def find_delete_button(self):
        if self.number > 1:
            try:
                elements = self.browser.find_elements(*L.REMOVEELEMENT)
                for el in elements:
                    el.click()
                return elements
            except NoSuchElementException:
                return 'Elements not found'
        else:
            try:
                element = self.browser.find_element(*L.REMOVEELEMENT)
                return element
            except NoSuchElementException:
                return 'Element not found'
    
    def should_be_deleted(self):
        assert self.find_delete_button() == 'Element not found' or 'Elements not found'

class CheckBoxes(BasePage):
    
    def __init__(self, browser, url, waits, number_of_checkboxes: int=1, checkbox_number: int=1):
        super().__init__(browser, url, waits)
        self.go_to_site(L.CHECKBOXES)
        self.checkboxes = [self.browser.find_element(*L.CHECKBOX1), self.browser.find_element(*L.CHECKBOX2)]
        self.number_of_checkboxes = number_of_checkboxes
        self.checkbox_number = checkbox_number

    def find_checkboxes(self):
        if self.checkbox_number == 1:
            for checkbox in self.checkboxes:
                checkbox.click()
        elif self.number_of_checkboxes == 2:
            self.checkboxes[0].click()

    def should_be_checked(self):
        if self.number_of_checkboxes == 2:
            assert self.checkboxes[0].get_attribute('checked') and self.checkboxes[1].get_attribute('checked') == 'true'
        else:
            assert self.checkboxes[0].get_attribute('checked') or self.checkboxes[1].get_attribute('checked') == 'true'
        
class ContextMenu(BasePage):
    def __init__(self, browser, url, waits):
        super().__init__(browser, url, waits)
        self.go_to_site(L.CONTEXTMENU)
        self.action_chain = self.create_action_chains()
        self.clickable = self.browser.find_element(*L.HOT_SPOT)
        
    def click_context_menu(self):
        self.action_chain.context_click(self.clickable).perform()

    def should_be_open_alert(self):
        alert_text = self.browser.switch_to.alert.text
        assert alert_text == 'You selected a context menu'

class DragAndDrop(BasePage):
    def __init__(self, browser, url, waits):
        super().__init__(browser, url, waits)
        self.go_to_site(L.DRAGANDDROP)
        self.action_chain = self.create_action_chains()
        self.column_a = self.browser.find_element(*L.COLUMNA)
        self.column_b = self.browser.find_element(*L.COLUMNB)

    def drag_and_drop(self):
        self.action_chain.drag_and_drop(self.column_a, self.column_b).perform()

    def should_be_drag(self):
        assert 'A' == self.column_b.text

class BrokenImages(BasePage):
    def __init__(self, browser, url, waits):
        super().__init__(browser, url, waits)
        self.go_to_site(L.BROKENIMAGES)
        self.src = {}
       
    def get_src(self):
        for number in range(2, 5):
            image = self.browser.find_element(By.CSS_SELECTOR, f'img:nth-child({number})')
            src = image.get_attribute('src')
            if src.find('img') != -1:
                self.src[f'image{number-1}'] = 'true'
            else:
                self.src[f'image{number-1}'] = 'false'

    def should_be_not_broken(self):
        counter = 0
        for value in self.src.values():
            if value == 'true':
                counter += 1
        print(self.src)
        assert counter == 3

class JSAlerts(BasePage):
    def __init__(self, browser, url, waits):
        super().__init__(browser, url, waits)
        self.go_to_site(L.JSALERTS)

    def alert(self):
        element = self.browser.find_element(*L.ALERT)
        element.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        result_text = self.browser.find_element(*L.RESULT).text
        assert result_text == 'You successfully clicked an alert'
    
    def confirm(self):
        element = self.browser.find_element(*L.CONFIRM)
        element.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        result_text = self.browser.find_element(*L.RESULT).text
        assert result_text == 'You clicked: Ok'
    
    def prompt(self):
        text = 'test'
        element = self.browser.find_element(*L.PROMPT)
        element.click()
        alert = self.browser.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        result_text = self.browser.find_element(*L.RESULT).text
        assert result_text == f'You entered: {text}'

class MultipleWindows(BasePage):
    def __init__(self, browser, url, waits):
        super().__init__(browser, url, waits)
        self.go_to_site(L.WINDOWS)

    def create_and_switch_window(self):
        self.browser.find_element(*L.OPENWINDOW).click()
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[-1])
    def assert_text(self):
        assert self.browser.find_element(*L.TEXT).text == 'New Window'

