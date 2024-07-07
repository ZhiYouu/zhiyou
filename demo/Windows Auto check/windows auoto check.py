import pyautogui
import time
import datetime
import os

pyautogui.click(1916,1059,button='left')##回到桌面
pyautogui.click(18,1059,button='left') ##
time.sleep(10)
pyautogui.click(470,670,button='left') ##打开雷电
time.sleep(50)
pyautogui.click(1244,252,button='left') ##关闭广告
time.sleep(5)
pyautogui.click(836,265,button='left') ##进入学习通
time.sleep(40)
pyautogui.click(848,400,button='left') ##点击我的课程
time.sleep(20)
pyautogui.click(888,197,button='left') ##留校课程
time.sleep(20)
pyautogui.click(877,301,button='left') ##进入签到界面
time.sleep(20)
pyautogui.click(1127,569,button='left') ##允许使用地理位置
time.sleep(20)
pyautogui.click(959,860,button='left') ##签到
time.sleep(20)
name=datetime.date.today()      ##截图
img=pyautogui.screenshot(fr'C:\Users\pc1\Desktop\打卡记录\{name}.png')
pyautogui.click(1916,1059,button='left') ##回到桌面

time.sleep(10)

pyautogui.doubleClick(1851,767,button='left')#打开图片所在文件夹
time.sleep(10)
pyautogui.hotkey('alt', 'space','x')    #最大化
time.sleep(10)
pyautogui.click(148,270,button='right')
time.sleep(10)
pyautogui.press('c')        #复制最新照片
time.sleep(10)
pyautogui.doubleClick(1885,9,button='left') #关闭文件夹
time.sleep(10)
pyautogui.doubleClick(1665,1059,button='left')  #打开qq
time.sleep(20)
pyautogui.doubleClick(1665,1059,button='left')  #打开qq
time.sleep(10)
pyautogui.doubleClick(1694,271,button='left')  #keep yourself
time.sleep(10)
pyautogui.hotkey('ctrl','v')    #复制
time.sleep(10)
pyautogui.press('enter')#发送
pyautogui.click(1916,1059,button='left') ##回到桌面
time.sleep(10)
pyautogui.doubleClick(1838,29,button='left')##最小化QQ
time.sleep(10)
os.system("taskkill /F /IM DNPLAYER.EXE")#关闭指定程序