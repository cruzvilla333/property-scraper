import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            yield {
                'name': book.css('a::text').get(),
                'price': book.css('.price_color::text').get(),
                'url': book.css('h3 a').attrib['href']
            }

        next_page = response.css('li.next a ::attr(href)').get()
        
        if(next_page):
            next_page_url = 'https://books.toscrape.com/catalogue/'
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/'
            
            next_page_url = next_page_url + next_page
            yield response.follow(next_page_url, callback = self.parse)