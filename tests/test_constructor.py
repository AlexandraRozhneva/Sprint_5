import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from helpers import wait_and_click, get_active_tab_text
import logging

logger = logging.getLogger(__name__)

class TestConstructor:
    
    def test_switch_to_buns_section(self, driver):
        """Тест перехода к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ожидаем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        
        # Кликаем по разделу "Булки"
        wait_and_click(driver, MainPageLocators.BUNS_SECTION)
        
        # Проверяем, что активный таб - "Булки"
        active_tab_text = get_active_tab_text(driver)
        assert active_tab_text == "Булки", f"Активный таб '{active_tab_text}', ожидался 'Булки'"
        
        # Дополнительная проверка: наличие класса активного таба
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "tab_tab_type_current__2BEPc" in active_tab.get_attribute("class")
        
        logger.info("Тест перехода к разделу 'Булки' пройден")
    
    def test_switch_to_sauces_section(self, driver):
        """Тест перехода к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        
        wait_and_click(driver, MainPageLocators.SAUCES_SECTION)
        
        active_tab_text = get_active_tab_text(driver)
        assert active_tab_text == "Соусы", f"Активный таб '{active_tab_text}', ожидался 'Соусы'"
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "tab_tab_type_current__2BEPc" in active_tab.get_attribute("class")
        
        logger.info("Тест перехода к разделу 'Соусы' пройден")
    
    def test_switch_to_fillings_section(self, driver):
        """Тест перехода к разделу 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        
        wait_and_click(driver, MainPageLocators.FILLINGS_SECTION)
        
        active_tab_text = get_active_tab_text(driver)
        assert active_tab_text == "Начинки", f"Активный таб '{active_tab_text}', ожидался 'Начинки'"
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "tab_tab_type_current__2BEPc" in active_tab.get_attribute("class")
        
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
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(section_locator)
            )
            assert element.is_displayed(), f"Элемент {section_name} не отображается"
            logger.info(f"Раздел {section_name} кликабелен")
        
        logger.info("Тест кликабельности всех разделов пройден")