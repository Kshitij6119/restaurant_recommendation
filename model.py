from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def train_model(train_df):
    features = ["vendor_latitude", "vendor_longitude", "deliverydistance", "preparationtime"]
    X = train_df[features]
    y = train_df["vendor_id"]

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_val, y_val)
    print(f"✅ Model trained with accuracy: {accuracy:.2f}")

    return model, le
