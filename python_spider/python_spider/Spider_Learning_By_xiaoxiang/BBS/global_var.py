headers = {
        'Host': "www.newsmth.net",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': "en-US,en;q=0.5",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "http://www.newsmth.net/nForum/",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'cache-control': "no-cache"
    }

crawl_interval = 2

#代码执行顺序：
#先执行 mysql_manager.py文件建立存储表结构
#在执行board.py文件抓取版面信息
#在执行topic.py文件抓取版面下的主题信息。
#再执行post_list.py文件，抓取每个主题下的楼层信息。