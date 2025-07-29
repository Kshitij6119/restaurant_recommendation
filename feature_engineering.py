def create_features(train_orders, train_locations, vendors):
    # Rename to lowercase for consistency
    train_locations = train_locations.rename(columns={"location_number": "LOCATION_NUMBER"})

    # Merge orders with customer location
    train = train_orders.merge(train_locations, on=["customer_id", "LOCATION_NUMBER"], suffixes=('', '_cust'))

    # Merge with vendor location
    train = train.merge(vendors, on="vendor_id", suffixes=('', '_vendor'))

    return train
