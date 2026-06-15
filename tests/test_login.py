import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
import logging

logger = logging.getLogger(__name__)

class TestLogin:
    
    def test_login_via_main_button(self, driver, registered_user):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN)
        )
        
        # Клик по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
        ).click()
        
        # Ожидаем появления формы входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.EMAIL_INPUT)
        )
        
        # Вводим данные
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        logger.info("Тест входа через главную кнопку пройден")
    
    def test_login_via_personal_account_button(self, driver, registered_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        
        # Клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ожидаем появления формы входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.EMAIL_INPUT)
        )
        
        # Вводим данные
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        logger.info("Тест входа через личный кабинет пройден")
    
    def test_login_via_register_form(self, driver, registered_user):
        """Тест входа через кнопку в форме регистрации"""
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.REGISTER_BUTTON)
        )
        
        # Клик по ссылке "Войти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)
        ).click()
        
        # Ожидаем появления формы входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.EMAIL_INPUT)
        )
        
        # Вводим данные
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        logger.info("Тест входа через форму регистрации пройден")
    
    def test_login_via_password_recovery_form(self, driver, registered_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        # Ожидаем загрузки страницы восстановления пароля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.LOGIN_LINK)
        )
        
        # Клик по ссылке "Войти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)
        ).click()
        
        # Ожидаем появления формы входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.EMAIL_INPUT)
        )
        
        # Вводим данные
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        logger.info("Тест входа через форму восстановления пароля пройден")