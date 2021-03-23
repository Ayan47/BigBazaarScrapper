
# BIG BAZAAR SCRAPPER
-----------------
# Cloning the Project
```sh
git clone git@github.com:Ayan47/BigBazaarScrapper.git
```
# Prerequisites 

The `BigBazaarScrapper` has the following prerequisites: 

 - **Python 3.7 or newer versions**
 - **Python Library - BeautifulSoup**
 - **Python Library - Selemium**
 - **Chromedriver.exe**


The BigBazaarscrapper has been tested on `Windows 10` Build Version `19042.867`

# Steps to Run the BigBazaarScrapper 

 - Install `Python 3.7` or newer versions
 - Install the following Python Libraries- `BeautifulSoup`, `Selenium` (`Json` and `Time` too if not already present)
 - We are using `Google Chrome` as the Browser to scrape data which
   is running in Windows, therefore,Download `Chromedriver.exe`
 - Put the location of your Chromedriver.exe in the "`driver`" variable in
   `line 6`. 
      ```yaml
   driver = webdriver.Chrome(executable_path  =  r"*Your\*Path\*Here\chromedriver.exe")
   
 - Run the Code
## NOTE
As of `24-03-2021` Everything works fine.
For seperate `Categories` mentioned seperate `JSON files` shall form.
