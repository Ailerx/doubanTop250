from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import os
import urllib
# 随机请求头和随机代理列表
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/95.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/95.0.1020.40 Safari/537.36 Edg/95.0.1020.40',
    # ...
]

proxy_list = ['http://ip1:port', 'http://ip2:port', 'http://ip3:port']
# 随机选择请求头
headers = {
    'User-Agent': random.choice(user_agent_list),
    'Accept-Language': 'en-US,en;q=0.9',
}

# 随机选择代理
proxy_ip = random.choice(proxy_list)
proxy_options = webdriver.ChromeOptions()
proxy_options.add_argument(f'--proxy-server={proxy_ip}')
proxy_options = webdriver.ChromeOptions()
proxy_options.add_experimental_option("detach", True)       #防止异常关闭
url = 'https://movie.douban.com/top250'
web = webdriver.Chrome(options=proxy_options)
web.maximize_window()
web.get(url)
time.sleep(random.uniform(1.5, 3.5))
folder_path="./film_pic/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

j=int(input("请输入要爬取的页数"))
k=1
while(j>0):
    f = open("films.txt", mode='a', encoding='utf-8')
    l = web.find_element(By.CLASS_NAME, "article")
    l1 = l.find_elements(By.CLASS_NAME, "item")
    i = 1
    for l in l1:
        time.sleep(2)
        Xpath=f'//*[@id="content"]/div/div[1]/ol/li[{i}]/div/div[1]/a/img'
        moives_poster = l.find_element(By.CLASS_NAME, "pic").find_element(By.XPATH, Xpath)      #电影海报
        moives_poster_url=moives_poster.get_attribute('src')
        file_path = os.path.join(folder_path,f"poster_{k}.jpg")
        urllib.request.urlretrieve(moives_poster_url,file_path)
        i+=1
        moives_name=l.find_element(By.CLASS_NAME,"title").text          #电影名
        moives_directer=l.find_element(By.CLASS_NAME,"bd").find_element(By.CSS_SELECTOR,"p:first-child").text       #导演及演员
        moives_position=l.find_element(By.CLASS_NAME,"pic").find_element(By.CSS_SELECTOR,"em").text                 #电影名次
        moives_score = l.find_element(By.CLASS_NAME, "star").find_element(By.CLASS_NAME, "rating_num").text         #电影分数
        moives_comments = l.find_element(By.CLASS_NAME, "star").find_element(By.CSS_SELECTOR, "span:last-child").text  #电影评价数
        f.write(moives_position)
        f.write(',')
        f.write(moives_name)
        f.write(',')
        f.write(moives_directer.replace("\n"," "))
        f.write(',')
        f.write(moives_score)
        f.write(',')
        f.write(moives_comments)
        f.write('\n')
        print(f"第{k}部电影爬取完毕")
        k += 1
    j-=1
    wait = WebDriverWait(web, 10)
    web.find_element(By.XPATH, "//*[@id='content']/div/div[1]/div[2]/span[3]/a").click()
    time.sleep(2.5)
