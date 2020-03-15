# 引入requests和bs
import requests
from bs4 import BeautifulSoup


url = 'http://www.xiachufang.com/explore/'

res_foods = requests.get(url)                                        #请求网站
bs_foods = BeautifulSoup(res_foods.text,'html.parser')               #解析数据
articles = bs_foods.find_all('div',class_='info pure-u')             #提取数据
list_all = []

for food in articles:
    tag_a = food.find('a')                                           #查找a标签，里面包含菜名
    name = tag_a.text[17:-13]                                        #切片，且只筛选字符串
    url1 = 'http://www.xiachufang.com'+tag_a['href']                  #做法的网址  
    tag_p = food.find('p',class_='ing ellipsis')                     #食材的标签和属性
    ingredients = tag_p.text[1:-1]
    
    

    res = requests.get(url1)
    bs = BeautifulSoup(res.text,'html.parser')
    info = bs.find('div',class_='steps')
    step = info.find_all('p',class_='text')
    
    list_all.append(['--------------------'])
    list_all.append([name])
    list_all.append([ingredients])
   
    for i in step:
        method = i.text
        list_all.append([method])
print(len(list_all))

file = open('下厨房终极爬取.txt','w',encoding='utf-8')
for i in range(len(list_all)):
    s = str(list_all[i]).replace('[','').replace(']','')
    s = s.replace("'",'').replace(',','') +'\n'
    file.write(s)
file.close()




