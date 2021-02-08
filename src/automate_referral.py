#from selenium import webdriver
from seleniumrequests import Chrome
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import time
import os
import pickle
import json

# browser authentication for auth and cookie grabbing
load_dotenv() 
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
UW_EMAIL=os.getenv("UW_EMAIL")
UW_NETID=os.getenv("UW_NETID")
UW_PASSWORD=os.getenv("UW_PASSWORD")

driver = Chrome(executable_path = DRIVER_BIN)

driver.set_window_position(0, 0)
driver.set_window_size(400, 1000)
driver.get("http://localhost:3000/api/login")

driver.find_element_by_id("identifierId").send_keys(UW_EMAIL)
driver.find_element_by_id("identifierNext").click()
time.sleep(1)
driver.find_element_by_id("weblogin_netid").send_keys(UW_NETID)
driver.find_element_by_id("weblogin_password").send_keys(UW_PASSWORD)
driver.find_element_by_id("submit_button").click()
time.sleep(1)
driver.find_element_by_xpath('//button[normalize-space()="Continue"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[normalize-space()="New referral"]').click()

# start for a browser automation approach

# CREATE A CHILD
driver.find_element_by_id("childFirstName").send_keys('Cindy')
driver.find_element_by_id("childLastName").send_keys('Martin')
driver.find_element_by_id("childDateOfBirth").send_keys('02/03/2020')
driver.find_element_by_xpath("//html").click()
sex = driver.find_element_by_id("sexOfChildIsFemale")
driver.execute_script("arguments[0].click();", sex)
driver.find_element_by_xpath("//html").click()
# wait for child search
time.sleep(2)
continueWithoutMatchRadio = driver.find_element_by_id("continueWithoutMatch")
driver.execute_script("arguments[0].click();", continueWithoutMatchRadio)

# CREATE A REFERRAL
continueButton = driver.find_element_by_xpath('//button[normalize-space()="Continue"]')
driver.execute_script("arguments[0].click();", continueButton)
time.sleep(1)
# Primary Contact Name
driver.find_element_by_id("primaryContactFirstName").send_keys("Carol")
driver.find_element_by_id("primaryContactLastName").send_keys('Tyler')
# Primary Contact Address
driver.find_element_by_id("primaryContactPhysicalAddressAddress1").send_keys('4222 Clinton Way')
driver.find_element_by_id("primaryContactPhysicalAddressCity").send_keys('Tacoma')
driver.find_element_by_id("primaryContactPhysicalAddressZip").send_keys('98406')
# Primary Contact Method (Needs support for email and mail)
selectPreferredContactMethod = Select(driver.find_element_by_id('preferredContactMethod'))
selectPreferredContactMethod.select_by_visible_text("Phone")
time.sleep(1)
# Primary Contact Method Detail (Needs support for email and mail)
driver.find_element_by_id("primaryContactPhone").send_keys("555-762-0799")
# Family Contact Status
familyContactedIsTrueButton = driver.find_element_by_id('familyContactedIsTrue')
driver.execute_script("arguments[0].click();", familyContactedIsTrueButton)
driver.find_element_by_id("familyContactDate").send_keys('02/06/2020')
driver.find_element_by_xpath("//html").click()
# Referring Party Information
driver.find_element_by_id("referringPartyFirstName").send_keys("Mistress")
driver.find_element_by_id("referringPartyLastName").send_keys('Tyler')
# Referring Party Role (needs support for all roles)
selectReferringPartyRole = Select(driver.find_element_by_id('referringPartyRole'))
selectReferringPartyRole.select_by_visible_text("Family Member")
# Referring Party Contact Method (needs support for email)
selectReferringPartyPreferredContactMethod = Select(driver.find_element_by_id('referringPartyPreferredContactMethod'))
# Primary Contact Method Detail (Needs support for email)
selectReferringPartyPreferredContactMethod.select_by_visible_text("Phone")
driver.find_element_by_id("referringPartyPhone").send_keys("555-762-0799")
# Date of initial referral
driver.find_element_by_id("dateOfInitialReferral").send_keys('02/03/2020')
driver.find_element_by_xpath("//html").click()
# Referral reason (need support for other reasons)
referralReason = driver.find_element_by_id("referralReasonIsDevelopmentConcerns")
driver.execute_script("arguments[0].click();", referralReason)
# post referral
createReferralButton = driver.find_element_by_xpath('//button[normalize-space()="Create referral"]')
driver.execute_script("arguments[0].click();", createReferralButton)

# start for a post approach (currently returns 401)
# get koa cookies
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver_cookies = pickle.load(open("cookies.pkl", "rb"))
koa_sess_cookie_dict = driver_cookies[1]
koa_sess_cookie_str = koa_sess_cookie_dict['value']
koa_sess_sig_cookie_dict = driver_cookies[0]
koa_sess_sig_cookie_str = koa_sess_sig_cookie_dict['value']
# read dummy referral record
with open('new_referral.json') as f:
    data_dict = json.load(f)
    data_str = json.dumps(data_dict)
# set minimum headers
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'http://localhost:3000',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'http://localhost:3000/create-referral',
    'Accept-Language': 'en-US,en;q=0.9',
}

# cookies as JSON
cookies_for_post = {
    'koa.sess': koa_sess_sig_cookie_str,
    'koa.sess.sig': koa_sess_cookie_str,
}

# make the post
response = driver.request('POST', 'http://localhost:3000/api/referral/create', headers=headers, cookies=cookies_for_post, data=data_str)

# print post results
print(cookies_for_post)
print(data_str)
print(response)

driver.quit()