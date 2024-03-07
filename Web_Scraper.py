from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

#Search
search_item = input("Enter the search term for Amazon.in: ")


# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Initialize WebDriver with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# Initialize WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Amazon
driver.get("https://www.amazon.in")

# Find search input field and search for the item
# search_item = "headset"
search_input = driver.find_element(By.ID, "twotabsearchtextbox")
search_input.send_keys(search_item)
search_input.send_keys(Keys.RETURN)

# Wait for products to load
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']")))

# Extract product names
products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
extracted_data = []

for product in products:
    product_info = {}
    try:
        product_name = product.find_element(By.CSS_SELECTOR, "h2 span").text
        product_price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        asin = product.get_attribute("data-asin")
        # sponsored_order = product.get_attribute("data-sponsored-position")
        sponsored_element = product.find_element(By.CSS_SELECTOR, ".a-color-secondary")
        if sponsored_element.text == "Sponsored":
            sponsored_order = "Sponsored"
        else:
            sponsored_order = "Not sponsored"
        product_info["Product Name"] = product_name
        product_info["Price"] = product_price
        product_info["ASIN"] = asin
        product_info["Sponsored listing order"] = sponsored_order
        
        extracted_data.append(product_info)
    except NoSuchElementException:
        print("Product name not found for one of the products.")
    except Exception as e:
        print(f"Error extracting product info: {e}")

# Quit the WebDriver
driver.quit()

#Convert Json to Datafram
df = pd.DataFrame(extracted_data)
# Specify the file path for the Excel file
excel_file = "product.xlsx"

# Export the DataFrame to Excel
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created successfully.")
