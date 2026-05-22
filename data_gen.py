import pandas as pd
import numpy as np

# Madurai Ward list
wards = ["Mattuthavani", "Periyar", "Simmakkal", "Goripalayam", "Anna Nagar"]

# 100 random lines of data create pandrom
data = {
    "Location": np.random.choice(wards, 100),
    "Status": np.random.choice(["Empty", "Half-Full", "Critical"], 100, p=[0.4, 0.4, 0.2])
}

df = pd.DataFrame(data)
# Direct-ah C drive folder-la save pandrom, path prachana varakoodadhu nu
df.to_csv(r"C:\Data analyst\MSDB-DATA ANALYSIS\madurai_waste_data.csv", index=False)
print("✅ Success! 'madurai_waste_data.csv' ready aayiduchu macha!")