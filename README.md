# 🎓 My Master Project

## Overview

My master project is titled **"Sentiment Analysis on Skincare Product Reviews in Amazon Platform"**.  
It was completed as part of my Master's degree program at **Universiti Teknologi Malaysia (UTM)** under the **Faculty of Computing**.  

The project focuses on analyzing how consumers from two cosmetics brands perceive and make choices regarding cosmetics based on factors like **price** and **brand reputation**.  
The objective is to help consumers make more **informed purchasing decisions** by understanding general sentiment trends.  

This includes a comparison between **local, budget-friendly skincare products** and **well-known, expensive products**, using **sentiment analysis techniques** to categorize and indicate the overall consumer sentiment reflected in product reviews.

---

# 🛒 Amazon Product Review Scraper

This is a **Python script** for scraping product reviews from Amazon.

## ✨ Project Description

This project collects and analyzes product reviews on Amazon to gain insights into **customer feedback**, **product ratings**, and **trends**.  
It serves as a **web scraping tool** that allows automated retrieval and storage of Amazon product reviews in a **CSV** file for further sentiment analysis.  

By providing a **product name** and **ID**, users can easily scrape reviews, which are then processed and cleaned for downstream tasks like **Natural Language Processing (NLP)** and **machine learning modeling**.

---

# 🔍 Project Workflow

## 1. Data Collection
- Scrape skincare product reviews from the Amazon platform using the web scraper.
- Target products from two selected brands (one budget-friendly, one premium).

## 2. Data Preprocessing
- Remove HTML tags, special characters, and irrelevant information.
- Tokenize reviews and clean the text data.
- Handle imbalanced datasets if necessary (e.g., using undersampling or oversampling).

## 3. Sentiment Analysis
Implemented multiple techniques to assess sentiment polarity:

- **VADER (Valence Aware Dictionary for Sentiment Reasoning)**:
  - A rule-based model ideal for social media texts, short sentences, and customer reviews.
  - VADER scores texts based on the positivity, neutrality, and negativity of words.

- **TextBlob**:
  - A simple NLP tool that calculates the polarity (sentiment score between -1 to 1) and subjectivity of a sentence.
  - Helpful for quick baseline sentiment analysis.

Each review was assigned a sentiment label:
- **Positive** (Polarity > 0)
- **Neutral** (Polarity = 0)
- **Negative** (Polarity < 0)

## 4. Machine Learning Models for Sentiment Classification
To improve classification accuracy beyond rule-based methods, two supervised ML models were trained:

- **Support Vector Machine (SVM)**:
  - A powerful algorithm for text classification tasks.
  - Finds the optimal hyperplane that separates positive and negative sentiment classes.
  - **Kernel**: Linear
  - **Preprocessing**: TF-IDF Vectorization

- **Multinomial Naive Bayes (MNB)**:
  - A probabilistic classifier based on Bayes' theorem, particularly effective for text data.
  - Assumes features (words) are conditionally independent given the sentiment label.
  - **Preprocessing**: TF-IDF and Count Vectorization

Both models were evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

---

# 🛠 Tech Stack

- **Languages**: Python

- **Libraries**:
  - `BeautifulSoup4` (Web scraping)
  - `requests` (HTTP requests)
  - `pandas` (Data manipulation)
  - `nltk` (Text processing)
  - `TextBlob` (Sentiment scoring)
  - `VADER` (Sentiment analysis)
  - `scikit-learn` (Machine learning: SVM, MNB, evaluation metrics)
  - `matplotlib` and `seaborn` (Visualization)

---

# 📊 Key Insights

- Budget-friendly brands showed more polarized sentiment compared to premium brands.
- Premium brands maintained a more consistently positive sentiment, although value-for-money issues were frequently mentioned.
- Price and brand perception significantly influence consumer emotions and loyalty.
- VADER and TextBlob provided good baseline sentiment detection, but SVM achieved higher accuracy in complex review classification tasks.

---

# 🔮 Future Enhancements

- Apply deep learning models (e.g., **LSTM**, **BERT**) for more nuanced sentiment understanding.
- Perform **aspect-based sentiment analysis** to analyze specific features (e.g., packaging, ingredients, effectiveness).
- Create an interactive **dashboard** using **Streamlit** or **Tableau** for dynamic visualization and reporting.
- Expand scraping to more brands and geographical regions to understand cultural variations in sentiment.

---

# 📑 References

- Amazon Product Reviews Dataset (Scraped)
- Research papers on Sentiment Analysis Techniques
- Natural Language Processing with Python (NLTK)
- VADER Sentiment Analysis Tool Documentation
- TextBlob Documentation
- Support Vector Machine and Naive Bayes Classification Algorithms

---
