from selenium.webdriver.common.by import By

class Locators:
    ADDREMOVE = (By.CSS_SELECTOR, '[href="/add_remove_elements/"]')
    ADDELEMENT = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    REMOVEELEMENT = (By.CSS_SELECTOR, '[onclick="deleteElement()"]')
   
    CHECKBOXES = (By.CSS_SELECTOR, '[href="/checkboxes"]')
    CHECKBOX1 = (By.CSS_SELECTOR, '.example #checkboxes > input:nth-child(1)')
    CHECKBOX2 = (By.CSS_SELECTOR, '#checkboxes > input:nth-child(3) ')
    
    CONTEXTMENU = (By.CSS_SELECTOR, '[href="/context_menu"]')
    HOT_SPOT = (By.CSS_SELECTOR, '#hot-spot')
    
    DRAGANDDROP = (By.CSS_SELECTOR, '[href="/drag_and_drop"]')
    COLUMNA = (By.ID, 'column-a')
    COLUMNB = (By.ID, 'column-b')

    BROKENIMAGES = (By.CSS_SELECTOR, '[href="/broken_images"]')
    # BROKENIMAGE = (By.CSS_SELECTOR, 'img:nth-child(X)')