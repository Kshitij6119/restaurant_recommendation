from src.preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model

print(" Loading data...")
train_orders, train_locations, vendors = load_data()

print(" Creating features...")
train_df = create_features(train_orders, train_locations, vendors)

print(" Training model...")
model, label_encoder = train_model(train_df)
