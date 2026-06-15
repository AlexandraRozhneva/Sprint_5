from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, MoveTargetOutOfBoundsException
import logging
import time

logger = logging.getLogger(__name__)

def scroll_to_element(driver, element):
    """Плавная прокрутка к элементу"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)

def wait_and_click(driver, locator, timeout=15):
    """
    Ожидание кликабельности элемента, прокрутка и стандартный клик
    С обработкой перекрытий
    """
    # Ждем, пока элемент станет видимым
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    
    # Прокручиваем к элементу
    scroll_to_element(driver, element)
    
    # Дополнительная прокрутка, чтобы убедиться, что элемент не перекрыт
    driver.execute_script("window.scrollBy(0, -100);")
    
    # Ждем, пока элемент станет кликабельным
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    
    # Пробуем кликнуть с обработкой перехвата
    try:
        element.click()
    except ElementClickInterceptedException:
        # Если элемент перехвачен, пробуем закрыть перекрывающий элемент
        try:
            # Пробуем нажать Escape для закрытия возможных модальных окон
            driver.find_element(By.TAG_NAME, 'body').send_keys(u'\ue00c')
        except:
            pass
        
        # Пробуем кликнуть еще раз
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    return element

def get_active_tab_text(driver):
    """Получение текста активного таба"""
    try:
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]"))
        )
        text_element = active_tab.find_element(By.TAG_NAME, "span")
        return text_element.text
    except:
        return None
    
def close_overlays(driver):
    """Закрытие возможных перекрывающих элементов"""
    try:
        # Проверяем наличие кнопки закрытия модального окна
        close_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'close') or contains(@class, 'CloseButton')]")
        for button in close_buttons:
            if button.is_displayed():
                button.click()
                WebDriverWait(driver, 3).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal')]"))
                )
    except:
        pass

def wait_and_click_safe(driver, locator, timeout=15):
    """Максимально безопасный клик с обработкой всех возможных проблем"""
    # Закрываем перекрывающие элементы
    close_overlays(driver)
    
    # Ждем элемент
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    
    # Прокручиваем
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    # Небольшая пауза для завершения анимации
    time.sleep(0.5)
    
    # Пробуем разные способы клика
    try:
        element.click()
    except ElementClickInterceptedException:
        # Пробуем кликнуть через JavaScript как крайний случай
        driver.execute_script("arguments[0].click();", element)
    
    return element