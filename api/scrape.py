from PIL import Image
from selenium import webdriver
import time
import string
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



PATH='chromedriver'

def clean (text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ') # Remove Punctuation
        lowercased = text.lower() # Lower Case
        lowercased=lowercased.replace('\n','')
    return lowercased


# only usefull for the dual-boot model
def get_photo_text(url, webdriver=False):
    if webdriver ==True:
        driver=webdriver.Chrome(PATH)
        driver.get(url)
        driver.save_screenshot(f'photo/{url}.png')

        text = driver.find_elements( by = "tag name", value = "body")
        time.sleep(2)
        final1 = text[0].get_attribute("innerText")
        final_text=clean(final1)
        image=Image.open('photo/{url}.png')
    elif webdriver == False :
        options = Options()
        options.headless = True
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(url)
        driver.save_screenshot(f'photo/{url}.png')

        text = driver.find_elements( by = "tag name", value = "body")
        time.sleep(2)
        final1 = text[0].get_attribute("innerText")
        final_text=clean(final1)
        image=Image.open('photo/{url}.png')

    return final_text , image

#use for the nlp
def scrape_text(url):

    # Initialise webdriver
    options = Options()
    options.headless = True
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    # scrape text
    scraped_text = driver.find_elements(by = "tag name", value = "body")
    scraped_text = scraped_text[0].get_attribute("innerText")
    scraped_text = clean(scraped_text)

    return scraped_text
