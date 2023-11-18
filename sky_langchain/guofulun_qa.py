from sky_langchain import spider_qa

url = "https://www.99csw.com/book/8735/index.htm"
domain = "https://www.99csw.com/book/8735"
name = "guofulun"
spider_qa.scraper(name=name, url=url, domain=domain)
