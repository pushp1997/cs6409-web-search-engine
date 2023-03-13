import os
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    start_urls = ["https://en.wikipedia.org/wiki/Cork_(city)"]

    def parse(self, response):
        # extract text from paragraphs of the wikipedia page
        text = " ".join(response.xpath("//p//text()").getall())

        # extract links from these texts to scrape the associated pages
        links = response.xpath("//a/@href").getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link), callback=self.parse_link, meta={"text": text}
            )

    def parse_link(self, response):
        # extract text from paragraphs
        text = " ".join(response.xpath("//p//text()").getall())

        # save text to file
        directory = "scraped_documents"
        os.makedirs(directory, exist_ok=True)
        filename = response.url.split("/")[-1] + ".txt"
        with open(os.path.join(directory, filename), "w") as f:
            f.write(text)
