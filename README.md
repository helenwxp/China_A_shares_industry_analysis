# China_A_shares_industry_analysis
**Methods employed:**
- K-Means clustering
- PCA
- t-SNE
- web scraping
- word segmentation, wordcloud
- word2vec
---

**1. business-based industry classification**
- path: 
  - **/industries_clustering/revenue-based-classification.ipynb**
- description: This code classify first-class & second-class industries in China's A share market.
  - **Input file** `主营构成.xlsx`: main businesses listed companies assert in their 2020 annual reports
  - use the best Python *Chinese word segmentation module* `jieba` to break down listed companies' business assertions
  - count word frequencies and calculate cosine similarity matrix of listed companies
  - employ `Word2Vec` to generate an aggregated vector which implies its business field for each listed company
  - K-Means clustering: Mini-batch K-Means; select the optimal number of clusters based on **elbow rules** and **silhouette_scores**
  - **Output file**
  `industries_clustering_1_tier_classification_elbow.xlsx`
  `industries_clustering_1_tier_classification_silhouette_score.xlsx`
  `industries_clustering_2_tier_classification_elbow.xlsx`
  `industries_clustering_2_tier_classification_silhouette_score.xlsx`

<br>

**2. volatility-based cluster (PCA & t-SNE)**
- path:
  - **/volatility_based_cluster_pca_tsne/t-SNE-PCA-2021-definedindustry.ipynb**
- description: This code does hierarchical cluster analysis on the monthly return rate and return rate volalitity from 2021.01 to 2021.09 of all A shares companies in China.
  - **input file**: `波动率2021.xlsx`; `industries_clustering_1_tier_classification_silhouette_score.xlsx`; `return_rate.xlsx`
  - use the Python PCA analysis and t-SNE analysis package to carry out the cluster analysis
  - use our ***self-defined*** first-tier industry classification for robustness
  - visualize cluster result 
- path:
  - **/volatility_based_cluster_pca_tsne/Standard-Industry-Classification-Analysis.ipynb**
  - **/volatility_based_cluster_pca_tsne/Standard-Industry-Classification-Analysis.py**
- description: This code does hierarchical cluster analysis on the monthly return rate and return rate volalitity from 2021.01 to 2021.09 of all A shares companies in China.
  - **input file**: `波动率2021.xlsx`; `industry_classification.xlsx`; `return_rate.xlsx`
  - use the Python PCA analysis and t-SNE analysis package to carry out the cluster analysis
  - use ***standard*** first-tier industry classification for robustness
  - visualize cluster result 

<br>

**3. industry policy scraping and wordcloud**
- path: 
  - **/webscraping+wordcloud/industry_policy_scraping.py**
  - **/webscraping+wordcloud/industry_policy_wordcloud.py**
- description: This code first scrape <a href='http://zhengce.chinabaogao.com/'>policies of 28 different industries</a> from web and identify the most popular words mentioned by policymakers via `wordcloud`. 


![sample wordcloud](/webscraping+wordcloud/imgs/wc/电力.jpg)
