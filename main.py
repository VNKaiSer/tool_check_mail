from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import random
from selenium.webdriver.common.keys import Keys

CHECK_RECOVERY_EMAIL_XPATH = '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/section/div/div/div/ul/li[3]/div'
RECOVER_MAIL_ERROR_XPATH = '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[3]/div/div/div/div[1]/div/div[2]/div[2]/div'
email = "lo235536@gmail.com"
password = "teaxa1T@16"
recovery_email = "ryan.t.lore23@gmail.com"
def random_time():
    return random.randint(1, 2)

def random_time_input():
    return random.uniform(0.05, 0.1)

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_password(password):
    return len(password) >= 6

def validate_input(input_string):
    parts = input_string.split('|')
    if len(parts) != 3:
        return "Đầu vào không đúng định dạng (cần 3 phần tách bởi '|')."
    
    email, password, recovery_email = parts
    if not validate_email(email):
        return f"Email không đúng định dạng: {email}"
    if not validate_password(password):
        return f"Mật khẩu không hợp lệ (phải dài ít nhất 6 ký tự): {password}"
    if not validate_email(recovery_email):
        return f"Email khôi phục không đúng định dạng: {recovery_email}"
    
    return email, password, recovery_email 

# Ví dụ kiểm tradat
# input_string = "allaniziyaya@gmail.com|S.B901.12hasn8276|ryan.t.lore23@gmail.com"
# result = validate_input(input_string)
# print(result)

def start_task(): 
    # Cấu hình Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-infobars")
    
    # Khởi chạy trình duyệt với proxy
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://accounts.google.com/signin")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'identifierId')))
    email_input = driver.find_element(By.ID, 'identifierId')
    time.sleep(random_time())
    email_input.send_keys(email)
    
    email_input.send_keys(Keys.ENTER)
    time.sleep(random_time())
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'Passwd')))
    password_input = driver.find_element(By.NAME, 'Passwd')
    time.sleep(random_time())
    password_input.send_keys(password)
    
    password_input.send_keys(Keys.ENTER)
    
    # Kiểm tra trường hợp nhập email khôi phục
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, CHECK_RECOVERY_EMAIL_XPATH)))
        recovery_email_button = driver.find_element(By.XPATH, CHECK_RECOVERY_EMAIL_XPATH)
        recovery_email_button.click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'knowledgePreregisteredEmailResponse')))
        recovery_email_input = driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse')
        time.sleep(random_time())
        recovery_email_input.send_keys(recovery_email)
        
        recovery_email_input.send_keys(Keys.ENTER)
        # Kiểm tra email có sai không 
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, RECOVER_MAIL_ERROR_XPATH)))
            error_element = driver.find_element(By.XPATH, RECOVER_MAIL_ERROR_XPATH)
            error_text = error_element.text
            print(error_text)
        except:
            print()
    except:
        print()
        
    

    input("Enter to close:")
    driver.quit()
start_task()
