# Imports

import csv
import time
from selenium import webdriver

# Setup

with open('data1.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	# Web automation

	for line in csv_reader:
		
		driver = webdriver.Chrome()
		driver.get('http://mdslearninghub.com/user/login')

		time.sleep(1)

		user = driver.find_element("xpath", '//*[@id="edit-name"]')
		driver.execute_script("arguments[0].scrollIntoView();",user)
		user.send_keys("ContentManager1")

		time.sleep(1)

		passw = driver.find_element("xpath", '//*[@id="edit-pass--2"]')
		passw.send_keys("29.")

		time.sleep(2)

		login = driver.find_element("name", 'op')
		login.click()

		time.sleep(2)

		driver.get('http://mdslearninghub.com/node/add/ward%20representative')

		time.sleep(2)
		
		politician = driver.find_element("xpath", '//*[@id="edit-title-0-value"]')
		driver.execute_script("arguments[0].scrollIntoView();",politician)
		politician.send_keys(line[6])
		politician.send_keys("- Ward Representative")

		time.sleep(1)

		gender = driver.find_element("xpath", '//*[@id="edit-field-gender-0-target-id"]')
		gender.send_keys(line[7])
		
		time.sleep(1)

		elposition = driver.find_element("xpath", '//*[@id="edit-field-elective-position-0-target-id"]')
		elposition.send_keys("Members of County Assembly- Ward Representative (198)")

		time.sleep(1)

		elarea = driver.find_element("xpath", '//*[@id="edit-field-electorla-area-0-target-id"]')
		elarea.send_keys("County Electoral Ward (199)")

		time.sleep(1)

		government = driver.find_element("xpath", '//*[@id="edit-field-gover-0-target-id"]')
		government.send_keys("County Government (202)")

		time.sleep(1)

		aog = driver.find_element("xpath", '//*[@id="edit-field-arm-of-government-0-target-id"]')
		aog.send_keys("County Assembly (208)")

		time.sleep(1)

		eldate = driver.find_element("xpath", '//*[@id="edit-field-election-0-target-id"]')
		eldate.send_keys('"Tuesday, 9 August 2022 (179)"')

		time.sleep(1)

		polparty = driver.find_element("xpath", '//*[@id="edit-field-party-0-target-id"]')
		polparty.send_keys(line[8])

		time.sleep(1)

		coalparty = driver.find_element("xpath", '//*[@id="edit-field-political-coalition-0-target-id"]')
		coalparty.send_keys(line[9])

		time.sleep(1)

		status = driver.find_element("xpath", '//*[@id="edit-field-office-status-0-target-id"]')
		status.send_keys("Elected (176)")

		time.sleep(1)

		term = driver.find_element("xpath", '//*[@id="edit-field-office-term-0-target-id"]')
		term.send_keys('"Tuesday, 9 August 2022 to Tuesday, 9 August 2027 (180)"')

		time.sleep(1)

		country = driver.find_element("xpath", '//*[@id="edit-field-country-0-target-id"]')
		country.send_keys("Kenya (181)")

		time.sleep(1)

		countrycode = driver.find_element("xpath", '//*[@id="edit-field-country-code-0-target-id"]')
		countrycode.send_keys("+254 (182)")

		time.sleep(1)

		name = driver.find_element("xpath", '//*[@id="edit-field-politician-name-0-target-id"]')
		name.send_keys(line[6])

		time.sleep(1)

		county = driver.find_element("xpath", '//*[@id="edit-field-county-name-0-target-id"]')
		county.send_keys(line[1])

		time.sleep(1)

		countycode = driver.find_element("xpath", '//*[@id="edit-field-county-code-0-target-id"]')
		countycode.send_keys(line[0])

		time.sleep(5)

		constcy = driver.find_element("xpath", '//*[@id="edit-field-constituency-name-0-target-id"]')
		constcy.send_keys(line[3])

		time.sleep(1)

		constcycode = driver.find_element("xpath", '//*[@id="edit-field-constituency-code-0-target-id"]')
		constcycode.send_keys(line[2])

		time.sleep(1)

		ward = driver.find_element("xpath", '//*[@id="edit-field-county-ward-name-0-target-id"]')
		ward.send_keys(line[5])

		time.sleep(1)

		wardcode = driver.find_element("xpath", '//*[@id="edit-field-country-ward-code-0-target-id"]')
		wardcode.send_keys(line[4])

		time.sleep(1)


		focus = driver.find_element("xpath", '//*[@id="edit-field-real-time-seo-status-focus-0-yoast-seo-focus-keyword"]')
		focus.send_keys(line[6])
		focus.send_keys(", Ward Representative, ")
		focus.send_keys(line[1])
		focus.send_keys(", ")
		focus.send_keys(line[3])
		focus.send_keys(", ")
		focus.send_keys(line[10])
		focus.send_keys(", Hustler, Freedom is here, Mapema ndio best")

		time.sleep(1)

		save = driver.find_element("name",'op')
		save.click()

		






		