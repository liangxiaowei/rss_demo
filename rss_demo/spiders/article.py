# -*- coding: utf-8 -*- 

def cmpArticle(a, b):
    aId = a.articleId
    bId = b.articleId
    if aId > bId:
        return 1
    elif aId < bId:
        return -1
    else:
        return 0

class Article:
    def __init__(self, link, title, pageIndex, articleId):
        self.link = link
        self.title = title
        self.pageIndex = pageIndex
        self.articleId = articleId

    def hashKey(self):
       return self.link
    
    def setpage(self, pageIndex):
        self.pageIndex = pageIndex   

    def __eq__(self, other):
        return self.link == other.link    
