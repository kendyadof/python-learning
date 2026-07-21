 # type: ignore 
# só pq tava dando problema de tipagem no luiz otavio

# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chrome-win64" / "chromedriver.exe"
#  Arquivo de log para consultar erros
LOG = ROOT_FOLDER / "chromedriver.log"

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option) 

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser



if __name__ == '__main__':
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless") # nao mostrar o navegador em si
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument(r'--user-data-dir=C:\Temp\selenium_profile')

    # chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC), log_path=str(LOG))
    # chrome_browser = webdriver.Chrome(
    #     service=chrome_service,  options=chrome_options,
    # )

    WAIT = 10
    options = ("--no-sandbox","--disable-gpu")
    browser = make_chrome_browser(*options)

    try: # try sugerido por duck ai
        browser.set_page_load_timeout(60)
        # browser.get("https://www.google.com/") # google está me dando captcha
        browser.get("https://www.duckduckgo.com/")

        # elementos: class pode retornar mais de um. Recomendável utilizar name ou id
        search_input = WebDriverWait(browser, WAIT).until(
            EC.presence_of_element_located(
                (By.NAME, "q")
            )
        )
        
        search_input.send_keys("sua mãe banda")
        search_input.send_keys(Keys.ENTER)

        # google
        # results = browser.find_element(By.ID, "search")
        # links = results.find_elements(By.TAG_NAME, "a")
        # link = links[0]
        # link.click()

        container_result = WebDriverWait(browser, WAIT).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "react-results--main")
            )
        )

        lista_result = container_result.find_element(By.CLASS_NAME, "wLL07_0Xnd1QZpzpfR4W")
        primeiro_result = lista_result[.find_element(By.ID,"r1-0")]
        primeiro_result.click()

        # # ou seria
        # lista_result = container_result.find_elements(By.CLASS_NAME, "wLL07_0Xnd1QZpzpfR4W")
        # primeiro_result = lista_result[0]
        # primeiro_result.click()
        

        # ent vai DORME
        sleep(WAIT)
        


    finally:
        browser.quit()