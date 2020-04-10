import pandas as pd


class DataStructure:

    def __init__(self, source, author, title, description,url, published_at, url_to_image, content):
        """
        Single news instance

        :param source:str source of the news
        :param author:str author of the  news
        :param title:str author of the title
        :param description:str description of the news
        :param url:str url of the news
        :param published_at:datetime  publish date of the news
        :param url_to_image:str url to the image of the news
        :param content:str content of the news
        """
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.published_at=published_at
        self.url_to_image= url_to_image
        self.content = content




