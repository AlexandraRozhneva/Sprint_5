import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, AccountPageLocators
import logging

logger = logging.getLogger(__name__)

class TestAccount:
    
    def test_go_to_personal_account(self, driver, login_user):
        """Тест перехода в личный кабинет"""
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        
        assert "account" in driver.current_url
        logger.info("Тест перехода в личный кабинет пройден")
    
    def test_go_from_account_to_constructor(self, driver, login_user):
        """Тест перехода из личного кабинета в конструктор по кнопке 'Конструктор'"""
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert "account" not in driver.current_url
        logger.info("Тест перехода из кабинета в конструктор пройден")
    
    def test_go_from_account_to_main_via_logo(self, driver, login_user):
        """Тест перехода из личного кабинета на главную по клику на логотип"""
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert "account" not in driver.current_url
        logger.info("Тест перехода по логотипу пройден")
    
    def test_logout_from_account(self, driver, login_user):
        """Тест выхода из аккаунта"""
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.LOGIN_BUTTON)
        )
        
        assert "login" in driver.current_url
        logger.info("Тест выхода из аккаунта пройден")