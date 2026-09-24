# 🍽️ Food Review Analyzer

An **NLP-based Food Review Analyzer** that analyzes restaurant reviews and classifies them into **Positive, Negative, and Neutral** sentiments. The project uses **Python, Natural Language Processing, Machine Learning, and Flutter** to provide an end-to-end solution for analyzing customer feedback.

---

## 📌 Project Overview

Customer reviews contain valuable information about food quality, service, restaurant experience, and customer satisfaction. However, manually analyzing thousands of reviews is time-consuming.

The **Food Review Analyzer** uses Natural Language Processing (NLP) techniques to process customer reviews, identify important textual patterns, and classify the sentiment of each review.

The project follows an end-to-end workflow:

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning & Preprocessing
     ↓
Exploratory Data Analysis
     ↓
NLP Processing
     ↓
Text Vectorization
     ↓
Sentiment Classification
     ↓
Model Evaluation
     ↓
Flutter Application
```

---

## 🎯 Objectives

The main objectives of this project are:

* Analyze customer food and restaurant reviews.
* Clean and preprocess textual review data.
* Apply Natural Language Processing techniques.
* Identify important words and patterns in reviews.
* Classify reviews as Positive, Negative, or Neutral.
* Train and evaluate sentiment classification models.
* Provide an easy-to-use interface through a Flutter application.
* Generate useful insights from customer feedback.

---

## ✨ Key Features

* 📊 Exploratory Data Analysis of restaurant reviews
* 🧹 Text cleaning and preprocessing
* 🔤 Tokenization and stopword removal
* 📝 NLP-based text analysis
* 📈 Sentiment distribution analysis
* 🔎 Frequently used word analysis
* 🤖 Sentiment classification
* 📊 Model performance evaluation
* 📱 Flutter-based user interface
* 💬 User review sentiment prediction
* 📋 Clear and understandable sentiment results

---

## 🛠️ Technologies Used

### Programming Languages

* Python
* Dart

### Data Analysis & NLP

* Pandas
* NumPy
* NLTK
* Scikit-learn

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Bag-of-Words
* TF-IDF
* Classification Algorithms

### Application Development

* Flutter
* Dart

### Development Tools

* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
food-review-analyzer/
│
├── data/
│   └── yelp_sentiment_master_dataset.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_nlp_eda.ipynb
│   └── 04_*.ipynb
│
├── scripts/
│   └── ...
│
├── models/
│   └── ...
│
├── flutter_app/
│   ├── lib/
│   ├── android/
│   ├── ios/
│   ├── web/
│   └── pubspec.yaml
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Dataset

The project uses a restaurant review dataset containing customer reviews and business information.

### Dataset File

```text
yelp_sentiment_master_dataset.csv
```

### Dataset Size

* **Rows:** 14,351
* **Columns:** 10

### Main Columns

| Column           | Description                        |
| ---------------- | ---------------------------------- |
| `stars_review`   | Star rating given by the reviewer  |
| `text`           | Customer review text               |
| `date`           | Review date                        |
| `name`           | Restaurant/business name           |
| `categories`     | Business categories                |
| `city`           | City of the business               |
| `state`          | State of the business              |
| `stars_business` | Average business rating            |
| `review_count`   | Number of reviews for the business |
| `rating_review`  | Sentiment label                    |

---

# 📈 Sentiment Distribution

The reviews are classified into three sentiment categories:

| Sentiment |      Count | Percentage |
| --------- | ---------: | ---------: |
| Positive  |      9,857 |     68.69% |
| Negative  |      2,699 |     18.81% |
| Neutral   |      1,795 |     12.51% |
| **Total** | **14,351** |   **100%** |

The dataset contains a higher proportion of positive reviews compared with negative and neutral reviews.

---

# ⭐ Star Rating Distribution

The review ratings are distributed as follows:

| Stars | Reviews | Percentage |
| ----: | ------: | ---------: |
|     1 |   1,422 |      9.91% |
|     2 |   1,277 |      8.90% |
|     3 |   1,795 |     12.51% |
|     4 |   3,949 |     27.52% |
|     5 |   5,908 |     41.17% |

The sentiment labels are associated with star ratings as follows:

```text
1 Star → Negative
2 Stars → Negative
3 Stars → Neutral
4 Stars → Positive
5 Stars → Positive
```

---

# 🧹 Data Preprocessing

Text preprocessing is an important part of the project because raw customer reviews contain punctuation, unnecessary words, and other textual noise.

The preprocessing pipeline includes:

```text
Raw Review
     ↓
Lowercasing
     ↓
Remove Punctuation
     ↓
Tokenization
     ↓
Stopword Removal
     ↓
Cleaned Review
```

### Example

**Original review:**

```text
Food is not good!
```

**Processed review:**

```text
food not good
```

Another example:

**Original review:**

```text
I never liked this restaurant.
```

**Processed review:**

```text
never liked restaurant
```

The preprocessing stage resulted in **0 empty processed reviews**.

---

# 📏 Review Length Analysis

The project also analyzes the length of customer reviews.

| Statistic          |  Value |
| ------------------ | -----: |
| Mean               | 536.81 |
| Standard Deviation | 496.93 |
| Minimum            |     18 |
| Median             |    382 |
| Q3                 |    675 |
| Maximum            |  4,994 |

This analysis helps understand how short or detailed customer reviews are.

---

# 🔤 NLP Analysis

After preprocessing, the project analyzes frequently occurring words in customer reviews.

Some of the most frequent tokens are:

| Word      | Frequency |
| --------- | --------: |
| `not`     |    17,506 |
| `food`    |    10,268 |
| `good`    |     8,661 |
| `place`   |     8,457 |
| `great`   |     6,951 |
| `time`    |     5,211 |
| `service` |     5,072 |
| `like`    |     4,626 |
| `one`     |     4,341 |
| `get`     |     4,148 |
| `would`   |     4,021 |
| `go`      |     3,807 |
| `back`    |     3,764 |

These words provide an initial understanding of the common themes present in customer reviews.

---

# 🧠 NLP Techniques

The project uses several Natural Language Processing techniques.

### 1. Tokenization

Reviews are divided into individual words or tokens.

```text
"I love the food"

↓

["I", "love", "the", "food"]
```

### 2. Stopword Removal

Common words that provide limited information are removed.

Examples:

```text
the
is
a
an
and
```

Important words such as **"not"** are retained because they can significantly affect sentiment.

### 3. Text Cleaning

The text is cleaned by removing unnecessary punctuation and unwanted characters.

### 4. Bag-of-Words

Bag-of-Words represents text based on the frequency of words appearing in the documents.

### 5. TF-IDF

TF-IDF assigns importance to words based on their frequency in a document and their occurrence across the entire dataset.

---

# 🤖 Sentiment Classification

The processed review text is converted into numerical features using text vectorization techniques.

The general machine learning workflow is:

```text
Cleaned Reviews
      ↓
Text Vectorization
      ↓
Feature Matrix
      ↓
Train/Test Split
      ↓
Machine Learning Model
      ↓
Sentiment Prediction
      ↓
Model Evaluation
```

The model predicts one of three sentiment classes:

```text
Positive
Negative
Neutral
```

---

# 📊 Model Evaluation

The trained model is evaluated using standard classification metrics.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Classification Report

The final model results will be documented here after model training and evaluation.

```text
Accuracy: XX.XX%

Precision: XX.XX%

Recall: XX.XX%

F1-Score: XX.XX%
```

> **Note:** The final values will be updated after completing the model training phase.

---

# 📱 Flutter Application

A Flutter application is planned as the user interface for the Food Review Analyzer.

The application allows users to enter a food or restaurant review and receive the predicted sentiment.

### Application Workflow

```text
User enters review
        ↓
Flutter Application
        ↓
NLP / ML Model
        ↓
Sentiment Prediction
        ↓
Positive / Negative / Neutral
```

### Example

**User Input:**

```text
The food was delicious and the service was excellent.
```

**Output:**

```text
Sentiment: Positive
```

---

# 🔮 Future Scope

The project can be extended with several additional features:

* ⭐ Aspect-based sentiment analysis
* 🍕 Food-specific sentiment detection
* 🏪 Restaurant-level sentiment analysis
* 📊 Interactive analytics dashboard
* 🌐 Deployment as a web application
* 📱 Complete Android application
* 🔄 Real-time sentiment prediction
* 🌍 Multilingual review analysis
* 🤖 Advanced NLP models such as BERT
* 📈 Restaurant recommendation based on review sentiment
* ☁️ Cloud deployment of the ML model and application

---

# 💡 Potential Applications

The Food Review Analyzer can be useful for:

* Restaurants
* Food delivery platforms
* Restaurant management teams
* Customer feedback analysis
* Food review websites
* Business intelligence teams
* Customer experience analysis

Businesses can use sentiment analysis to identify common customer opinions and understand areas that receive positive or negative feedback.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/VaishnaviMahadik23/food-review-analyzer.git
```

Navigate to the project:

```bash
cd food-review-analyzer
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Python Libraries

The project uses libraries such as:

```text
pandas
numpy
matplotlib
seaborn
nltk
scikit-learn
jupyter
```

Install them using:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn jupyter
```

---

# ▶️ Running the Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then execute the notebooks in sequence:

```text
01_data_understanding.ipynb
        ↓
02_data_preprocessing.ipynb
        ↓
03_nlp_eda.ipynb
        ↓
04_*.ipynb
```

---

# 📱 Running the Flutter Application

Navigate to the Flutter project:

```bash
cd flutter_app
```

Install dependencies:

```bash
flutter pub get
```

Run the application:

```bash
flutter run
```

Make sure Flutter and the required Android development environment are properly configured.

---

# 🧪 Project Development Status

| Phase              | Status         |
| ------------------ | -------------- |
| Repository Setup   | ✅ Completed    |
| Dataset Collection | ✅ Completed    |
| Data Understanding | ✅ Completed    |
| Data Preprocessing | ✅ Completed    |
| NLP EDA            | ✅ Completed    |
| Text Vectorization | 🔄 In Progress |
| Model Training     | 🔄 In Progress |
| Model Evaluation   | 🔄 In Progress |
| Flutter UI         | 🔄 In Progress |
| Model Integration  | ⏳ Planned      |
| Final Testing      | ⏳ Planned      |
| Deployment         | ⏳ Planned      |

---

# 📸 Screenshots

Screenshots of the project will be added here as development progresses.

### EDA

```text
Coming Soon
```

### NLP Analysis

```text
Coming Soon
```

### Flutter Application

```text
Coming Soon
```

### Sentiment Prediction

```text
Coming Soon
```

---

# 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* Data cleaning
* Exploratory Data Analysis
* Pandas and NumPy
* Data visualization
* Natural Language Processing
* Text preprocessing
* Tokenization
* Stopword removal
* Bag-of-Words
* TF-IDF
* Machine Learning
* Sentiment classification
* Model evaluation
* Flutter application development
* Git and GitHub
* End-to-end project development

---

## 👩‍💻 Authors

* **Vaishnavi Shivaji Mahadik**
* **Aradhana Umesh Mahale**
* **Om Vijay Mane**
* **Omkar Mangesh Matkar**

**B.Tech. – Information Technology**
**Sanjivani College of Engineering, Kopargaon**


---

# 📄 License

This project is intended for **educational, academic, and portfolio purposes**.

If a specific dataset is subject to its own license or usage restrictions, those terms take precedence over this repository's general project license.

---

# ⭐ Acknowledgements

* Python community
* Pandas and NumPy
* Scikit-learn
* NLTK
* Matplotlib and Seaborn
* Flutter
* Dataset source/providers

---

## ⭐ If You Find This Project Useful

If this project is helpful for learning NLP, sentiment analysis, or Flutter integration, consider giving the repository a ⭐ on GitHub.
