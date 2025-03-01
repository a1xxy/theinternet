import pytest
from pages.pageobject import AddRemoveElements, CheckBoxes, ContextMenu, DragAndDrop, BrokenImages, JSAlerts
import time






@pytest.mark.skip
@pytest.mark.parametrize('numb', [1, 3, 0])
def test_add_remove(browser, numb):
    driver = AddRemoveElements(browser, 'http://the-internet.herokuapp.com/', 3, number=numb)
    driver.add_element()
    driver.find_delete_button()
    driver.should_be_deleted()

@pytest.mark.skip    
def test_checkbox(browser):
    driver = CheckBoxes(browser, 'http://the-internet.herokuapp.com/', 3, 0, 2)
    driver.find_checkboxes()
    driver.should_be_checked()


@pytest.mark.skip
def test_context_menu(browser):
    driver = ContextMenu(browser, 'http://the-internet.herokuapp.com/',3)
    driver.click_context_menu()
    driver.should_be_open_alert()

@pytest.mark.skip
def test_drag_and_drop(browser):
    driver = DragAndDrop(browser, 'http://the-internet.herokuapp.com/', 3)
    driver.drag_and_drop()
    driver.should_be_drag()
@pytest.mark.skip
def test_broken_images(browser):
    driver = BrokenImages(browser, 'http://the-internet.herokuapp.com/', 3)
    driver.get_src()
    driver.should_be_not_broken()
    
def test_alert(browser):
    driver = JSAlerts(browser, 'http://the-internet.herokuapp.com/', 3)
    driver.alert()

def test_prompt(browser):
    driver = JSAlerts(browser, 'http://the-internet.herokuapp.com/', 3)
    driver.prompt()

def test_confirm(browser):
    driver = JSAlerts(browser, 'http://the-internet.herokuapp.com/', 3)
    driver.confirm()