import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators
from generators import generate_email, generate_password, generate_name, generate_invalid_password
import logging

logger = logging.getLogger(__name__)

class TestRegistration:
    
    def test_successful_registration(self, driver):
        """Тест успешной регистрации"""
        email = generate_email()
        password = generate_password()
        name = generate_name()
        
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
        
        assert driver.find_element(*AuthPageLocators.LOGIN_BUTTON).is_displayed()
        logger.info(f"Тест успешной регистрации пройден для {email}")
    
    def test_registration_with_invalid_password(self, driver):
        """Тест регистрации с некорректным паролем"""
        email = generate_email()
        invalid_password = generate_invalid_password()
        name = generate_name()
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.NAME_INPUT)
        )
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.PASSWORD_ERROR)
        )
        
        assert error_message.is_displayed()
        assert "Некорректный пароль" in error_message.text
        logger.info("Тест регистрации с некорректным паролем пройден")
    
    def test_registration_with_empty_name(self, driver):
        """Тест регистрации с пустым именем"""
        email = generate_email()
        password = generate_password()
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.NAME_INPUT)
        )
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys("")
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        assert "register" in driver.current_url
        logger.info("Тест регистрации с пустым именем пройден")