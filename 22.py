import pandas as pd
from  sklearn.preprocessing import OneHotEncoder
data = {
    "customer_id": [1,2,3,4,5],
    "gender": ["Male","Male","Female","Female","Male"],
    "city": ["Hyderabad","Kolkata","Banglore","Pune","Kerela"],
    "fruits": ["Apple","Banana","Kivi","Orange","Grapes"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender","city","fruits"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
print(encoded_df)
print("\nOne-Hot Encoded DataFrame with sklearn:")
