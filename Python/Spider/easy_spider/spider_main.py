#!/usr/bin/env python
# -*- coding:utf-8 -*-

import html_outputer
import url_manager
import html_downloader
import html_parser


class SpiderMain:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parse = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw {0}: {1}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parse.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 50:
                    break
                count = count + 1
            except:
                print('craw fail')

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spoder = SpiderMain()
    obj_spoder.craw(root_url)
