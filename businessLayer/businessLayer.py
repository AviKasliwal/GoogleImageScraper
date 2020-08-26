# Business Logics here

from scraperLayer.scraperLayer import Scraper

class BusinessLayer:
    keyword = ""
    fileLocation = ""
    imageName = ""
    header = ""

    def downloadImages(self, keyword, header):
        scraper = Scraper
        url = scraper.createUrl(keyword)
        rawHtml = scraper.scrap_html_data(url, header)
        imgUrlList = scraper.getImgUrlList(rawHtml)
        masterList = scraper.downloadImgFromUrl(imgUrlList, keyword, header)

        return masterList