from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get('https://www.bestfightodds.com/events/ufc-200-tate-vs-nunes-1102')
driver.implicitly_wait(2)
fight_table = driver.find_element(By.XPATH,'//*[@id="event1102"]/div[2]/div[3]/table/tbody')
fight_table = fight_table.find_elements(By.XPATH, "*")

fight_matchup = []

save_to_last_element = False
for element in fight_table:
    print("Getting Element")
    saved_element = element.find_element(By.XPATH, "*")
    print(saved_element.get_attribute("class"))
    if save_to_last_element == True:
        if(saved_element.get_attribute("class") != 'pr'):
            fight_matchup[-1].append(saved_element.text)
    else:
        if(saved_element.get_attribute("class") != 'pr'):
            fight_matchup.append([saved_element.text])

json.dump(fight_matchup, open('fight_matchup.json', 'w'))
driver.quit()
