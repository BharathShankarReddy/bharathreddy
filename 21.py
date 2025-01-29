
import pandas as pd
from sklearn.preprocessing import StandardScaler
data = {
    "age":[25,30,35,40,45],
    "height": [150, 160, 170, 180, 190],
    "weight": [50,60,70,80,90],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

scaler = StandardScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data,columns=df.columns)
print("\nNormlaized DataFrame(scaled to range [0, 1]):")
print(normalized_df)
