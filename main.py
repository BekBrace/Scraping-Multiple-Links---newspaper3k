#  Requested by Solomon Aka
# 'Newspaper Module to scrap multiple URLS'


from newspaper import Article
import newspaper

URLS = ['https://www.latimes.com/world-nation/story/2020-09-20/coronavirus-aerosol-airborne-spread',
        'https://edition.cnn.com/2020/12/22/asia/hong-kong-pirates-eli-boggs-intl-hnk-dst/index.html'
        ]


class MainSource(newspaper.Source):
    def __init__(self, articleURL):
        super(MainSource, self).__init__('http://localhost')
        self.articles = [newspaper.Article(url=articleURL)]


sources = [MainSource(articleURL=u) for u in URLS]

newspaper.news_pool.set(sources)
newspaper.news_pool.join()

for i in sources:
    i.articles[0].download()
    i.articles[0].parse()
    print('Title:', i.articles[0].title)
    print('Author:', i.articles[0].authors)
    # And you can continue scraping whatever attribute you choose
