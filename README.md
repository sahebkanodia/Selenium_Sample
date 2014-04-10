Selenium_Sample
===============

These codes are my sample work which I did during my internship. Basic idea is to perform a regression test using Selenium Webdriver on the functionality of Wishpicker.com. Please see `deploy.sh` for sequentiality[is that a word?].


==============================================
Tests performed on www[dot]wishpicker[dot]com

Redirect - Subscribe Test
---------------------

	This test is performed for all the three Buy Now Links of a product; 3 products for each partner website.
	This test checks the Subscribe option present inside Email Box in the redirect page. Also checks the Product Name, Price with the partner site's product page.

	Estimated Runtime : 2 Hours 30 Minutes.

Procedure : 
	
	Step 1:
	Run `main.py`

	First, search for the respective partner website. Then randomly select a product from the result and click on it. When Quickview opens, click on the Buy Now link. Then a test is applied to check whether "www[dot]wishpicker[dot]com/redirect/" is present in the redirect page, if not present test fails. Then an incorrect email is entered in the email box and subscribe button is clicked. A sleep of 2 secs is timed and the url is checked for whether the page has navigated or not. If yes, test fails. If not, a correct email is entered and subscribe button is clicked and waits for the page to redirect to partner website. On successful redirection to partner website, we check the response code from the page.

	Then from the Quickview, we navigate to the product page, fetch the Product name and Price displayed and save it along with product page link in `data.jl` file. Then the process as above is followed till redirection to partner website is completed. Now, we fetch the link of the partner site's product page link and check the response code. Also save the partner site's link in `data.jl` file for scrapy to crawl later.

	Then we shortlist the product and perform the redirection as usual and check for the response code of the partner site on successful redirection.

	Step 2:

	Now crawl the parner site's links one by one accordingly. The links are extracted from the 'data.jl' file. The crawled data is saved in a file called `items.jl`. Now run `main_final.py`, This performs a final test which checks the data gathered from wishpicker and partner website. For every product, there are two test cases. One for Price and the other for Product Name. The fails if match does not occur.
