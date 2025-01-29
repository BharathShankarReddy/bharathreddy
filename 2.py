from google.colab import files
import pandas as pd

# Upload the file from local system
uploaded = files.upload()

# Get the filename of the uploaded file
aaa = list(uploaded.keys())[0]

df = pd.read_csv(aaa)
print(df)
