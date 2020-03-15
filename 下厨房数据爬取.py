import requests,openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()              #创建工作簿
sheet = wb.active                     #获取工作簿的活动表                                 
sheet.title= '下厨房数据'                 #工作表命名

sheet['A1'] = '菜名'                  #A1单元格命名
sheet['B1'] = '網站'                  #B1命名 
sheet['C1'] = '食材'                  #C1命名

url = 'http://www.xiachufang.com/explore/'

res_foods = requests.get(url)                                        #请求网站
bs_foods = BeautifulSoup(res_foods.text,'html.parser')               #解析数据
articles = bs_foods.find_all('div',class_='info pure-u')             #提取数据


for food in articles:
    tag_a = food.find('a')                                           #查找a标签，里面包含菜名
    name = tag_a.text[17:-13]                                        #切片，且只筛选字符串
    url = 'http://www.xiachufang.com'+tag_a['href']                  #做法的网址  
    tag_p = food.find('p',class_='ing ellipsis')                     #食材的标签和属性
    ingredients = tag_p.text[1:-1]
    sheet.append([name,url,ingredients])
    
    

wb.save('下厨房.xlsx')
