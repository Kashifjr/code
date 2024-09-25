import requests
#import stmplib #enables to send emails
from bs4 import BeautifulSoup

# Debug Amazon link
amazon = 'https://www.amazon.com/Zeee-Batteries-Connector-Helicopter-Quadcopter/dp/B0972RKJDS/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.5hKdpgWW2pJIzFBYoEmgISa8YfivcQIkJiiYH7x2uDDVHLid7O8FMbysu-IiGrTV9hhRztodkGYm1v_c0SOzA7sBpslljoajW1kCj6avS_PDuNKYYzuJpKRyp4mPv0USdpLwJTpxNjcMO9gtva-c87XNwc4VDWOStPAnDmwZX23MhzEFXPQhh_fY6AiIyXZ52Zeqn_nuGLBpAmiUckFK2n0x80Z715O2l6dRF8lLfshUfvs0z8KWsREoD_7WpLEC7UOd5UkGRmehhRPqj68_d3R9ptdWKicIisOgPpxyFQA.zND7HOSj5xD-rF-xX42SjraeFo7oWVYG6zbs4B1enRM&dib_tag=se&keywords=3s+lipo+battery&qid=1727061514&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

# google 'my user agent'
# the 'accept-language' will prevent Amazon from blocking this request
# b/c they block when detecting a bot
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'accept-language': 'en-US,en;q=0.9',
}

def checkPrice(url):
# def checkPrice():

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    whole = soup.find(attrs="a-price-whole").get_text()
    decimal = soup.find(attrs="a-price-fraction").get_text()
    price = whole + decimal
    # format item name and cost
    string1 = "The item is: "
    string2 = "The current price is: "
    print(string1 + title+"\n"+ string2 +price + "\n")

def main():
    URL = input("Enter the URL of the Amazon the item you'd like to scrape: \n")
    checkPrice(URL)
    
# Call main Method
main()


# Implementation to send an email when the prices is below a set threshold
def sendMail():
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