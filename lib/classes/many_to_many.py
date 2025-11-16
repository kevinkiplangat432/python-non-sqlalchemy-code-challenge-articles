
class Article:
    all =[]
    def __init__(self, author, magazine, title):
        #  @kelvin based on my understanding if i want to use the setters in init method i have to first initialize the private attributes to None. hence my assumption is "self.title = title" in init method will call the title setter and is not an initialisation of the attribute.

        self._author = None
        self._magazine =None
        self._title = None
        self.author = author 
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if self._title is not None: #if already has a title no change should be made.
            return
        if isinstance(value,str) and 5 <= len(value) <= 50: # title be string 5-50 chars
            self._title =value
        else:
             print(f"Invalid title '{value}', must be string 5–50 chars") 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author): # this will ensure only instances of author is assigned to author attribute
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine): # same case to the one above
            self._magazine = value

class Author:
    def __init__(self, name):
        self._name =None # this will alloe me to  determine if a name has already been assigned.since name cannot change after creation.
        self.name = name

    @property
    def name (self):
        return self._name
    
    # setter
    @name.setter
    def name(self, value):
        # name cannot change after i craete it
        if self._name is not None:
            return
        
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        
    #now to thge relationship between this classes
    def articles(self):
        #interate through all articles.
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        #give me magazines from this author's articles.
        return list({article.magazine for article in self.articles()})



    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str): # ensure magazine is an instance of Magazine and title is string
            return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        # here i use set comprehension to avoid duplicate categories wrapped in list to return list
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    all= []   # will manage all magazines and this is a class variable 

    def __init__(self, name, category):
        #same assumption as above or understanding it is playing with my mind.all i know is that to use the setters in init method i have to first initialize the private attributes to None.
        self._name =None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

        else:
            print(f"print Invalid name '{value}', must be a string 2-16 chars")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print(f"Invalid category '{value}', must be string > 0 chars") 
            

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})
    



    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = []
        for author in self.contributors():  
            count = len([article for article in self.articles() if article.author == author])
            if count > 2:
                authors.append(author)

        return authors if authors else None
    
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
    
        return max(cls.all, key=lambda mag: len(mag.articles()))