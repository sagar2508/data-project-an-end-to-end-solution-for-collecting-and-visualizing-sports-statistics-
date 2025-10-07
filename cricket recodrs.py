from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
ser = Service(r"C:\Users\vedpa\Desktop\selenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = ser)
driver.get("https://www.espncricinfo.com/records")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
batting_record = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[4]/div/div[3]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a/span')))
batting_record.click()
time.sleep(3)
most_run = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main-container"]/div[4]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div/ul/li[1]/a/span/div')))
most_run.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.ds-table")))
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
file_path = os.path.join(os.getcwd(), "test_cricket_records.txt")
with open(file_path, "w", encoding="utf-8") as f:
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        if data:  # avoid empty rows
            f.write(" | ".join(data) + "\n")
driver.quit()
import pandas as pd
file_path = os.path.join(os.getcwd(), "test_cricket_records.txt")
excel_file = os.path.join(os.getcwd(), "test_cricket_records.xlsx")
columns = ["Player", "Span", "Matches", "Innings", "NotOuts", "Runs", "HighestScore",
    "Average", "BallsFaced", "StrikeRate", "100s", "50s", "0s", "4s", "6s"
]
df = pd.read_csv(file_path, sep="\\|", engine="python", header=None)
df.columns = columns[:len(df.columns)]
df.to_excel(excel_file, index=False)

