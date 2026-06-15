from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)

def scroll_to_element(driver, element):
    """Плавная прокрутка к элементу"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)

def wait_and_click(driver, locator, timeout=15):
    """
    Ожидание кликабельности элемента, прокрутка и стандартный клик
    Не использует execute_script для клика, только для прокрутки
    """
    # Ждем, пока элемент станет кликабельным
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    
    # Прокручиваем к элементу
    scroll_to_element(driver, element)
    
    # Небольшая пауза для завершения анимации прокрутки
    # Используем implicit wait, который уже настроен в драйвере
    
    # Стандартный клик
    element.click()
    return element

def get_active_tab_text(driver):
    """Получение текста активного таба"""
    try:
        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]"))
        )
        text_element = active_tab.find_element(By.TAG_NAME, "span")
        return text_element.text
    except:
        return None