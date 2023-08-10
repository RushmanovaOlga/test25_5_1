import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()


def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('hea007@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('456111')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(1)

# Присутствуют все питомцы
def test_stat(driver):
    driver.find_element(By.ID, 'email').send_keys('hea007@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('456111')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Список всех питомцев на странице
    all_my_pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')
    # Количество питомцев взято из статистики пользователя
    stat = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.task3.fill .left'))).text
    num = int(stat.split('\n')[1].split(' ')[1])

    assert len(all_my_pets) == num


