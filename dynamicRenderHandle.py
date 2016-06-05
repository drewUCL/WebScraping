'''
Author: Andrew D. Mann
Last Update: 20160605 
'''


import time
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup


def init_driver():
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 5)
	return driver
	
def filterDirtyData(browser):
	html_source = browser.page_source
	soup = BeautifulSoup(html_source,'html.parser') 
	scrape_data = soup.findAll('table',{'class':'genTbl openTbl ecHistoryTbl'})
	print scrape_data
	for row in scrape_data:
		cells = row.find_all("td")
		print cells 
		#rn = cells.get_text() #cells[0]
		#print rn
	
def showMore(browser,URL,XPATH):
	browser.get(URL)
	time.sleep(15) # let page load
	count = 0
	for a in browser.find_elements_by_xpath(XPATH):
		link_text = a.text
		#if("Show more" in link_text):
		while(count < 2):
			try:
				print "[info] Button to click: %s" % a.text
				print "[info] DOM sleep: 15 seconds"
				time.sleep(15)
				#browser.execute_script("document.getElementById('id').scrollIntoView();")
				#browser.find_element_by_id("eventHistoryTable345").send_keys(Keys.NULL)
				browser.execute_script("window.scrollBy(0, -150);")
				action = webdriver.common.action_chains.ActionChains(browser)
				action.move_to_element(a)
				action.click()
				action.perform()
				print "[Massage] Success"
			except:
				print "[Message] Could not find element location\n"
				# handle - try to re focus as the element moves down the page
				browser.execute_script("window.scrollBy(0, -150);")
			count += 1
			
	# Now scrape the page contents
	filterDirtyData(browser)


if __name__ == "__main__":
	PAGE_URL = 'http://www.investing.com/economic-calendar/mi-inflation-gauge-345'
	xpath = './/div[@id="showMoreHistory345"]/a'
	browser = init_driver()
	epoch=0
	pages = ['PAGE_1']
	while(epoch < len(pages)):
		print "[info] epoch: %s" % (epoch)
		#PAGE_URL would be pages[epoch] ## NOTE I AM ONLY DOING ONE EXAMPLE
		showMore(browser,PAGE_URL,xpath)
		epoch += 1
	print "[info] Complete"
	
	
	
	
	