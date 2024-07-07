import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

path = 'https://ding.cjfx.cn/f/oorz62yc'
browser = webdriver.Edge()  # 打开浏览器
browser.maximize_window()  # 浏览器最大化
browser.get(path)  # 打开网页
browser.implicitly_wait(10)
i=44
count=1
while count<=i:
    num=str(count).rjust(2,'0')
    time.sleep(2)
    browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[4]/div/div[2]/div/div/input").send_keys(num)
    time.sleep(2)
    action=ActionChains(browser)#建立一个动作（单击）
    classify=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[5]/div/div/div/div/div[3]/div/div/div/label/span[1]/span/span");action.click(classify).perform()
    region=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[6]/div/div/div/div/div[10]/div/div/div/label/span[1]/span/span");action.click(region).perform()
    q1=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[7]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q1).perform()
    q2=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[8]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q2).perform()
    q3=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[9]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q3).perform()
    q4=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[10]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q4).perform()
    q5=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[11]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q5).perform()
    q6=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[12]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q6).perform()
    q7=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[13]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q7).perform()
    q8=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[14]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q8).perform()
    q9=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[15]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q9).perform()
    q10=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[16]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q10).perform()
    q11=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[17]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q11).perform()
    q12=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[18]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q12).perform()
    q13=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[19]/div/div/div/div/div[1]/div/div/div/label/span[1]/span/span");action.click(q13).perform()
    time.sleep(2)
    print('第%d份已确认填写完成'%(count))
    count+=1
    tj=browser.find_element(By.XPATH,"/html/body/div/div/div[3]/div/article/div/section/div[1]/div[20]/div/div/button");action.click(tj).perform()
    time.sleep(3)
    browser.refresh()
    time.sleep(3)

