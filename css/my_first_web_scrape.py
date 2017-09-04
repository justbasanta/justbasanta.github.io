from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.sastodeal.com/sastodeal/faces/category.jsp?cts=1'

#opening the connection and grabbing the page
uClient = uReq(my_url)

#read the html and stores in varibale page_html
page_html = uClient.read() 

uClient.close()

page_soup = soup(page_html, "html.parser")

#grabbing the needed section
containers = page_soup.findAll("section", {"class": "categoryProduct"})

for container in containers:
	rate = containers[0].span.text.strip()

	prod_detail = containers.[0].findAll("div", {"class"} : "prod-detail")
	product = prod_detail[0].text.strip()

	print("Product name : " + product)
	print("Rate : " + rate)