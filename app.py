from bs4 import BeautifulSoup
import urllib.request as urllib
import re
import time
import smtplib

# Configure the below details
site = 'https://in.bookmyshow.com/buytickets/annaatthe-coimbatore/movie-coim-ET00127667-MT/'
site += '20211104'
venue = 'INPT' # Inorbit Mall
showtime = ''
showList = ''
delay = 20 # Delays the script execution
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

# Configure the email account (if you need an email notification)
# Please do not give your account password, instead generate an app password
# Visit https://security.google.com/settings/security/apppasswords to generate an app password
USERNAME = 'tharani.calms@gmail.com'
PASSWORD = 'caagoszkivciqoit'

# Make sure you have enabled access to less secure apps on your account
# https://myaccount.google.com/les
# ssecureapps
TO = 'tharani.calms@gmail.com'
SUBJECT = 'movie tickets are now available!'



# Send email alert
def send_email_notification(movie):
    print('Sending email...')
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(USERNAME, PASSWORD)
    email = 'To:' + TO + '\n' + 'From: ' + USERNAME
    email += email + '\n' + 'Subject: ' + movie + ' ' + SUBJECT + '\n'
    print(email)
    email += email + '\n' + movie + ' '  + '\n\n' + TEXT + '\n\n'
    smtp.sendmail(USERNAME, TO, email)
    smtp.close()


request = urllib.Request(site, headers = headers)
content = urllib.urlopen(request)

soup = BeautifulSoup(content, 'lxml')

theaters = soup.find_all('div', {'data-online': 'Y'})
theaters = str(theaters)

soup2 = BeautifulSoup(theaters, 'lxml')
#print(soup2.contents)
theater = soup2.find_all('a', {'data-venue-code': venue})
theater = str(theater)
#print(theater)
# for p in theater:
#     print(p)

theatersoup = BeautifulSoup(theater, 'lxml')
showtimeList = theatersoup.find_all('a', {'data-availability': "A"})
for p in showtimeList:
    showList += 'movie tickets for ' + p.text.strip() + ' show are available.'+ '\n\n'
showtimeList = str(showtimeList)

if (showtime != ""):
    TEXT = 'movie tickets for ' + showtime + ' show are available.' + '\n\n Please book your tickets here: \n' + site
else: 
    TEXT = showList + '\n\n Please book your tickets here: \n' + site

showtime = soup2.find_all('a', {'data-display-showtime': showtime})
showtime = str(showtime)


movie = soup.find_all('meta', {'itemprop': 'name'})
movie = movie[-1]['content']

result = re.findall('data-availability="A"', theater)
if len(result) > 0:
    print('Tickets are available!')
    send_email_notification(movie)
else:
    print('Sorry, tickets are not available')

time.sleep(delay)