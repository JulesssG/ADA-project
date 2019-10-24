# Amazon food data analysis

## Abstract
Nowadays Amazon's popularity grows increasingly and becomes massive, it is ubiquitous in our era of cloud services and big data. Amazon has plenty of servers, buys big succesful companies such as Twitch, its CEO is the wealthiest man of our generation. But its underpinning is of course the website Amazon.

On Amazon you can buy almost any product nowadays, you can see users's ratings of any product, this of course changes the consumer's behavior. However, how much of an impact does it have on the consumer? Are there groups of consumers, groups that always buy the same stuff? On Amazon you can also see what related products people tend to look at after looking at the one you're looking at. Again, this most likely has an impact on sales, but is it possible to quantify it?

## Research questions
A list of research questions you would like to address during the project.

We can study different trends and their popularity at different levels:

Product level :
- Price ranges
- Brands
- Ranking in one category
Review level : 
- Helpful or not
- Reviewer
- Review text (see below)

With PCA we can maybe study different questions using the review texts:
- Are there any trends in the comments
- Many people buy gifts on Amazon maybe we can extract some information about it:
	- To who do people buy gifts (husband, wife, children, ...)
	- Are some categories more gifted than others and to the same group of people 

We can as well use the "also bought" and "also viewed" list in the metadata
-Try to see how the recommender system works: is there a correlation between the prices, the ranking, the vendor, the product type?


## Dataset
Our Dataset is Amazon product data from Amazon which contains information about the rating of the product. Especially, it has information about the review from the user who did it to the product.  We are planning to extract as a first step insights about the review per year. We expect to see the number of review is increasing during the years and after we will focus on the rating of the review. We will try to classify the users depend on the behaviors. We expect to have some users who is actually bot (and always do bad rating) and we expect to have some users who always do rating depend on the exist rating of this product. Also, we will try to find correlation between time and grade of review. Example, maybe during the night period the majority of the coment are bad and during the morning period the majority of the comment are good.

List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

## A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

## Questions for TAa
Add here some questions you have for us, in general or project-specific.
