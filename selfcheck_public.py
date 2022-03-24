# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:35:22 2021

@author: cgg
"""


from selenium import webdriver
import selenium
import time
import sys
import socket
def is_online():
    try:
        host=socket.gethostbyname("target website")
        s=socket.create_connection((host,80),2)
        return True
    except Exception as e:
        return False
while(not is_online()):
    i=0
driver = webdriver.Chrome()
driver.get("website")
time.sleep(1)
driver.find_element_by_id("username").send_keys("[your student id]")#keyin
driver.find_element_by_id("password").send_keys("[your password]")#keyin
driver.find_element_by_id("login").click()
time.sleep(1)
driver.find_element_by_id("report-submit-btn").click()
time.sleep(1)
driver.get("website")
time.sleep(1)
driver.find_element_by_id("uid").send_keys("[your mail name]")#keyin
driver.find_element_by_id("password").send_keys("[your mail password]")#keyin
js = 'changeDomain(\'mail.ustc.edu.cn\')'#if you are the teacher of USTC,delete "mail." 
driver.execute_script(js) 
driver.find_element_by_id("login_button").click()
time.sleep(1)
try:
    driver.find_element_by_id("navNewCount_1")
except:
    driver.close()
    quit()
driver.find_element_by_id("navFid_1").click()
