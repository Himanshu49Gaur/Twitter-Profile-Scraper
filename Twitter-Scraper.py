import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run browser in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to scrape Twitter profile details
def scrape_twitter_profile(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    try:
        bio = driver.find_element(By.XPATH, '//div[@data-testid="UserDescription"]').text
    except:
        bio = "N/A"

    try:
        following = driver.find_element(By.XPATH, '//a[contains(@href, "/following")]/span[1]/span').text
    except:
        following = "0"

    try:
        followers = driver.find_element(By.XPATH, '//a[contains(@href, "/followers")]/span[1]/span').text
    except:
        followers = "0"

    try:
        location = driver.find_element(By.XPATH, '//span[@data-testid="UserLocation"]').text
    except:
        location = "N/A"

    try:
        website = driver.find_element(By.XPATH, '//a[@data-testid="UserUrl"]').get_attribute('href')
    except:
        website = "N/A"

    return {
        "Bio": bio,
        "Following Count": following,
        "Followers Count": followers,
        "Location": location,
        "Website": website
    }

# Read Twitter profile URLs from a CSV file without headers
input_csv = r'E:\\Intern\\Scripting\\twitter_links.csv'  # Corrected the path

try:
    profiles_df = pd.read_csv(input_csv, header=None)  # No header in CSV
except Exception as e:
    print(f"Error reading CSV file: {e}")
    driver.quit()
    exit()

# Check if the CSV is empty
if profiles_df.empty:
    print("The CSV file is empty. Please check the file content.")
    driver.quit()
    exit()

# Loop through the first column containing URLs
results = []
for index, row in profiles_df.iterrows():
    url = row[0]  # Access the URL directly
    if pd.notnull(url):  # Skip empty rows
        print(f"Scraping {url}...")
        try:
            data = scrape_twitter_profile(url)
            results.append(data)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

# Save the scraped data to a new CSV file
output_df = pd.DataFrame(results)
output_df.to_csv('twitter_profiles_scraped.csv', index=False)

# Close the browser
driver.quit()
