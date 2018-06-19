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

    def __cmp__(self, other):  
        return cmp(self.articleId, other.articleId)  