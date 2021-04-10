#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

st = "Short"
# Step 1. Añadir Google Chrome como buscador
browser = webdriver.Chrome(executable_path="./drivers/chromedriver")

# Step 2. Abrir la siguiente web en Chrome
browser.get('http://automationpractice.com/index.php')
assert browser.title == "My Store"

# Step 3. Buscar la barra de busqueda y escribir "Short" para hacer la busqueda
search_query = browser.find_element_by_id("search_query_top")
search_query.send_keys(st)

# Step 4. Buscar el boton des busqueda y darle click
button = browser.find_element_by_name("submit_search")
button.click()
    
browser.quit()
