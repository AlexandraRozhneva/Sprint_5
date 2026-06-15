import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators, MainPageLocators
from generators import generate_email, generate_password, generate_name
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    logger.info("Браузер запущен")
    
    yield driver
    
    driver.quit()
    logger.info("Браузер закрыт")

@pytest.fixture
def registered_user(driver):
    """Фикстура для создания зарегистрированного пользователя"""
    email = generate_email()
    password = generate_password()
    name = generate_name()
    
    logger.info(f"Регистрация пользователя: {email}")
    driver.get("https://stellarburgers.education-services.ru/register")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(AuthPageLocators.NAME_INPUT)
    )
    
    driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )
    
    logger.info(f"Пользователь {email} успешно зарегистрирован")
    return {"email": email, "password": password, "name": name}

@pytest.fixture
def login_user(driver, registered_user):
    """Фикстура для входа зарегистрированного пользователя"""
    logger.info(f"Вход пользователя: {registered_user['email']}")
    driver.get("https://stellarburgers.education-services.ru/login")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(AuthPageLocators.EMAIL_INPUT)
    )
    
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
    
    logger.info(f"Пользователь {registered_user['email']} успешно вошел в систему")
    return registered_user