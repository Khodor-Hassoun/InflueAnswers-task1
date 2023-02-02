from pathlib import Path

import scrapy


class ChatsSpider(scrapy.Spider):
    name = "chats"
    allowed_domains = ['chatlogs.planetrdf.com']
    start_urls = ["https://chatlogs.planetrdf.com/swig/2014-06-01.html"]

    def parse(self, response):
        chatContainer = response.xpath("//div[@class='log']/p")
        chatDate = response.xpath("//html/body/p[3]/strong/text()").get()
        for paragraph in chatContainer:
            time = paragraph.xpath("./span[@class='time']/a/text()").get()
            user = paragraph.xpath("./span[2]/text()").get()
            comment = paragraph.xpath("./span[3]/text()").get()
            if(isinstance(user, str)):
                user = user[1: -1]

            yield {
                "chat_date": chatDate,
                "time": time,
                "user": user,
                "comment": comment
            }
