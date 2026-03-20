# 🌍 Population Service API

Simple REST API for fetching historical population data and predicting future population using World Bank data.

---

## 🚀 Features

* Get population for a country in a given past year
* Predict future population using linear regression
* Clean and simple REST API
* Built with Flask (Python)

---

## 🛠 Tech Stack

* Python 3.12
* Flask
* Requests

---

## 📦 Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd population-service
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
python -m pip install flask requests
```

---

## ▶️ Run the app

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 1. Get Past Population

```
GET /population/past?country={CODE}&year={YEAR}
```

**Example:**

```
http://127.0.0.1:5000/population/past?country=BG&year=2010
```

**Response:**

```json
{
  "country": "BG",
  "year": 2010,
  "population": 7395599
}
```

---

### 2. Predict Future Population

```
GET /population/future?country={CODE}&year={YEAR}
```

**Example:**

```
http://127.0.0.1:5000/population/future?country=BG&year=2030
```

**Response:**

```json
{
  "country": "BG",
  "year": 2030,
  "population": 6500000
}
```

---

## 📊 Data Source

* World Bank API
  https://api.worldbank.org/

---

## 🧠 How Prediction Works

* Uses last 5 years of population data
* Applies simple linear regression
* Estimates population for a future year

---

## ⚖️ Tradeoffs

* Linear model is not highly accurate
* Multiple API calls per prediction
* No caching implemented

---

## 📁 Project Structure

```
.
├── app.py
├── services.py
├── predict.py
└── README.md
```

---

## 👨‍💻 Author

Kris
