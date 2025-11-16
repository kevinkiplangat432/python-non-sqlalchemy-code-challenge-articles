class Article:
    all_articles =[]
    def __init__(self, author, magazine, title):
        self.author = author 
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, "_title"): #if already has a title no change should be made.
            return
        if isinstance(value,str) and 5 <= len(value) <= 50:
            self._title =value
        else:
             print(f"Invalid title '{value}', must be string 5–50 chars") 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
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
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    all_magazines = []   # will manage all magazines and this is a class variable 

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 10:
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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass