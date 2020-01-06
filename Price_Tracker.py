import requests
from bs4 import BeautifulSoup
import smtplib
import time



def Check_Price():
    # The url of the product page in amazon whose price is to be tracked
    #could be any other website or product
    url="https://www.amazon.in/House-Tara-Laptop-Messenger-Combat/dp/B07FYP3TMS?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_Cj0KCQjwkK_qBRD8ARIsAOteukBD7IY_rEUXJIadgZ80m3cVZcdT46nenTt2KbnFAgl08hNZLLpr6VQaAoDwEALw_wcB_k_&gclid=Cj0KCQjwkK_qBRD8ARIsAOteukBD7IY_rEUXJIadgZ80m3cVZcdT46nenTt2KbnFAgl08hNZLLpr6VQaAoDwEALw_wcB"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    # Scraping data from the above url
    page=requests.get(url, headers=headers)
    soup=BeautifulSoup(page.content,"html.parser")
    price=soup.find(id="priceblock_saleprice").get_text() # Here id is the id tag of the price extracted from the script of the product page
    price=price.replace(',','.')
    Converetd_Price=float(price[2:7])
    print(Converetd_Price)
    # If price falls under the desired range,send the email
    if(Converetd_Price<1.8):
        Send_Mail()
        
        
def Send_Mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("xyz@gmail.com","The one time google app password for authentication") #parameters are senders email and the corresponding one time gmail passcode(refer to readme file for more info)
    subject="Price fell down!!"
    body="Check the Amazon link: https://www.amazon.in/House-Tara-Laptop-Messenger-Combat/dp/B07FYP3TMS?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_Cj0KCQjwkK_qBRD8ARIsAOteukBD7IY_rEUXJIadgZ80m3cVZcdT46nenTt2KbnFAgl08hNZLLpr6VQaAoDwEALw_wcB_k_&gclid=Cj0KCQjwkK_qBRD8ARIsAOteukBD7IY_rEUXJIadgZ80m3cVZcdT46nenTt2KbnFAgl08hNZLLpr6VQaAoDwEALw_wcB"
    msg=f"Subject: {subject}\n\n{body}"    
    server.sendmail("xyz@gmail.com","abc@gmail.com",msg) #xyz@gmail.com-The senders email, abc@gmail.com-Receivers email
    print("Mail has bveen sent")
    server.quit()

while(True):
    Check_Price()
    time.sleep(60*60) #Will check after every hour
    
        

        
    
    
