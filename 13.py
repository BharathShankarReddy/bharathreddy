import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
datf = pd.DataFrame({"Summary 1":[7,7,5,5,3],"Summary 2":[1,2,2,4,9]})
p = sns.histplot(data=datf)
p.set(xlabel="X Label value",ylabel = "Y Label Value")
plt.show()
