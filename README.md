# 🍽️ Food Review Analyzer

An end-to-end **NLP-based Food Review Analyzer** that analyzes restaurant reviews, predicts their sentiment, identifies review aspects, and presents the results through a **Flutter mobile application**.

The project combines **Natural Language Processing, Machine Learning, FastAPI, SQLite, REST APIs, and Flutter** to provide an interactive system for analyzing customer feedback.

---

## 📌 Project Overview

Customer reviews contain valuable information about food quality, service, cleanliness, ambience, pricing, location, and overall customer satisfaction.

Manually analyzing a large number of reviews can be difficult and time-consuming. The **Food Review Analyzer** automates this process by applying NLP techniques to restaurant reviews and providing meaningful sentiment and aspect-level information.

The system supports:

* Review sentiment classification
* Positive, Negative, and Neutral sentiment detection
* Aspect-based review analysis
* Review result storage
* Review history
* Analytics
* REST API integration
* Flutter mobile application

### Overall Workflow

```text
                    ┌──────────────────────┐
                    │   Customer Review    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Text Preprocessing   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   NLP Processing     │
                    │  BoW / TF-IDF        │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
     ┌─────────────────┐              ┌──────────────────┐
     │    Sentiment    │              │ Aspect Analysis  │
     │   Classification│              │                  │
     └────────┬────────┘              └────────┬─────────┘
              │                                │
              └────────────────┬───────────────┘
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    SQLite Database   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Flutter App       │
                    └──────────────────────┘
```

---

# 🎯 Objectives

The main objectives of this project are:

* Analyze restaurant and food-related customer reviews.
* Clean and preprocess natural language text.
* Apply NLP techniques for textual analysis.
* Classify reviews into Positive, Negative, and Neutral categories.
* Identify important aspects mentioned in customer reviews.
* Store analyzed reviews and results.
* Provide review history and analytics.
* Develop a REST API for communication between the ML system and application.
* Build a user-friendly Flutter mobile application.
* Demonstrate an end-to-end AI/NLP application.

---

# ✨ Key Features

## 🧠 NLP & Machine Learning

* Text preprocessing
* Tokenization
* Stopword removal
* Punctuation removal
* Review length analysis
* Word-frequency analysis
* N-gram analysis
* Bag-of-Words vectorization
* TF-IDF vectorization
* Sentiment classification
* Aspect analysis

## 📊 Analysis

* Positive sentiment detection
* Negative sentiment detection
* Neutral sentiment detection
* Aspect-level sentiment information
* Review analytics
* Sentiment distribution
* Review history

## ⚙️ Backend

* FastAPI REST API
* SQLite database
* NLP service integration
* Structured request/response schemas
* Review analysis endpoint
* History and analytics endpoints

## 📱 Flutter Application

* Material 3 interface
* Splash screen
* Bottom navigation
* Review input
* Sentiment result screen
* Review history
* Analytics
* REST API integration
* Android emulator support

---

# 🛠️ Technology Stack

| Category         | Technologies              |
| ---------------- | ------------------------- |
| Programming      | Python, Dart              |
| NLP              | NLTK, Scikit-learn        |
| Data Processing  | Pandas, NumPy             |
| Visualization    | Matplotlib, Seaborn       |
| Machine Learning | Scikit-learn              |
| Vectorization    | Bag-of-Words, TF-IDF      |
| Backend          | FastAPI                   |
| Database         | SQLite                    |
| API              | REST API                  |
| Mobile App       | Flutter                   |
| UI               | Material 3                |
| Version Control  | Git, GitHub               |
| Development      | Jupyter Notebook, VS Code |

---

# 📊 Dataset

The project uses a restaurant review dataset containing customer reviews, ratings, business information, location information, and sentiment labels.

### Dataset

```text
yelp_sentiment_master_dataset.csv
```

### Dataset Size

```text
14,351 rows
10 columns
```

### Dataset Columns

| Column           | Description                        |
| ---------------- | ---------------------------------- |
| `stars_review`   | Rating given by the reviewer       |
| `text`           | Customer review text               |
| `date`           | Date of the review                 |
| `name`           | Restaurant/business name           |
| `categories`     | Business categories                |
| `city`           | Business city                      |
| `state`          | Business state                     |
| `stars_business` | Business rating                    |
| `review_count`   | Number of reviews for the business |
| `rating_review`  | Review sentiment category          |

---

# 📈 Dataset Sentiment Distribution

The dataset contains three sentiment categories.

| Sentiment |    Reviews | Percentage |
| --------- | ---------: | ---------: |
| Positive  |      9,857 |     68.69% |
| Negative  |      2,699 |     18.81% |
| Neutral   |      1,795 |     12.51% |
| **Total** | **14,351** |   **100%** |

The dataset therefore contains substantially more positive reviews than negative and neutral reviews.

---

# ⭐ Star Rating Distribution

|  Rating | Number of Reviews | Percentage |
| ------: | ----------------: | ---------: |
|  1 Star |             1,422 |      9.91% |
| 2 Stars |             1,277 |      8.90% |
| 3 Stars |             1,795 |     12.51% |
| 4 Stars |             3,949 |     27.52% |
| 5 Stars |             5,908 |     41.17% |

The sentiment mapping used in the project is:

```text
1 Star → Negative
2 Stars → Negative
3 Stars → Neutral
4 Stars → Positive
5 Stars → Positive
```

---

# 🧹 Data Preprocessing

The raw review text is processed before applying NLP and machine learning techniques.

### Preprocessing Pipeline

```text
Raw Review
    ↓
Text Cleaning
    ↓
Lowercasing
    ↓
Punctuation Removal
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
Processed Review
```

### Example 1

Original:

```text
Food is not good!
```

Processed:

```text
food not good
```

### Example 2

Original:

```text
I never liked this restaurant.
```

Processed:

```text
never liked restaurant
```

The preprocessing stage resulted in:

```text
Empty processed reviews = 0
```

The word **`not`** is retained because negation can be important for sentiment interpretation.

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

This analysis helps understand the distribution and characteristics of customer review text.

---

# 🔤 Frequent Words

Some of the most frequently occurring cleaned tokens are:

| Token     | Frequency |
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

---

# 🔎 N-Gram Analysis

The project also analyzes combinations of words to identify common phrases in customer reviews.

Examples of frequently occurring positive bigrams include:

```text
great food
really good
go back
highly recommend
```

N-gram analysis helps identify meaningful phrases that may not be captured by analyzing individual words alone.

---

# 🧠 NLP Techniques

## 1. Tokenization

Tokenization divides a review into individual words or tokens.

```text
"I love the food"

        ↓

["I", "love", "the", "food"]
```

---

## 2. Stopword Removal

Common words that contribute limited information are removed during preprocessing.

Examples:

```text
the
is
a
an
and
```

Important sentiment-related words such as `not` are preserved.

---

## 3. Bag-of-Words

Bag-of-Words represents each review using the frequency of words appearing in the text.

This converts textual data into numerical features that can be processed by machine learning algorithms.

---

## 4. TF-IDF

TF-IDF, or **Term Frequency-Inverse Document Frequency**, assigns importance to words based on how frequently they occur in a review and how distinctive they are across the complete collection of reviews.

---

# 🤖 Sentiment Classification

The project converts processed review text into numerical features and applies machine learning techniques for sentiment classification.

### Classification Pipeline

```text
Processed Review
       ↓
Text Vectorization
       ↓
Numerical Feature Matrix
       ↓
Machine Learning Model
       ↓
Sentiment Prediction
       ↓
Positive / Negative / Neutral
```

The final application uses the trained NLP/ML pipeline to analyze user-submitted reviews.

---

# 🔍 Aspect-Based Analysis

In addition to overall sentiment, the project analyzes specific aspects mentioned in reviews.

The implemented aspect analysis includes categories such as:

* 🍴 Food
* 🧼 Cleanliness
* 🌆 Location
* 💰 Price
* 🪑 Ambience

Example aspect-level output:

```text
Food         → Positive
Service      → Negative
Location     → Positive
Price        → Neutral
```

This provides more detailed information than overall sentiment alone.

---

# 📊 Aspect Sentiment Analysis

The project can represent aspect-level sentiment using a sentiment-by-aspect analysis.

Example structure:

| Aspect      | Negative | Neutral | Positive |
| ----------- | -------: | ------: | -------: |
| Ambience    |        1 |       0 |       12 |
| Cleanliness |        2 |       0 |        4 |
| Food        |       17 |       7 |       52 |
| Location    |        8 |       5 |       37 |
| Price       |        — |       — |        — |

The values shown above represent the analyzed aspect results available during project development.

---

# ⚙️ Backend Architecture

The backend is implemented using **FastAPI**.

### Backend Components

```text
backend/
│
├── main.py
├── database.py
├── schemas.py
├── nlp_service.py
└── food_reviews.db
```

### Responsibilities

#### `main.py`

Handles:

* FastAPI application
* API routes
* Request handling
* Backend application startup

#### `database.py`

Handles:

* SQLite database connection
* Database operations
* Review storage and retrieval

#### `schemas.py`

Defines structured request and response models.

#### `nlp_service.py`

Handles NLP-related processing and review analysis.

#### `food_reviews.db`

SQLite database used for storing analyzed review information and application data.

---

# 🔗 REST API

The Flutter application communicates with the FastAPI backend through REST APIs.

### General Architecture

```text
Flutter Application
        │
        │ HTTP Request
        ▼
   FastAPI Backend
        │
        ├── NLP Service
        │
        └── SQLite Database
        │
        ▼
   JSON Response
        │
        ▼
Flutter Application
```

This architecture separates the mobile user interface from the NLP and data-processing logic.

---

# 📱 Flutter Application

The frontend is developed using **Flutter and Dart**.

The application provides a mobile interface through which users can interact with the Food Review Analyzer.

## Main Application Features

### 🏠 Review Analysis

Users can enter a restaurant review and submit it for analysis.

The application sends the review to the FastAPI backend and displays the returned analysis.

### 📊 Result Screen

Displays the analyzed review result, including sentiment and available analysis information.

### 📜 History

Users can view previously analyzed reviews stored by the backend.

### 📈 Analytics

The application provides an analytics view of review and sentiment information.

### 🧭 Bottom Navigation

The application uses bottom navigation to provide access to the major application sections.

### 🎨 Material 3 UI

The application uses Flutter's Material 3 design system for a modern and consistent interface.

### 🚀 Splash Screen

A splash screen is implemented as the initial application screen.

---

# 📂 Flutter Project Structure

The Flutter application is organized into reusable components.

```text
flutter_app/
│
├── lib/
│   ├── main.dart
│   │
│   ├── models/
│   │   ├── review_result.dart
│   │   └── analytics.dart
│   │
│   ├── services/
│   │   └── api_service.dart
│   │
│   ├── screens/
│   │   ├── ...
│   │
│   ├── theme/
│   │   └── ...
│   │
│   └── widgets/
│       └── ...
│
├── android/
├── assets/
├── ios/
├── web/
├── linux/
├── macos/
├── test/
├── windows/
├── pubspec.yaml
└── ...
```

---

# 📱 Android Configuration

The application is configured for Android development and testing.

The Android application uses:

```text
Flutter 3.41.4
Dart 3.11.1
Android SDK 35
```

The Android application includes Internet permission because it communicates with the FastAPI backend.

For Android Emulator communication, the backend is accessed using:

```text
http://10.0.2.2:8000
```

`10.0.2.2` maps to the host machine from the Android emulator.

---

# 🗄️ Database

The project uses **SQLite** as a lightweight local database for backend data storage.

Database file:

```text
backend/food_reviews.db
```

The database supports storing review analysis information required by the application, including history and analytics-related data.

---

# 📁 Project Structure

The complete project follows an organized separation between data analysis, backend services, and the mobile application.

```text
food-review-analyzer/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_02_data_understanding.ipynb
│   ├── 03_text_preprocessing.ipynb
│   ├── 04_nlp_eda.ipynb
│   ├── 05_bow_tfidf_vectorization.ipynb
│   ├── 06_sentiment_classification.ipynb
│   ├── 07_aspect_based_sentiment.ipynb
│   ├── 08_fastapi_backend_testing.ipynb
│   └── 09_integration_final_testing.ipynb
│
│
├── models/
│   └── ...
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   ├── nlp_service.py
│   └── food_reviews.db
│
├── flutter_app/
│   ├── lib/
│   │   ├── main.dart
│   │   ├── models/
│   │   ├── screens/
│   │   ├── services/
│   │   ├── theme/
│   │   └── widgets/
│   │
│   ├── android/
│   ├── assets/
│   ├── ios/
│   ├── web/
│   ├── linux/
│   ├── macos/
│   ├── test/
│   ├── windows/
│   └── pubspec.yaml
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/VaishnaviMahadik23/food-review-analyzer.git
```

Navigate into the project:

```bash
cd food-review-analyzer
```

---

# 🐍 Backend Setup

Navigate to the backend/project environment as required by the repository structure.

Create a Python virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

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

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the FastAPI Backend

Start the backend using:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation can be accessed from:

```text
http://127.0.0.1:8000/docs
```

---

# 📓 Run the NLP Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in sequence:

```text
01_02_data_understanding.ipynb
          ↓
03_text_preprocessing.ipynb
          ↓
04_nlp_eda.ipynb
          ↓
05_bow_tfidf_vectorization.ipynb
          ↓
06_sentiment_classification.ipynb
          ↓
07_aspect_based_sentiment.ipynb
          ↓
08_fastapi_backend_testing.ipynb
          ↓
09_integration_final_testing.ipynb
```

The notebooks document the data understanding, preprocessing, NLP analysis, vectorization, and model-development workflow.

---

# 📱 Run the Flutter Application

Navigate to the Flutter application:

```bash
cd flutter_app
```

Install Flutter dependencies:

```bash
flutter pub get
```

Check Flutter configuration:

```bash
flutter doctor
```

Run the application:

```bash
flutter run
```

For an Android emulator:

```bash
flutter run -d emulator-5554
```

Make sure the FastAPI backend is running before using features that require API communication.

---

# 🔄 Complete Application Flow

```text
1. User opens Flutter application
              ↓
2. User enters a restaurant review
              ↓
3. Flutter sends HTTP request
              ↓
4. FastAPI receives the review
              ↓
5. NLP service preprocesses the text
              ↓
6. Sentiment is analyzed
              ↓
7. Aspect analysis is performed
              ↓
8. Result is stored in SQLite
              ↓
9. JSON response is returned
              ↓
10. Flutter displays the result
              ↓
11. History and analytics can be viewed
```

---

# 📊 Project Results

The project successfully implements the complete analysis pipeline from raw review data to a usable mobile application.

### Dataset Analysis

```text
Total Reviews       : 14,351
Positive Reviews    : 9,857
Negative Reviews    : 2,699
Neutral Reviews     : 1,795
```

### Preprocessing

```text
Processed Reviews   : 14,351
Empty Reviews       : 0
```

### Implemented NLP Components

```text
✓ Text preprocessing
✓ Tokenization
✓ Stopword removal
✓ Word-frequency analysis
✓ N-gram analysis
✓ Bag-of-Words
✓ TF-IDF
✓ Sentiment classification
✓ Aspect analysis
```

### Application Components

```text
✓ FastAPI backend
✓ SQLite database
✓ REST API
✓ Flutter application
✓ Sentiment result screen
✓ Review history
✓ Analytics
✓ Material 3 UI
✓ Bottom navigation
✓ Splash screen
```

---

# 📈 Model Evaluation

The project evaluates sentiment classification using standard machine-learning evaluation metrics.

The evaluation process includes:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

The exact final model-performance values should be taken directly from the final model-evaluation notebook/output rather than manually estimated.

---

# 🧪 Testing

The application was tested across the major project components:

### NLP

* Review preprocessing
* Sentiment analysis
* Aspect analysis
* Empty/invalid text handling

### Backend

* API requests
* API responses
* Database operations
* Review history
* Analytics

### Flutter

* Application startup
* Navigation
* Review submission
* API communication
* Result display
* History
* Analytics

### Android

The Flutter application was tested using an Android emulator.

```text
Device: emulator-5554
Android SDK: 35
Flutter: 3.41.4
Dart: 3.11.1
```

---

# 📸 Screenshots

Screenshots can be added to this section after uploading them to the repository.

### Application Screens

```text
Coming Soon / Add screenshots here
```

Recommended screenshots:

1. Splash Screen
2. Home/Review Input Screen
3. Sentiment Result Screen
4. Aspect Analysis
5. Review History
6. Analytics Dashboard

Example Markdown:

```markdown
![Home Screen](screenshots/home.png)
![Result Screen](screenshots/result.png)
![History Screen](screenshots/history.png)
![Analytics Screen](screenshots/analytics.png)
```

---

# 🎓 Learning Outcomes

This project demonstrates practical knowledge of:

### Python & Data Science

* Python programming
* Pandas
* NumPy
* Data cleaning
* Exploratory Data Analysis
* Data visualization

### Natural Language Processing

* Text preprocessing
* Tokenization
* Stopword removal
* Frequency analysis
* N-grams
* Bag-of-Words
* TF-IDF
* Sentiment classification
* Aspect analysis

### Backend Development

* FastAPI
* REST APIs
* Request/response schemas
* SQLite
* Database operations
* API integration

### Mobile Development

* Flutter
* Dart
* Material 3
* REST API integration
* JSON handling
* Android application development
* Navigation and reusable UI components

### Software Development

* Git
* GitHub
* Project structuring
* Modular development
* End-to-end application development

---

# 🔮 Future Scope

The project can be further enhanced with:

* Advanced transformer-based NLP models such as BERT
* Multilingual sentiment analysis
* Real-time review analysis
* More detailed aspect extraction
* Restaurant recommendation functionality
* Restaurant comparison
* Cloud deployment
* Authentication and user accounts
* Advanced analytics dashboards
* Real-time review data integration
* Model retraining pipelines
* Improved explainability of sentiment predictions

---

# 💼 Potential Applications

The Food Review Analyzer can be used for:

* Restaurant customer-feedback analysis
* Food delivery platforms
* Restaurant management
* Customer experience analysis
* Business intelligence
* Review monitoring
* Restaurant performance analysis
* Academic NLP projects

---

# 🔐 Data & Privacy

The application should be used with review data that is legally available for analysis.

When deploying the application with real customer data, appropriate privacy, security, and data-protection practices should be followed.

---

# 👩‍💻 Authors

* **Vaishnavi Shivaji Mahadik**
* **Aradhana Umesh Mahale**
* **Om Vijay Mane**
* **Omkar Mangesh Matkar**

**B.Tech. – Information Technology**
**Sanjivani College of Engineering, Kopargaon**

---

# ⭐ Acknowledgements

This project uses open-source technologies and libraries including:

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Matplotlib
* Seaborn
* FastAPI
* SQLite
* Flutter
* Dart

---

# 📄 License

This project is developed for **educational, academic, and portfolio purposes**.

Dataset usage and redistribution should follow the license and terms associated with the original dataset source.

---

# ⭐ Project Summary

**Food Review Analyzer** is an end-to-end NLP application that combines **data analysis, natural language processing, machine learning, backend development, database management, REST APIs, and Flutter mobile development**.

The system takes a customer restaurant review, processes and analyzes the text, identifies its sentiment and relevant aspects, stores the result, and presents the information through a mobile application.

```text
                 FOOD REVIEW ANALYZER
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
      NLP/ML          FastAPI          Flutter
        │                │                │
        │                ▼                │
        │             SQLite             │
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
              Customer Review Insights
```

**Built with Python + NLP + FastAPI + SQLite + Flutter 🚀**
