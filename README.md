# China_A_shares_industry_analysis
**Methods employed:**
- K-Means clustering
- PCA
- web scraping
- word segmentation, wordcloud
- word2vec

**1. business-based industry classification**
- path: 
  - **/industries_clustering/revenue-based-classification.ipynb**
- description: This code classify first-class & second-class industries in China's A share market.
  - **Input file** `主营构成.xlsx`: main businesses listed companies assert in their 2020 annual reports
  - use the best Python *Chinese word segmentation module* `jieba` to break down listed companies' business assertions
  - count word frequencies and calculate cosine similarity matrix of listed companies
  - employ `Word2Vec` to generate an aggregated vector which implies its business field for each listed company
  - K-Means clustering: Mini-batch K-Means; select the optimal number of clusters based on **elbow rules** and **silhouette_scores**
  - **Output file** `industries_clustering_1_tier_classification_elbow.xlsx` `industries_clustering_1_tier_classification_silhouette_score.xlsx` `industries_clustering_2_tier_classification_elbow.xlsx` `industries_clustering_2_tier_classification_silhouette_score.xlsx`

**3. industry policy scraping and wordcloud**
- path: 
  - **/webscraping+wordcloud/industry_policy_scraping.py**
  - **/webscraping+wordcloud/industry_policy_wordcloud.py**
- description: This code first scrape <a href='http://zhengce.chinabaogao.com/'>policies of 28 different industries</a> from web and identify the most popular words mentioned by policymakers via `wordcloud`. 
