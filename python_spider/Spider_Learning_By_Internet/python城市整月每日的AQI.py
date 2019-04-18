from splinter import Browser
import time
import csv

def main():
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    city_name = input("请输入城市名字：")
    month = input("请输入年月（格式为2014-01）：")
    browser = Browser('chrome')
    browser.visit('https://www.aqistudy.cn/historydata/daydata.php?city='+ city_name + '&month='+ month)
    time.sleep(3)
    rows = browser.find_by_xpath('//table//tbody//tr')
    titles = rows[0]
    title_str = ''
    for title in titles.find_by_xpath('th'):
        title_str += title.html + '\t'
    print(title_str)
    header = ['日期','AQI','质量等级','PM2.5','PM10','SO2','CO','NO2','O3_8h']
    with open('{}_{}_aqi.csv'.format(city_name,month), 'w', encoding='GB2312', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range( 1, len(rows) ):
            columns = rows[i].find_by_xpath('td')
            date = columns[0].html
            aqi = columns[1].html
            zhiliang = columns[2].find_by_tag('span')[0].html
            pm25 = columns[3].html
            pm10 = columns[4].html
            so2 = columns[5].html
            co = columns[6].html
            no2 = columns[7].html
            o3 = columns[8].html
            row = ([date] + [aqi]  + [zhiliang]  + [pm25]   + [pm10]  + [so2]  + [co]  + [no2]  + [o3])
            print(row)
            writer.writerow(row)

    # def main():
    #     header = [title_str]
    #     with open('xian_date_aqi.csv','w',encoding='utf-8',newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(header)
    #         for i in range (1,len(rows)):
    #             columns = rows[i].find_by_xpath('td')
    #             date = columns[0].html
    #             aqi = columns[1].html
    #             zhiliang = columns[2].find_by_tag('span')[0].html
    #             pm25 = columns[3].html
    #             pm10 = columns[4].html
    #             so2 = columns[5].html
    #             co = columns[6].html
    #             no2 = columns[7].html
    #             o3 = columns[8].html
    #             row = (date + aqi + zhiliang + pm25  + pm10 + so2 + co + no2 + o3)
    #             writer.writerrow(row)
#
if __name__ == '__main__':
    main()




#browser.quit()