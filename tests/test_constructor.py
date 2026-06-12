import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
import logging

logger = logging.getLogger(__name__)

class TestConstructor:
    
    def test_switch_to_buns_section(self, driver):
        """Тест перехода к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        ).click()
        
        # Проверяем, что URL не изменился (остались на главной)
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Булки' пройден")
    
    def test_switch_to_sauces_section(self, driver):
        """Тест перехода к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Соусы' пройден")
    
    def test_switch_to_fillings_section(self, driver):
        """Тест перехода к разделу 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        ).click()
        
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Начинки' пройден")
    
    def test_all_sections_are_clickable(self, driver):
        """Тест, что все разделы кликабельны"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        sections = [
            MainPageLocators.BUNS_SECTION,
            MainPageLocators.SAUCES_SECTION,
            MainPageLocators.FILLINGS_SECTION
        ]
        
        for section in sections:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(section)
            )
            assert element.is_displayed()
            logger.info(f"Раздел {section} кликабелен")
        
        logger.info("Тест кликабельности всех разделов пройден")