from pathlib import Path
from datetime import datetime
import scrapy


class ChatsSpider(scrapy.Spider):
    name = "chats"
    allowed_domains = ['chatlogs.planetrdf.com']
    start_urls = ["https://chatlogs.planetrdf.com/swig/2014-06-01.html",
                  "https://chatlogs.planetrdf.com/swig/2014-06-02.html", "https://chatlogs.planetrdf.com/swig/2014-06-03.html",
                  "https://chatlogs.planetrdf.com/swig/2014-06-04.html", "https://chatlogs.planetrdf.com/swig/2014-06-05.html"
                  ]

    def parse(self, response):
        chatContainer = response.xpath("//div[@class='log']/p")
        chatDate = response.xpath("//html/body/p[3]/strong/text()").get()
        for paragraph in chatContainer:
            time = paragraph.xpath("./span[@class='time']/a/text()").get()
            user = paragraph.xpath("./span[2]/text()").get()
            comment = paragraph.xpath("./span[3]/text()").get()
            if(isinstance(user, str)):
                user = user[1: -1]
            timeObj = datetime.strptime(time, "%H:%M:%S").time()
            yield {
                "chat_date": chatDate,
                "chat_hour": timeObj.hour,
                "chat_minute": timeObj.minute,
                "user": user,
                "chat_message": comment
            }
