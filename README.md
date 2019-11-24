# Amazon food data analysis

## Abstract
Nowadays Amazon's popularity grows increasingly and becomes massive, it is ubiquitous in our era of cloud services and big data. Amazon has plenty of servers, buys big succesful companies such as Twitch, its CEO is the wealthiest man of our generation. But its underpinning is of course the website Amazon, thus making it a very interesting data provider.

On Amazon you can buy almost any product nowadays, including food. Indeed you can buy your groceries on Amazon and you can see users's ratings of the food item you're looking at. This of course changes the consumer's behavior. However, how much of an impact does it have on the consumer? Does Amazon favor some diets over others? Are users's consumption affected over time or do they keep buying the same stuff? On Amazon you can also see what related products people tend to look at after looking at the one you're looking at. Again, this most likely has an impact on sales, but is it possible to quantify it?

## Research questions
The key idea would be to see how user's consumption behaves over time: how it follows trends, how seasons affect it or even how the time passed on Amazon influences it. And since our purpose is to explore how topics such as vegetarianism, veganism, organic food, holiday food, seasonal food and healthy food are characterised on Amazon and how the latter directly or indirectly influences buyers towards the formers we will ask us:
- How is the data distributed? In order to answer this question we will analyse the following distributions : number of stars per review, number of upvotes per review, review length, number of review per year and per month etc.
- How did buying habits change throughout the years? Since veganism is a recent topic, how does it translate through the Amazon dataset ?
- How do buying habits change throughout the year ? Do holidays such as Thanksgiving, Christmas or Halloween have an influence ? Are there feasts, such as Mother's day or Valentine's Day that stick out ?
- Do special events such as the end of the world in 2012 or the release of a movie give rise to some products ?

## Dataset
Our dataset is _Amazon product data 2018_ (https://nijianmo.github.io/amazon/index.html, i.e. one of the proposed dataset but updated), more specifically the "Grocery and Gourmet Food", which contains around 5'074'160 millions of reviews from May 1996 to October 2018 along with the food items's metadata.

The metadata contains basic information like the product id, but also more complex information like a list of `also bought` and `also viewed` products that points to products related to the original one, on two different levels. It also contains the price, the brand and the categories for example.

Concerning the actual reviews in the dataset, they contain all relevant information for a review: reviewer, time of the review, rating on the review, comment of the review.

However, we thus don't directly have access to what users bought. So we must be careful as we can't analyze what people purchased but only what they are reviewing. Also, the metadata is per item so it's not personalized by users.

## Questions for TAs
