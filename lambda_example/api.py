from flask import Flask
from newspaper import Article

app = Flask(__name__)

@app.route('/articles/')
def get_articles():
    url = 'http://pythondata.com/stock-market-forecasting-with-prophet/'
    article_content = Article(url, language='en')
    article_content.download()
    article_content.parse()
    print article_content.text[:150]
    return article_content.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)