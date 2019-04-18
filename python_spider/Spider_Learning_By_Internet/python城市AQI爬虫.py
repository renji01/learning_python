from splinter import Browser
import time
import csv

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html


def main():
    city_name = input("请输入城市名字：")
    browser = Browser('chrome')
    browser.visit('https://www.aqistudy.cn/historydata/monthdata.php?city=' + city_name)
    time.sleep(3)
    rows = browser.find_by_xpath('//table//tbody//tr')
    titles = rows[0]
    title_str = ''
    for title in titles.find_by_xpath('th'):
        title_str += title.html + '\t'
    print(title_str)
    header = ['月份', 'AQI','范围', '质量等级', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h']
    with open('{}_aqi.csv'.format(city_name), 'w', encoding='GB2312', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range( 1, len(rows) ):
            columns = rows[i].find_by_xpath('td')
            month = columns[0].find_by_tag('a')[0].html
            aqi = columns[1].html
            fanwei = columns[2].html
            zhiliang = columns[3].find_by_tag('span')[0].html
            pm25 = columns[4].html
            pm10 = columns[5].html
            so2 = columns[6].html
            co = columns[7].html
            no2 = columns[8].html
            o3 = columns[9].html
            row = ([month] + [aqi] + [fanwei] + [zhiliang] + [pm25] + [pm10] + [so2] + [co] + [no2] + [o3])
            print(row)
            writer.writerow(row)



if __name__ == '__main__':
    main()

#browser.quit()