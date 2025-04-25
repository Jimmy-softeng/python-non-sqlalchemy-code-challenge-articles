class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters")

        self._title = title
        self.author = author
        self.magazine = magazine
        Article._all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        if hasattr(self, '_name'):
            raise Exception("Name is immutable and cannot be changed")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [a for a in Article._all if a.author == self]

    def magazines(self):
        return list(set(a.magazine for a in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(mag.category for mag in self.magazines()))


class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name  # will go through setter
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [a for a in Article._all if a.magazine == self]

    def contributors(self):
        return list(set(a.author for a in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        author_count = {}
        for a in self.articles():
            author_count[a.author] = author_count.get(a.author, 0) + 1
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article._all:
            return None
        return max(cls._all, key=lambda mag: len([a for a in Article._all if a.magazine == mag]), default=None)
