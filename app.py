import requests 
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY?ref_=Oct_DLandingS_D_2f2e560d_60&smid=A14CZOWI0VEHLG'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
def check_price():
    page = requests.get(url , headers = headers)

    soup = BeautifulSoup(page.content , 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    cost = soup.find(id = 'priceblock_dealprice').get_text().replace(',' , '')

    actual_price = float(cost[1:])

    if (actual_price < 69000):
        send_mail()
 

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Enter your own email , make sure that it's two step verification in on and enable app passwords.
    #To enable app passwords , go to: https://myaccount.google.com/intro/security
    
    server.login('aditya09temp@gmail.com', 'fjtlbiceuadvpruy')

    subject = 'price down on Amazon! for Iphone 11' 

    body = 'check link : https: // www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY?ref_ = Oct_DLandingS_D_2f2e560d_60 & smid = A14CZOWI0VEHLG'
    message = f"Subject : {subject} \n\n {body}"

    server.sendmail (
        'aditya09test@gmail.com' , 
        #Your email , 
        message 
    )

    print('email sent succesfuly!')

    server.quit()

while (True):
    check_price()
    time.sleep(25)
