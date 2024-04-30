import scrapy

from scrapy.http import Response


class PythonDjinniSpider(scrapy.Spider):
    name = "python_djinni"
    allowed_domains = ["djinni.co/jobs"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs) -> None:
        pass
