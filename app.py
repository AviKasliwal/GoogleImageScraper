from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import os
from scraperLayer.scraperLayer import Scraper
from businessLayer.businessLayer import BusinessLayer
from flask import request

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/displayImages')
@cross_origin()
def displayImages():
    allImages = os.listdir('static')
    print(allImages)
    try:
        if (len(allImages) > 0):
            return render_template('displayImages.html', allImages = allImages)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found :( , error : ", e)
        return "Try a different search term"


@app.route('/searchImages', methods = ['GET', 'POST'])
def searchImages():
    if request.method == 'POST':
        searchKey = request.form['searchKey']
        print("\n\n\n\n\n")
        print(searchKey, len(searchKey)) # comment later [debug statement]

    scraperUtil = BusinessLayer()
    scraper = Scraper() # Logic layer
    allImages = os.listdir('static') 
    scraper.delete_previous_imgs(allImages)

    imageName = searchKey.split()
    imageName = '+'.join(imageName)

    header = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }

    listImages = scraperUtil.downloadImages(keyword = searchKey, header = header)

    print(listImages) # comment later [debug statement]

    return displayImages()

if __name__ == "__main__":
    app.run(debug = True)