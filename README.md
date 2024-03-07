# Web-Scraper
 A web scraper using Python and Selenium for scraping data from e-commerce websites like Amazon and converting it to Excel.

The code prompts the user to input a search term for Amazon.in, then initializes the Chrome WebDriver to navigate to the website. Upon entering the search term and submitting the query, it waits for the search results page to load and extracts essential information about each product, including name, price, ASIN, and whether it's sponsored. This data is stored in a pandas DataFrame and exported to an Excel file named "products.xlsx". The script streamlines the process of gathering product details from Amazon search results, enabling efficient analysis and reference.

The code utilizes several tools and libraries to automate the process of retrieving product information:
1. Selenium
2. Chrome WebDriver
3. ChromeDriverManager
4. Pandas
