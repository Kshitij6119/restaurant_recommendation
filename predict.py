def generate_predictions(model, test_df, vendors):
    # Join test_locations with all vendors to create possible pairs
    test_df['key'] = 1
    vendors['key'] = 1
    merged = test_df.merge(vendors, on='key').drop('key', axis=1)

    # Calculate distance
    from geopy.distance import geodesic
    merged['distance'] = merged.apply(lambda row: geodesic(
        (row['latitude'], row['longitude']),
        (row['latitude_y'], row['longitude_y'])
    ).km, axis=1)

    features = ['distance']
    merged['prediction'] = model.predict_proba(merged[features])[:, 1]

    top_preds = merged.groupby(['customer_id', 'location_number']) \
                      .apply(lambda x: x.nlargest(1, 'prediction')) \
                      .reset_index(drop=True)

    top_preds['CID X LOC_NUM X VENDOR'] = top_preds.apply(
        lambda x: f"{x['customer_id']} X {x['location_number']} X {x['id']}", axis=1)

    return top_preds[['CID X LOC_NUM X VENDOR']]
