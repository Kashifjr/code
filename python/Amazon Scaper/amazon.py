import requests
import os
import webbrowser
#import stmplib #enables to send emails
from bs4 import BeautifulSoup

# This program takes an amazon link and prints you the name of the item with its 
# current price.
# 
# 
# ===== Features to Add ====
# *Add ability to store this information into a file(json). Excel sheet and other data 
# structures.
# *[x]Enter a search and return for the 1st result from the amazon site itself. 
# 

# Debug Amazon link
# debug_link1 = 'https://www.amazon.com/Zeee-Batteries-Connector-Helicopter-Quadcopter/dp/B0972RKJDS/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.5hKdpgWW2pJIzFBYoEmgISa8YfivcQIkJiiYH7x2uDDVHLid7O8FMbysu-IiGrTV9hhRztodkGYm1v_c0SOzA7sBpslljoajW1kCj6avS_PDuNKYYzuJpKRyp4mPv0USdpLwJTpxNjcMO9gtva-c87XNwc4VDWOStPAnDmwZX23MhzEFXPQhh_fY6AiIyXZ52Zeqn_nuGLBpAmiUckFK2n0x80Z715O2l6dRF8lLfshUfvs0z8KWsREoD_7WpLEC7UOd5UkGRmehhRPqj68_d3R9ptdWKicIisOgPpxyFQA.zND7HOSj5xD-rF-xX42SjraeFo7oWVYG6zbs4B1enRM&dib_tag=se&keywords=3s+lipo+battery&qid=1727061514&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

# google 'my user agent'
# the 'accept-language' will prevent Amazon from blocking this request
# b/c they block when detecting a bot
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'accept-language': 'en-US,en;q=0.9',
}

line1 = "============================"
line2 = "----------------------------"

def create_menu():
    print(line1+"""
URL Search.........1
Product Search.....2
Close Program....'q'
"""+line1)

def check_price(url):
    page = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    whole = soup.find(attrs="a-price-whole").get_text()
    decimal = soup.find(attrs="a-price-fraction").get_text()
    price = whole + decimal
    # format item name and cost
    string1 = "\nThe item is: "
    string2 = "The current price is: "
    print(string1 + title+"\n"+ string2 +price + "\17:30n")

# Function to get the first search result URL
def get_first_amazon_result(query):
    search_url = f"https://www.amazon.com/s?k={query}"
    response = requests.get(search_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    first_result = soup.find("a", class_="a-link-normal s-no-outline")
    # print(first_result)
    if first_result:
        return "https://amazon.com"+first_result["href"]
    return None

# Implementation to send an email when the prices is below a set threshold
def send_mail():
    server = stmplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()#establishes connection 
    server.starttls()#encrypts connection
    server.ehlo()

    server.login('ENTER THE USER', 'ENTER THE PASSWORD')

    subject = "Lipo 3d Batteries are is lower!"
    body = "chek teh link boii!!! https://www.amazon.com/Zeee-Batteries-Connector-Helicopter-Quadcopter/dp/B0972RKJDS/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.5hKdpgWW2pJIzFBYoEmgISa8YfivcQIkJiiYH7x2uDDVHLid7O8FMbysu-IiGrTV9hhRztodkGYm1v_c0SOzA7sBpslljoajW1kCj6avS_PDuNKYYzuJpKRyp4mPv0USdpLwJTpxNjcMO9gtva-c87XNwc4VDWOStPAnDmwZX23MhzEFXPQhh_fY6AiIyXZ52Zeqn_nuGLBpAmiUckFK2n0x80Z715O2l6dRF8lLfshUfvs0z8KWsREoD_7WpLEC7UOd5UkGRmehhRPqj68_d3R9ptdWKicIisOgPpxyFQA.zND7HOSj5xD-rF-xX42SjraeFo7oWVYG6zbs4B1enRM&dib_tag=se&keywords=3s+lipo+battery&qid=1727061514&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'frommal',
        'to',
        msg
    )

    print("EMAIL SENT")

    server.quit()

def main():
    while True:
        create_menu()
        user_option = input("Choose an option: ")
        # Enter amazon URL  
        if user_option == "1":
            user_url = input("\nEnter the URL of the Amazon the item you'd like to scrape: \n")
            amazon_url = "www.amazon.com"
            if amazon_url in user_url:
                check_price(user_url)
            else:
                print("you must enter a existing product from the Amazon website\n")

        # search amazon for productuserOption
        elif user_option == "2":
            query = input("what are you looking for?\n")

            # Open the first search result in the web browser
            print("\nsearching...\n")

            first_result_url = get_first_amazon_result(query)

            check_price(first_result_url)

        # close program
        elif user_option == "q":
            os.system('cls||clear')
            print("closing program...")
            break
          
# Call main function
main()