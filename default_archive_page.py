from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get('https://www.bestfightodds.com/archive')
driver.implicitly_wait(2)

# [find\_element(By.XPATH) driver method - Selenium Python - GeeksforGeeks](https://www.geeksforgeeks.org/find_element_by_xpath-driver-method-selenium-python/#)
table_element = driver.find_element(By.XPATH,'//*[@id="page-content"]/table')

# [python - Get all child elements - Stack Overflow](https://stackoverflow.com/questions/24795198/get-all-child-elements)
table_elements = table_element.find_element(By.XPATH, "*")
table_elements = table_elements.find_elements(By.XPATH, "*")

events = []
for table_row in table_elements:
    table_row_elements = table_row.find_elements(By.XPATH, "*")
    a_tag = table_row_elements[1].find_element(By.XPATH, "*")
    event_dict = {
        "event_date" : table_row_elements[0].text,
        "event_name" : table_row_elements[1].text,
        "event_link" : a_tag.get_attribute('href')
    }
    print(event_dict)
    events.append(event_dict)

json.dump(events, open('bestfightodds_events.json', 'w'))
driver.quit()
