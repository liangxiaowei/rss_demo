# -*- coding: utf-8 -*- 
import scrapy
import os
import re
import requests as req
from article import Article

class RssSpider(scrapy.Spider):
    name = "rss"

    # 通过 35篇
    # start_urls = ['https://niorgai.github.io/archives/']
    # allowed_domains = ["https://niorgai.github.io"]
    # next_url = "https://niorgai.github.io/archives/page/2/"

    # 143篇 实际144
    # 问题 会把页面所有的a标签都当成文章
    # 实际上，单页的静态博客样式比较简单，一般只有标题列表
    # e.g http://www.yinwang.org/ 
    # e.g http://knowthyself.cn/
    # todo
    # start_urls = ['http://dingyu.me/blog/']
    # allowed_domains = ["http://dingyu.me"]
    # next_url = ""

    # start_urls = ['http://www.yinwang.org/']
    # allowed_domains = ["http://www.yinwang.org"]
    # next_url = ""

    # 75篇
    # 问题：年份archive，和分类archive, 结果多了5个
    # href="/categories/Android//"
    # 解决：硬编码过滤
    # start_urls = ['http://yifeng.studio/archives/']
    # allowed_domains = ["http://yifeng.studio/"]
    # next_url = "http://yifeng.studio/page/2"

    # 554篇
    # 问题：分类太细。。。只出现一次的分类链接有很多
    # http://blog.inching.org/tags/bash/
    # 解决：硬编码过滤
    # 问题：有些文章标题出现多次，但是链接不一样
    # 解决：以文章链接为key
    # start_urls = ['http://blog.inching.org/archives/']
    # allowed_domains = ["http://blog.inching.org"]
    # next_url = "http://blog.inching.org/archives/page/2"
    
    # 55篇
    # 算通过，过滤了一个ppt链接
    # start_urls = ['http://wsztrush.github.io/index.html']
    # allowed_domains = ["http://wsztrush.github.io"]
    # next_url = "http://wsztrush.github.io/page2"
    
    # 13篇
    # 通过
    # start_urls = ['https://lision.me/archives/']
    # allowed_domains = ["https://lision.me"]
    # next_url = "https://lision.me/archives/page/2"
 
    # 70篇
    # 通过 多了一个关于我
    # start_urls = ['https://allenwu.itscoder.com/']
    # allowed_domains = ["https://allenwu.itscoder.com"]
    # next_url = "https://allenwu.itscoder.com/page2"
    
    # 254篇
    # 问题 多了一个page20,因为每一页都可以回到上一页和去下一页
    # 解决：硬编码正则
    # start_urls = ['https://61.life/']
    # allowed_domains = ["https://61.life"]
    # next_url = "https://61.life/page/2"
    
    # 69篇
    # 问题 文章内容可能引用了别的页的文章
    # 问题 每一页都有最新文章区域
    # 解决 增加相同区域过滤
    # start_urls = ['http://zhangtielei.com/']
    # allowed_domains = ["http://zhangtielei.com"]
    # next_url = "http://zhangtielei.com/posts/page2/index.html"

    # 59篇
    # 通过
    # start_urls = ['http://lfkdsk.github.io/archives/']
    # allowed_domains = ["http://lfkdsk.github.io"]
    # next_url = "http://lfkdsk.github.io/archives/page/2"

    # 16篇
    # 通过
    # start_urls = ['http://abner-nimengbo.cn/']
    # allowed_domains = ["http://abner-nimengbo.cn"]
    # next_url = "http://abner-nimengbo.cn/page/2"

    # 65篇
    # 问题 下一页，没有404，导致没有停止
    # 解决 判断当前页有没有非过滤掉的link
    # 问题 文章标题重复
    # 解决 增加相同区域过滤
    # start_urls = ['http://bennyhuo.leanote.com/']
    # allowed_domains = ["http://bennyhuo.leanote.com"]
    # next_url = "http://bennyhuo.leanote.com/?page=2"
    
    # 38篇
    # 通过
    # start_urls = ['http://notes.stay4it.com/archives/']
    # allowed_domains = ["http://notes.stay4it.com"]
    # next_url = "http://notes.stay4it.com/archives/page/2"
    
    # 36篇
    # 通过
    # start_urls = ['http://rkhcy.github.io/archives/']
    # allowed_domains = ["http://rkhcy.github.io"]
    # next_url = "http://rkhcy.github.io/archives/page/2"

    # 37篇
    # 通过
    # start_urls = ['http://weishu.me/archives/']
    # allowed_domains = ["http://weishu.me"]
    # next_url = "http://weishu.me/archives/page/2"

    # 134篇
    # 问题 最新文章区域，推广区域链接到自己文章
    # 解决 增加相同区域过滤
    # start_urls = ['http://liuwangshu.cn/archives/']
    # allowed_domains = ["http://liuwangshu.cn"]
    # next_url = "http://liuwangshu.cn/archives/page/2"
    
    # 75篇
    # 通过
    # 问题 第一页和第二页的html文本不一样，第二页奇葩地多了空行和注释
    # 解决 正则过滤空行和注释
    # start_urls = ['https://blog.piasy.com']
    # allowed_domains = ["https://blog.piasy.com"]
    # next_url = "https://blog.piasy.com/page2"

    # 135篇
    # 通过
    # start_urls = ['http://ice1000.org/']
    # allowed_domains = ["http://ice1000.org"]
    # next_url = "http://ice1000.org/page2"    
    
    # 44篇 实际43
    # 问题 文章内容可能引用了别的页的文章
    # 解决 不再需要跨页去重
    # 问题 多了一个 https://blog.ibireme.com/author/ibireme/
    # start_urls = ['https://blog.ibireme.com/']
    # allowed_domains = ["https://blog.ibireme.com"]
    # next_url = "https://blog.ibireme.com/page/2"
    
    # 170篇
    # 问题 置顶文章 热门文章
    # start_urls = ['http://gityuan.com/']
    # allowed_domains = ["http://gityuan.com"]
    # next_url = "http://gityuan.com/page2"

    # 问题 非主流分页
    # todo
    # start_urls = ['https://tech.meituan.com/']
    # allowed_domains = ["https://tech.meituan.com"]
    # next_url = "https://tech.meituan.com/?l=40&pos=0"

    start_urls = ['http://taobaofed.org/']
    allowed_domains = ["http://taobaofed.org"]
    next_url = "http://taobaofed.org/page/2"

    page_index = 1
    articleId = 1
    result_map = {}
    result_array = []
    filter_url = []
    # 页面结构不重复的地方，从开头数的行个数
    start = 0
    # 页面结构不重复的地方，从底部数的行个数
    end = 0
    reBODY =re.compile( r'<body.*?>([\s\S]*?)<\/body>', re.I)
    reCOMM = r'<!--[\s\S]*?-->'
    reBlankLine = r'\n\s+'
    
    # ^\n|\n+(?=\n)|\n$
    def parse(self, response):
        # 解析出body标签里面的内容
        htmlBody = self.processResp(response.body)
        # 根据第二页得出两页之间不同的内容区域
        if self.page_index == 1 and self.next_url != "":
            self.parseSecondPage(htmlBody)
        lineArray = htmlBody.split("\n")
        endLine = len(lineArray) - self.end
        print "start\n",self.start
        print "endLine\n",endLine
        listBody = "".join(lineArray[self.start:endLine])
        with open("listbody", 'wb') as f:
            f.write(listBody)
        sel = scrapy.Selector(text=listBody)
        links_in_a_page = sel.xpath('//a[@href]')
        
        hasNextPage = False
        # 遍历当前页面的所有合法链接，只进去一次，只需要取出标题
        for link_sel in links_in_a_page:
            
            link = str(link_sel.re('href="(.*?)"')[0]) 
            if not link.startswith("http"):
                link = self.allowed_domains[0] + link
            
            if self.isValidUrl(link):   
                hasNextPage = True
                request = scrapy.Request(link, callback=self.parseDetailPage, dont_filter = True) 
                request.meta['page'] = self.page_index
                request.meta['articleId'] = self.articleId
                self.articleId += 1
                yield request
                   
        self.page_index += 1  
        if self.next_url !="" and hasNextPage:
            yield scrapy.Request(self.getNextPage(), callback=self.parse, dont_filter = True)    

    def parseSecondPage(self, htmlBody1):
        try:
            resp = req.get(self.next_url, timeout=5)
        except Exception as e:
            raise e
        resp.encoding = "UTF-8"
        htmlBody2 = self.processResp(resp.text)
        self.findListRegion(htmlBody1, htmlBody2)
        

    def parseDetailPage(self, response):
        page = response.meta['page']
        articleId = response.meta['articleId']
        title = response.xpath('//title/text()')[0].extract()
        # todo 这里应该是去除标题重复后缀，'-'会误伤
        if title.find('|') != -1:
            title = title[:title.rindex('|')]
        # if title.find('-') != -1:
        #     title = title[:title.rindex('-')]

        article = Article(response.url, title.strip(), page, articleId)
        key = article.hashKey()

        if self.result_map.has_key(key):
            # self.result_map[key].setPage(page)
            if self.result_map[key].articleId <= articleId:
                self.result_map[key].articleId = articleId
                self.result_array.remove(article)
                self.result_array.append(article) 
        else:
            self.result_map[key] = article
            self.result_array.append(article) 
           

    # todo 错误处理    
    def findListRegion(self, page1, page2):
        page1ContentArray = page1.split("\n")
        page2ContentArray = page2.split("\n")
        self.start = 0
        self.end = 0        
        end1 = len(page1ContentArray) - 1
        end2 = len(page2ContentArray) - 1
        while True:
            if self.start > end1 or self.start > end2:
                break

            if page1ContentArray[self.start].decode("UTF-8") == page2ContentArray[self.start]:
                # print "start匹配成功",page1ContentArray[self.start]
                self.start += 1
            else:
                # print "start匹配结束",page1ContentArray[self.start]
                # print "start匹配结束",page2ContentArray[self.start]
                break
        
        while True:
            if end1 < 0 or end2 < 0:
                break

            if page1ContentArray[end1].decode("UTF-8") == page2ContentArray[end2]:
                # print "end匹配成功",page1ContentArray[end1]
                end1 -= 1
                end2 -= 1
                self.end += 1
            else:
                # print "end匹配结束",page1ContentArray[end1]
                # print "end匹配结束",page2ContentArray[end2]
                break
              

    # todo这里写2不好
    def getNextPage(self):
        return str(self.page_index).join(self.next_url.rsplit('2', 1))

    def closed(self, reason):
        with open("result.txt", 'wb') as f:
            for article in sorted(self.result_array):
                f.write("page" + str(article.pageIndex) + ": link:" + article.link.encode('utf-8'))
                f.write(" title: " + article.title.encode('utf-8'))
                f.write(" articleId: " + str(article.articleId))
                f.write("\n")
                    

    # todo about 404
    def isValidUrl(self, url):
        return  url.startswith(self.allowed_domains[0]) and not self.isCategory(url) and not self.isTag(url) and not self.isArchive(url) and not self.isMainSite(url) and not self.isPage(url) and not self.isHash(url)

    def isCategory(self, url):
        return url.find("/categories/") != -1 or url.find("/category/") != -1 or url.endswith("/categories") or url.endswith("/category")

    def isTag(self, url):
        return url.find("/tags/") != -1 or url.find("/tag/") != -1 or url.endswith("/tags") or url.endswith("/tag")    

    def isArchive(self, url):
        return url.find("/archives/") != -1 or url.find("/archive/") != -1 or url.endswith("/archive") or url.endswith("/archives")        

    def isMainSite(self, url):
        return (url == self.allowed_domains[0]) or (url == self.allowed_domains[0]+'/')

    def isPage(self, url):
        if self.next_url != "":
            pattern = re.compile('[0-9]+'.join(self.next_url.rsplit('2', 1))) 
            return pattern.match(url)
        else:
            return False    

    def isHash(self, url):
        return url.find("#") != -1        

    def processResp(self, resp):
        content = re.findall(self.reBODY, resp)[0]
        content = re.sub(self.reCOMM, "", content)
        content = re.sub(self.reBlankLine, "\n", content)

        return content   