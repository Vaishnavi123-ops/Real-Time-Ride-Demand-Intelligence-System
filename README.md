# 🚀 Real-Time Ride Demand Intelligence System

## 📌 Overview

This project is an end-to-end data analytics solution that predicts ride demand and provides actionable insights for driver allocation using SQL, Python, and Power BI.

---

## 🎯 Objectives

* Analyze ride demand patterns across time and location
* Predict future demand using machine learning
* Provide actionable decisions (Increase / Reduce drivers)
* Visualize insights using an interactive dashboard

---

## 🧱 Project Architecture

CSV Data → Python (Cleaning & Streaming) → MySQL → SQL Analysis → Python ML Model → Power BI Dashboard

---

## 🔧 Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* MySQL (Data storage & querying)
* Power BI (Visualization)
* Excel (Data preprocessing)

---

## 📊 Key Features

### 🔹 Data Pipeline

* Merged and cleaned large taxi datasets
* Converted date/time formats
* Streamed data into MySQL

### 🔹 SQL Analysis

* Hourly demand analysis
* Location-based demand using latitude & longitude
* Peak demand identification

### 🔹 Demand Intelligence

* Created zones using geospatial clustering
* Classified demand into HIGH / MEDIUM / LOW
* Generated surge alerts

### 🔹 Prediction Model

* Built Linear Regression model
* Improved accuracy using Polynomial Regression
* Predicted hourly ride demand

### 🔹 Decision System

* HIGH demand → Increase drivers
* LOW demand → Reduce drivers
* MEDIUM → Maintain

### 🔹 Power BI Dashboard

* Demand vs predicted demand visualization
* KPI cards (Total rides, Peak demand, Peak hour, Average demand)
* Donut chart for demand distribution
* Map visualization for high-demand zones
* Interactive slicers

---

## 📈 Output

* Hourly demand predictions
* Surge alerts and decisions
* Geospatial hotspot identification

---

## 💡 Key Learnings

* Built end-to-end data pipeline
* Integrated SQL + Python + Visualization tools
* Improved model using non-linear regression
* Applied business logic on analytical outputs

---

## 📸 Dashboard Preview

<img width="712" height="471" alt="Screenshot 2026-04-03 224944" src="https://github.com/user-attachments/assets/a61ed23d-ea18-4cb2-a389-b27e03e81469" />



---

## 🚀 Future Improvements

* Real-time streaming using APIs
* Advanced ML models (Time Series / LSTM)
* Deployment using Flask

---

## 👩‍💻 Author

Vaishnavi
