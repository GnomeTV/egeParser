import lxml
import requests
from bs4 import BeautifulSoup
import re
import town

uni_link = []
links = []
excel_list = []
f = open('table.txt', 'w')
f.write('Регион/адрес,Универ,Сайт,ЕГЭ1,ЕГЭ2,ЕГЭ3,ЕГЭ4,Направления\n')
for i in range(0, len(town.univ_link)):
    print(town.univ_link[i] + '\n')
    if 'inst_' in town.univ_link[i]:
        try:
            response = requests.get('https://miccedu.ru/monitoring/2014/materials/' + town.univ_link[i])
            response.encoding = 'Windows-1251'
            content = response.text
            soup = BeautifulSoup(content, "lxml")
            name = soup.findAll('table')[0].findAll('tr')[0].findAll('td')[1].text.strip()
            name = re.sub('\s+', ' ', name)
            region = soup.findAll('table')[0].findAll('tr')[1].findAll('td')[1].text.strip()
            region = re.sub('\s+', ' ', region)
            site = soup.findAll('table')[0].findAll('tr')[4].findAll('td')[1].text.strip()
            site = re.sub('\s+', ' ', site)
            ege1 = soup.findAll('table')[3].findAll('tr')[1].findAll('td')[3].text.strip()
            ege1 = re.sub('\s+', ' ', ege1)
            ege2 = soup.findAll('table')[3].findAll('tr')[2].findAll('td')[3].text.strip()
            ege2 = re.sub('\s+', ' ', ege2)
            ege3 = soup.findAll('table')[3].findAll('tr')[3].findAll('td')[3].text.strip()
            ege3 = re.sub('\s+', ' ', ege3)
            ege4 = soup.findAll('table')[11].findAll('tr')[7].findAll('td')[3].text.strip()

            ege4 = re.sub('\s+', ' ', ege4)
            direction = soup.findAll('table')[10].findAll('tr')
            direction_list = []
            for k in range(1, len(direction)):
                middle_directrion = soup.findAll('table')[10].findAll('tr')[k].findAll('td')[0].text.strip()
                middle_directrion = re.sub('\s+', ' ', middle_directrion)
                direction_list.append(middle_directrion)
            result = '\"' + region + '\"' + ',' + '\"' + name + '\"' + ',' + '\"' + site + '\"' + ',' + '\"' + ege1 + '\"' + ',' + '\"' + ege2 + '\"' + ',' + '\"' + ege3 + '\"' + ',' + '\"' + ege4 + '\"'
            for l in range(0, len(direction_list)):
                result += ',' + '\"' + direction_list[l] + '\"'
            f.write(result + '\n')
        except:
            f.write('https://miccedu.ru/monitoring/2014/materials/' + str(town.univ_link[i]) + ',' + 'Error link' + '\n')

    else:
        try:
            response = requests.get('https://miccedu.ru/monitoring/2014/materials/' + town.univ_link[i])
            response.encoding = 'Windows-1251'
            content = response.text
            soup = BeautifulSoup(content, "lxml")
            name = soup.findAll('table')[0].findAll('tr')[0].findAll('td')[1].text.strip()
            name = re.sub('\s+', ' ', name)
            region = soup.findAll('table')[0].findAll('tr')[1].findAll('td')[1].text.strip()
            region = re.sub('\s+', ' ', region)
            site = soup.findAll('table')[0].findAll('tr')[4].findAll('td')[1].text.strip()
            site = re.sub('\s+', ' ', site)
            ege1 = soup.findAll('table')[2].findAll('tr')[1].findAll('td')[3].text.strip()
            ege1 = re.sub('\s+', ' ', ege1)
            ege2 = soup.findAll('table')[2].findAll('tr')[2].findAll('td')[3].text.strip()
            ege2 = re.sub('\s+', ' ', ege2)
            ege3 = soup.findAll('table')[2].findAll('tr')[3].findAll('td')[3].text.strip()
            ege3 = re.sub('\s+', ' ', ege3)
            ege4 = soup.findAll('table')[9].findAll('tr')[7].findAll('td')[3].text.strip()
            ege4 = re.sub('\s+', ' ', ege4)
            direction = soup.findAll('table')[8].findAll('tr')
            direction_list = []
            for k in range(1, len(direction)):
                middle_directrion = soup.findAll('table')[8].findAll('tr')[k].findAll('td')[0].text.strip()
                middle_directrion = re.sub('\s+', ' ', middle_directrion)
                direction_list.append(middle_directrion)
            result = '\"' + region + '\"' + ',' + '\"' + name + '\"' + ',' + '\"' + site + '\"' + ',' + '\"' + ege1 + '\"' + ',' + '\"' + ege2 + '\"' + ',' + '\"' + ege3 + '\"' + ',' + '\"' + ege4 + '\"'
            for l in range(0, len(direction_list)):
                result += ',' + '\"' + direction_list[l] + '\"'
            f.write(result + '\n')
        except:
            f.write('https://miccedu.ru/monitoring/2014/materials/' + str(town.univ_link[i]) + ',' + 'Error link' + '\n')

f.close()
