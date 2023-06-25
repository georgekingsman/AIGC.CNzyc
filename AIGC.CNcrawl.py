# !/user/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome



web = Chrome()
web.get("https://www.aigc.cn/")

more = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[1]/a')
more.click()

time.sleep(1)

article_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[2]/div')

for div in article_list:
    article_intro = div.find_element(By.XPATH,'./div/div[2]/div[1]/h2/a')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("行业资讯intro:"+article_intro.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)


hot_list = web.find_elements(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[4]/div')

for div in hot_list:
    hotid = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    hotintro = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("热门工具Tool Name:"+hotid.text)
        f.write("\n")
        f.write("Tool Introduction:"+hotintro.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)


more1 = web.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[5]/a')
more1.click()

time.sleep(1)

tool_list = web.find_elements(By.XPATH, '//*[@id="content"]/div/div/div[1]/div')

for div in tool_list:
    toolid = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("写作平台Tool Name:"+toolid.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more2 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[7]/a')
more2.click()

time.sleep(1)

tool2_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool2_list:
    toolid2 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro2 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("互动平台Tool Name:"+toolid2.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro2.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more3 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[9]/a')
more3.click()

time.sleep(1)

tool3_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool3_list:
    toolid3 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro3 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("绘画平台Tool Name:"+toolid3.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro3.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more4 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[11]/a')
more4.click()

time.sleep(1)

tool4_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool4_list:
    toolid4 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro4 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("视觉平台Tool Name:"+toolid4.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro4.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more5 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[13]/a')
more5.click()

time.sleep(1)

tool5_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool5_list:
    toolid5 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro5 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("影视平台Tool Name:"+toolid5.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro5.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more5 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[15]/a')
more5.click()

time.sleep(1)

tool5_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool5_list:
    toolid5 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro5 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("语音平台Tool Name:"+toolid5.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro5.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)


tool6_list = web.find_elements(By.XPATH,'//*[@id="tab-2359-2045"]/div/div')

for div in tool6_list:
    toolid6 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro6 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt", "a+", encoding='utf-8') as f:
        f.write("企业平台Tool Name:"+toolid6.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro6.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)


more7 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[19]/a')
more7.click()

time.sleep(1)

tool7_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool7_list:
    toolid7 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro7 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("办公平台Tool Name:"+toolid7.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro7.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more8 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[21]/a')
more8.click()

time.sleep(1)

tool8_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool8_list:
    toolid8 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro8 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("运营平台Tool Name:"+toolid8.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro8.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)


tool9_list = web.find_elements(By.XPATH,'//*[@id="tab-1916-2056"]/div/div')

for div in tool9_list:
    toolid9 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro9 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt", "a+", encoding='utf-8') as f:
        f.write("学习平台Tool Name:"+toolid9.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro9.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)


tool10_list = web.find_elements(By.XPATH,'//*[@id="tab-1851-1852"]/div/div')

for div in tool10_list:
    toolid10 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro10 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt", "a+", encoding='utf-8') as f:
        f.write("科研平台Tool Name:"+toolid10.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro10.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)



more11 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[27]/a')
more11.click()

time.sleep(1)

tool11_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool11_list:
    toolid11 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro11 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("开发平台Tool Name:"+toolid11.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro11.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)

more12 = web.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[29]/a')
more12.click()

time.sleep(1)

tool12_list = web.find_elements(By.XPATH,'//*[@id="content"]/div/div/div[1]/div')

for div in tool12_list:
    toolid12 = div.find_element(By.XPATH,'./div/a[1]/div/div[2]/div/strong')
    toolintro12 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt","a+",encoding='utf-8') as f:
        f.write("生活平台Tool Name:"+toolid12.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro12.text)
        f.write("\n")

    time.sleep(1)

web.back()
time.sleep(3)


tool13_list = web.find_elements(By.XPATH,'//*[@id="tab-1910-244"]/div/div')

for div in tool13_list:
    toolid13 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro13 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt", "a+", encoding='utf-8') as f:
        f.write("游戏平台Tool Name:"+toolid13.text)
        f.write("\n")
        f.write("Tool Introduction:"+toolintro13.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)


tool14_list = web.find_elements(By.XPATH,'//*[@id="tab-2188-2186"]/div/div')

for div in tool14_list:
    toolid14 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/div/strong')
    toolintro14 = div.find_element(By.XPATH, './div/a[1]/div/div[2]/p')

    with open("AIGC.txt", "a+", encoding='utf-8') as f:
        f.write("权威机构name:"+toolid14.text)
        f.write("\n")
        f.write("权威机构Introduction:"+toolintro14.text)
        f.write("\n")

    time.sleep(1)
time.sleep(3)