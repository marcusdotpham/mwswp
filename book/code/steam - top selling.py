from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')


def top_seller():
	# search web scraping
	url = 'https://store.steampowered.com/tags/en/Education/#p=0&tab=TopSellers'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', {'id':'TopSellersRows'})
	
	for a in div.find_all('a', class_='tab_item'):
		div_name = a.find('div', class_='tab_item_name')
		print(div_name.text)
		print(a['href'])
		detail(a['href'])
		print('\n')


def detail(url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	detail = soup.find('div', class_='game_description_snippet')
	if detail is not None:
		print(detail.text.replace('	',''))

top_seller()

