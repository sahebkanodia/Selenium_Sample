export PATH=$PATH:/usr/local/bin
cat /dev/null > items.jl
cat /dev/null > data.jl
cat dev/null > redirectPage_subscribe.html
python main.py
killall Xvfb
killall firefox
python cleandata.py
scrapy crawl Flipkart
scrapy crawl shopin1
scrapy crawl Happily
scrapy crawl Healthkart
scrapy crawl Dezains
scrapy crawl Fnp
scrapy crawl Vmate
scrapy crawl Exlives
scrapy crawl Dgifts
scrapy crawl Babyoye
scrapy crawl Purp
scrapy crawl Fabf
scrapy crawl Zansaar
scrapy crawl Shop19
scrapy crawl Engrave
scrapy crawl Carat
scrapy crawl Todu
scrapy crawl Hit
scrapy crawl Limeroad
scrapy crawl Perfico
python main_final.py
