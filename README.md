# Twitter-Profile-Scraper
This Python script scrapes Twitter profiles for Bio, Following Count, Followers Count, Location, and Website using Selenium. The extracted data is saved to a CSV file for analysis.

🚀 Features
✔️ Headless browser for efficiency
✔️ Error handling for missing fields
✔️ Reads profile URLs from a CSV file
✔️ Saves extracted data to a new CSV file
✔️ Uses Selenium WebDriver for automation

🛠 Requirements
Make sure you have Python 3.8+ installed. Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install the required libraries:

bash
Copy
Edit
pip install selenium pandas webdriver-manager
📂 File Structure
bash
Copy
Edit
📦 Twitter-Scraper
 ┣ 📜 twitter_scraper.py   # Main script
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 twitter_links.csv     # Input file (list of Twitter profile URLs)
 ┗ 📜 README.md             # Documentation
🔧 Setup & Usage
1️⃣ Prepare CSV File
Place a CSV file (twitter_links.csv) in the project directory, containing one Twitter profile URL per line (without headers):

arduino
Copy
Edit
https://twitter.com/user1
https://twitter.com/user2
https://twitter.com/user3
2️⃣ Run the Script
Execute the script:

bash
Copy
Edit
python twitter_scraper.py
The extracted profile data will be saved as twitter_profiles_scraped.csv in the same directory.

🛠 Configuration
Modify input file path in the script:
python
Copy
Edit
input_csv = r'Link to File'
Adjust sleep time (time.sleep(3)) based on network speed for smoother scraping.
Enable GUI mode by removing options.add_argument('--headless').
⚠️ Important Notes
Twitter may block frequent requests—use proxies or delays to prevent bans.
Selenium requires a compatible Chrome browser—ensure it’s up to date.
Twitter’s HTML structure may change, breaking XPaths. Update selectors if needed.
📜 License
This project is open-source under the MIT License. Feel free to modify and use it as needed.
