# Amazon food data analysis

## Abstract
Nowadays Amazon's popularity grows increasingly and becomes massive, it is ubiquitous in our era of cloud services and big data. Amazon has plenty of servers, buys big succesful companies such as Twitch, its CEO is the wealthiest man of our generation. But its underpinning is of course the website Amazon, thus making it a very interesting data provider.

On Amazon you can buy almost any product nowadays, including food. Indeed you can buy your groceries on Amazon and you can see users's ratings of the food item you're looking at. This of course changes the consumer's behavior. However, how much of an impact does it have on the consumer? Does Amazon favor some diets over others? Are users's consumption affected over time or do they keep buying the same stuff? On Amazon you can also see what related products people tend to look at after looking at the one you're looking at. Again, this most likely has an impact on sales, but is it possible to quantify it?

## Research questions
The key idea would be to see how user's consumption behaves over time: how it follows trends, how seasons affect it or even how the time passed on Amazon influences it. And since our purpose is to explore how topics such as vegetarianism, veganism, organic food, holiday food, seasonal food and healthy food are characterised on Amazon and how the latter directly or indirectly influences buyers towards the formers we will ask us:
- What buying habits do users have ?
- How does the recommender system (`also bought` and `also viewed` fields) work?
  - Does it favor similar items or popular items?
- With PCA we can ask ourselves if there are any trends in the comments.
- Do people's behavior change over time as they use Amazon? :
  - Do they buy more?
  - Do they change their consumption (more healthy, more organic)?
- How did buying habits change throughout the years? Since veganism is a recent topic, how does it translate through the Amazon dataset?
- How do buying habits change throughout the year ? How do seasons affect it ? Do people tend to eat healthier at the dawn of the summer ? Do holidays such as thanksgiving have an influence ?

On the other hand there will be more general questions that will help us to understand how the data behaves :
- How often do people buy groceries online?
- What does the products' price distribution tell us? (At brand, product or category level)
- What is the correlation between prices, brands or sales rank?

## Dataset
Our dataset is _Amazon product data 2018_ (https://nijianmo.github.io/amazon/index.html, i.e. one of the proposed dataset but updated), more specifically the "Grocery and Gourmet Food", which contains around 5'074'160 millions of reviews from May 1996 to October 2018 along with the food items's metadata.

The metadata contains basic information like the product id, but also more complex information like a list of `also bought` and `also viewed` products that points to products related to the original one, on two different levels. It also contains the price, the brand and the categories for example.

Concerning the actual reviews in the dataset, they contain all relevant information for a review: reviewer, time of the review, rating on the review, comment of the review.

However, we thus don't directly have access to what users bought. So we must be careful as we can't analyze what people purchased but only what they are reviewing. Also, the metadata is per item so it's not personalized by users.

## A list of internal milestones up until project milestone 2
- For 3rd November: Send request to have the metadata + reviews data from the 2018 dataset, and decide, depending on the answer, if we use the 2014 dataset or the subset of the 2018 data that's available to download.

## Questions for TAs
- The dataset linked on the google spreadsheet has data from May 1996 - July 2014 but there is an updated one that goes until 2018 (https://nijianmo.github.io/amazon/index.html) and the number of reviews goes from 150'000 to 5'000'000. It seems like this extended dataset would be much better for our analysis. We would prefer using it if we can get it, and since it should simply be the same dataset but much bigger, we think the TAs could still help us. Can we use this dataset instead?
- Does the whole code need to be done for Milestone 2? With visualizations and analysis? Because it seems weird to have 1 month to do the **WHOLE** analysis and 1 month to write a 4 page report from that analysis. Can we still do further analysis after milestone 2? fancier visualization? and produce further results with the analysis? We don't really understand what exactly needs to be done for Milestone 2.
