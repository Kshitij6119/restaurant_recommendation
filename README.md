# 🍽️ Restaurant Recommendation Engine

## 🚀 Goal
Predict which vendor a test customer is most likely to order from using their location and historical order data.

## Dataset
- train_customers.csv
- train_locations.csv
- train_orders.csv
- test_customers.csv
- test_locations.csv
- vendors.csv

##🧠 Features Used

Distance between customer and vendor (via geopy)
Historical vendor-customer interaction
Popularity of vendor
Order patterns and density


## How to Run

```bash
pip install -r requirements.txt
python main.py
```
##🧪 Project Structure
```bash
restaurant_recommendation/
├── data/
│   ├── orders.csv
│   ├── train_locations.csv
│   ├── vendors.csv
│   ├── test_customers.csv
│   └── test_locations.csv
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── model.py
├── main.py
└── README.md

```
##✅ Output

After execution, the script will print or save the predicted vendor for each test customer based on proximity and order history.
