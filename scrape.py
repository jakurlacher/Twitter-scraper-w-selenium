import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Open webbrowser, login
driver = Chrome()
try:
    driver.get('https://www.twitter.com/login')
#driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-519080295%3A1671740754861718&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=en&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh6yMBUIwgW8ohuToCJAgfAO_wnQOfAbVzVlwSgZ4-6sFLILMpGOHkzrH6oAy-1L0yhlpjmArQ')
except:
    print("Could not access twitter login page")
    quit()
sleep(7)
#ENTER YOUR OWN USERNAME AND PASSWORD
my_username = "jak_urlacher"
my_password = " "

try:
    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys(my_username)
except:
    print("Twitter took too long to load")
    quit()

next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
next_button.click()
sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(my_password)
log_in = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
log_in.click()
sleep(5)

user = 'obama'
#Navigate to user's page

search_box = driver.find_element(By.XPATH, "//input[@data-testid= 'SearchBox_Search_Input']")
search_box.send_keys(user)
search_box.send_keys(Keys.RETURN)
sleep(5)
people = driver.find_element(By.XPATH, "//span[contains(text(), 'People')]")
people.click()
sleep(5)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span")
profile.click()
sleep(5)
Tweets =[]
articles = driver.find_elements(By.XPATH, "//article[@data-testid= 'tweet']")

#scrape tweets and manually scroll to end of page
while True:
    for article in articles:
        try:
            tweet = article.find_element(By.XPATH, ".//div[@data-testid= 'tweetText']").text
            print(tweet)
            Tweets.append(tweet)
        except:
            #Prevent the program from blowing up if there's a video
            continue



    sleep(4)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    articles = driver.find_elements(By.XPATH, "//article[@data-testid= 'tweet']")
    Tweets2 = list(set(Tweets))
    #stop at 100 tweets
    if len(Tweets2) > 84:
        break
    print(len(Tweets2))

print(Tweets2)
driver.close()

lst = list()

for tweets in Tweets2:
    words = tweets.split()
    lst.append(words)
file = 'obamatweets.txt'
with open(file, 'w') as f:
  # Write each element of the list to the file
  f.write(str(lst))
