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


def init_driver():
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 5)
	return driver
	
def showMore(browser,URL,XPATH):
	browser.get(URL)
	count=0
	for a in browser.find_elements_by_xpath(XPATH):
		link_text = a.text
		if("Show more" in link_text):
			while(count < 5):
				try:
					print "[info] Button to click: %s" % a.text
					print "[info] DOM sleep: 15 seconds"
					time.sleep(15)
					a.click()
				except:
					print "[info] Reconfig click number and try again"
					# handle
					pass
				count += 1


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
	
	
	
	
	