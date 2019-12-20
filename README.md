# Impact of events and trends on users and products

[Data Story](https://gorzen.github.io/Los-Moussaka-Data-Story/)


[milestone 3](https://github.com/Gorzen/Los-Moussaka-ADA/blob/master/milestone_3.ipynb)

## Abstract
Nowadays Amazon's popularity grows increasingly and becomes massive, it is ubiquitous in our era of cloud services and big data. Amazon has plenty of servers, buys big succesful companies such as Twitch, its CEO is the wealthiest man of our generation. But its underpinning is of course the website Amazon, thus making it a very interesting data provider.

On Amazon you can buy almost any product nowadays, including food. Indeed you can buy your groceries on Amazon and you can see users's ratings of the food item you're looking at. This of course changes the consumer's behavior. However, how much of an impact does it have on the consumer? In particular we know that people tend to be deeply affected by group effects, such as festive events. Indeed, Christmas or Valentine's day have a big impact on sales, is it possible to quantify it using reviews? There also are food trends such as veganism or specific diets, can we also observe an increase here?

## Research questions
The key idea would be to see how user's consumption behaves over time: how it follows trends, how seasons or events affect it. Thus, our purpose is to explore how topics, such as vegetarianism and veganism, and events are characterised on Amazon. To do this we will ask us: 
- How do buying habits change throughout the year? Do holidays such as Thanksgiving, Christmas or Halloween have an influence? Are there feasts, such as Mother's day or Valentine's Day that stick out ?
- How events impact the popularity of products? Can we get insights about what people feel and desire during an event from the type of products that are popular?
- How did buying habits change throughout the years? Since vegetarianism and veganism get more interest these days, how does it translate through the Amazon dataset ?
- Do special events such as the end of the world in 2012 or the release of a movie give rise to some products ?

## Dataset
Our dataset is _Amazon product data 2018_ (https://nijianmo.github.io/amazon/index.html, i.e. one of the proposed dataset but updated), more specifically the "Grocery and Gourmet Food", which contains around 5'074'160 millions of reviews from May 1996 to October 2018 along with the food items's metadata. Reviews in the dataset are from USA.

The metadata contains basic information like the product id, but also more complex information like a list of `also bought` and `also viewed` products that points to products related to the original one, on two different levels. It also contains the price, the brand and the categories for example.

Concerning the actual reviews in the dataset, they contain all relevant information for a review: reviewer, time of the review, rating on the review, comment of the review.

However, we thus don't directly have access to what users bought. So we must be careful as we can't analyze what people purchased but only what they are reviewing. Also, the metadata is per item so it's not personalized by users.

## Contributions
- Christina Mantonanaki:
  - First hands on with the dataset (pre-processing and experiment to extract topics using matching words)
  - Tries with Word2Vec on examples
  - Start of the website
  - Start of poster design
- Florian Ravasi: 
  - Event impact with bayesian structural time series
  - Word frequencies to capture events coding and analysis
  - Word2Vec coding and training on our dataset
  - NLTK pipeline and lemmatization
- Jules Gottraux:
  - Popular products extraction from time series
  - NLTK pipeline and lemmatization
  - Experiement with LDA to extract topics
  - Analysis and description of word frequency analysis
  - Analysis and extraction of results from core analysis
  - Sanitization of datasets (pre-processing)
- Lucien Iseli:
  - Basic structure of repo and notebook (basic functions etc ...)
  - Presentation of dataset and pre-processing
  - Feature distributions analysis
  - Food trends and countries
  - Analysis and extraction of results from core analysis and anomalies
  - Visualizations and plots
  - Website
