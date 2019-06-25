import bs4,ssl,requests
from urllib2 import urlopen
from bs4 import BeautifulSoup as soup
import mysql.connector

import htmldate

mydb = mysql.connector.connect()

	mycursor = mydb.cursor();

	mycursor.execute("create database scrap_data")
	mycursor.execute("create TABEL scraped")


my_url='https://innovaccer.com/news/'


context = ssl._create_unverified_context()
uClient = urlopen(my_url, context=context)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"col-lg-8"})

for container in containers:
	heading = container.h6.text

	description = container.p

	link = container.a["href"]

	date= htmldate.find_date(container.text)

	cursor.execute("Insert into scraped(heading,description,link,date) values(?, ?, ?, ?)",(heading, description, link, date))



	print( "heading :" + heading )
	print("link : " + str(my_url) + str(link)  )
	print("date : " , date)