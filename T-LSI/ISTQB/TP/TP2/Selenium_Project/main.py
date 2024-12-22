from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_google():
    # Instanciation du service Chrome
    driver_service = Service("C:\\Drivers\\chromedriver.exe")  # Chemin vers votre ChromeDriver
    driver = webdriver.Chrome(service=driver_service)
    
    # Test : ouverture de Google
    driver.get("https://www.google.com")
    print("Test réussi : Google est ouvert !")
    driver.quit()

def test_facebook_login():
    # Initialize Chrome browser
    browser = webdriver.Chrome()
    
    try:
        # Navigate to Facebook
        browser.get("http://www.facebook.com")
        
        # Find login elements
        username = browser.find_element(By.ID, "email")
        password = browser.find_element(By.ID, "pass")
        submit = browser.find_element(By.NAME, "login")
        
        # Enter credentials (replace with your test account credentials)
        username.send_keys("YOUR_TEST_EMAIL")
        password.send_keys("YOUR_TEST_PASSWORD")
        
        # Click login button
        submit.click()
        
        # Wait for page load
        wait = WebDriverWait(browser, 5)
        
        # Get current URL for verification
        current_url = browser.current_url
        print("The current url is:", current_url)
        
        # Verify login success (URL should not contain 'login' after successful login)
        assert 'login' not in current_url.lower(), "Login failed"
        print("Login test passed")
        
    except Exception as e:
        print("Test failed:", str(e))
    
    finally:
        browser.quit()
        print("Test finished")


def test_isims_login():
    # Initialize Chrome browser
    browser = webdriver.Chrome()
    # wait = WebDriverWait(browser, 10)
    
    try:
        # Navigate to Google.tn
        browser.get("https://www.google.tn")
        
        # Find and fill the search box
        search_box = browser.find_element(By.NAME, "q")
        search_box.send_keys("isims")
        search_box.submit()
        
        # Find and click on the ISIMS website link
        isims_link = browser.find_element(By.PARTIAL_LINK_TEXT, "ISIMS")
        isims_link.click()
        
        # Wait for page to load and find the "L'Institut" menu
        institut_menu = browser.find_element(By.LINK_TEXT, "L'Institut")
        institut_menu.click()

        # Find and click on "En chiffre"
        en_chiffre = browser.find_element(By.LINK_TEXT, "En chiffre")
        en_chiffre.click()
        
        # Verify the text content
        text_element = browser.find_element(By.XPATH, "//*[contains(text(), 'En chiffre')]")
        assert "En chiffre" in text_element.text, "Text 'En chiffre' not found on the page"
        print("Test passed: 'En chiffre' text found on the page")
        
    except Exception as e:
        print("Test failed:", str(e))
    
    finally:
        browser.quit()
        print("Test finished")
if __name__ == "__main__":
    # Uncomment the test you want to run
    # test_google()
    # test_facebook_login()  # Remember to add your test credentials before running
    test_isims_login()