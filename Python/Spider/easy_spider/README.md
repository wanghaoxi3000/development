# 简单爬虫架构

1. 爬虫调度端：启动爬虫，停止爬虫，监视爬虫的状态
2. URL管理器：管理将要爬取的URL，已经爬取过的URL
3. 网页下载器：获取指定网页的字符串信息
4. 网页解析器：解析爬取网页的字符串信息，获取有用的信息，并可将更多的URL补充至URL管理器