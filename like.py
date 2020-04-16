#!/bin/bash/python3
# by shiky

from time import sleep
import csv as cs
from selenium import webdriver
#browser=webdriver.Chrome()
browser=webdriver.Firefox(executable_path="./geckodriver")

def gloin(em,passed):
    browser.get("https://gmail.com")
    browser.find_element_by_id("identifierId").send_keys(em)
    browser.find_element_by_id("identifierNext").click()
    sleep(5)
    browser.find_element_by_name("password").send_keys(passed)
    browser.find_element_by_id("passwordNext").click()
    sleep(5)

def glogout():
    browser.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
    browser.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()

def add_lis(f):
    dlist=[]
    em = cs.reader(f)
    for r in em:
        dlist.append(r)
    return dlist
looges=open("email.txt",'r')
email_list=add_lis(looges)
password="22149388" # put the one password for all emails edit this
c=len(email_list)
video="https://www.youtube.com/watch?v=vlfIhnX2p_s&list=RDEDk9-GwX7SY&index=27" # put the video link here edit this
for i in range(len(email_list)):
    try:
        gloin(email_list[i],password)
        browser.get(video)
        sleep(3)
        like=browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a")
        #like=browser.find_element_by_xpath('//*[@id="button"]')
        like.click()
        sleep(3)
        glogout()
        browser.close()
        browser = webdriver.Firefox(executable_path="./geckodriver")
    except:
        print("try again")

print("done")
browser.close()