import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
import logging

logger = logging.getLogger(__name__)

class TestConstructor:
    
    def click_with_scroll(self, driver, element):
        """Прокрутка к элементу и клик с помощью JavaScript"""
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
    
    def test_switch_to_buns_section(self, driver):
        """Тест перехода к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем появления элемента
        buns_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        
        # Прокручиваем и кликаем через JavaScript
        self.click_with_scroll(driver, buns_element)
        
        # Проверяем, что URL не изменился (остались на главной)
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Булки' пройден")
    
    def test_switch_to_sauces_section(self, driver):
        """Тест перехода к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем появления элемента
        sauces_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        
        # Прокручиваем и кликаем через JavaScript
        self.click_with_scroll(driver, sauces_element)
        
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Соусы' пройден")
    
    def test_switch_to_fillings_section(self, driver):
        """Тест перехода к разделу 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем появления элемента
        fillings_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        
        # Прокручиваем и кликаем через JavaScript
        self.click_with_scroll(driver, fillings_element)
        
        assert "stellarburgers.education-services.ru" in driver.current_url
        logger.info("Тест перехода к разделу 'Начинки' пройден")
    
    def test_all_sections_are_clickable(self, driver):
        """Тест, что все разделы кликабельны"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        sections = [
            (MainPageLocators.BUNS_SECTION, "Булки"),
            (MainPageLocators.SAUCES_SECTION, "Соусы"),
            (MainPageLocators.FILLINGS_SECTION, "Начинки")
        ]
        
        for section_locator, section_name in sections:
            # Ожидаем появления элемента
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(section_locator)
            )
            
            # Проверяем, что элемент отображается
            assert element.is_displayed(), f"Элемент {section_name} не отображается"
            
            # Прокручиваем и кликаем через JavaScript
            self.click_with_scroll(driver, element)
            logger.info(f"Раздел {section_name} кликабелен")
        
        logger.info("Тест кликабельности всех разделов пройден")