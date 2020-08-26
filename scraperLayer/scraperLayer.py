# Logic Layer [of the scraper]

from bs4 import BeautifulSoup as bs
import os
import json
from urllib import request, parse, error
from urllib.request import urlretrieve

class Scraper:

    # Creating url for the search term
    def createUrl(keyword):
        keyword = keyword.split()
        keyword = "+".join(keyword)
        url = "https://www.picsearch.com/index.cgi?q=" + keyword
        return url

    # Function to get the raw HTML
    def scrap_html_data(url, header):
        req = request.Request(url, headers = header)
        response = request.urlopen(req)
        responseData = response.read()
        rawHtml = bs(responseData, 'html')
        return rawHtml

    def getImgUrlList(rawHtml):
        urlList = []
        imgs = rawHtml.find_all('img', class_ = 'thumbnail')
        for img in imgs:
            src = img['src']
            src = 'https:' + src
            src = src.replace('&amp;', '&')
            print(src)
            urlList.append(src)
        print(urlList)
        print("Total number of images : ", len(urlList))
        return urlList

    def downloadImgFromUrl(urlList, imageName, header):
        masterList = []
        count = 0
        imageCounter = 0
        for i, img in enumerate(urlList):
            try:
                if count > 4:
                    break
                else:
                    count += 1
                req = request.Request(img, headers = header)
                try:
                    request.urlretrieve(img, "./static/" + imageName + str(imageCounter) + ".jpg")
                    imageCounter += 1 
                except Exception as e:
                    print("Could not save the img, error : ", e)
                    imageCounter += 1
                respData = request.urlopen(req)
                rawImg = respData.read()

                masterList.append(rawImg)

            except Exception as e:
                print("Could not load : ", img)
                print(e)
                count += 1
        return masterList

    def delete_previous_imgs(self, allImages):
        for self.image in allImages:
            try:
                os.remove("./static/" + self.image)
            except Exception as e:
                print("Error Deleting : ", e)
        return 0
            
