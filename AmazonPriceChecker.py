import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.amazon.com/gp/product/B01KIIQUFW/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=C9WZAQB28R1NPGEPKNDQ&pf_rd_t=101&pf_rd_p=eec6b011-e8a9-43c7-816b-77061796d8ac&pf_rd_i=17871138011"
headers= 

def check_price(): # parses the web for the titel and price. It then compares the price and sends email
    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.text,'lxml')
    title = soup.select_one("h1 > #productTitle").get_text(strip=True)
    price= soup.find(id="priceblock_ourprice").get_text()
    converted_price= float(price[1:4])
    if (converted_price< 350):
        send_mail()
    print (converted_price)
def send_mail():
    server= smtplib.SMTP('smtp.gmail.com', 587) #used to send email
    server.ehlo() #used for connection between two email servers
    server.starttls() #encyption when establishing connection
    server.ehlo()

    server.login('ibrahimhajimohamed@gmail.com', 'tpsvcukhgxojqtme')
    subject= 'Price fell down'
    body = 'Check the amazon link  https://www.amazon.com/gp/product/B01KIIQUFW/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=C9WZAQB28R1NPGEPKNDQ&pf_rd_t=101&pf_rd_p=eec6b011-e8a9-43c7-816b-77061796d8ac&pf_rd_i=17871138011'
    msg = f"subject: {subject}\n\n{body}" #message format
    server.sendmail('ibrahimhajimohamed@gmail.com',
        'burhandinamedie@yahoo.com',
        msg
        ) # send email from,to,message
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()
while (True): # check every hour for a price
    check_price()
    time.sleep(60*60)
