import pandas as pd

def load_data():
    train_orders = pd.read_csv("data/orders.csv", low_memory=False)
    train_locations = pd.read_csv("data/train_locations.csv")
    vendors = pd.read_csv("data/vendors.csv")

    # Rename vendor columns to match expected names
    vendors = vendors.rename(columns={
        "id": "vendor_id",
        "latitude": "vendor_latitude",
        "longitude": "vendor_longitude"
    })

    return train_orders, train_locations, vendors
