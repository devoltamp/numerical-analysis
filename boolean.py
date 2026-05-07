# boolean reduction

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# creating random data
random_data = np.random.randint(1, 101, size=(4, 3))
df = pd.DataFrame(random_data, columns=['A', 'B', 'C'])

print("--- Randomly Generated Table ---")
print(df)


threshold = 50
print(f"\nGoal: Find numbers greater than {threshold}")


test = df > threshold
print("\n--- The 'Reduced' Results ---")

# .any()
print("Does each column have AT LEAST ONE success?")
print(test.any()) 

# .all()
print("\nIs EVERY number in a row a success?")
print(test.all(axis=1)) # the axis could be changed


# additional 
print("\n--- Data Health Check ---")
print(f"Is the table empty? {df.empty}")
print(f"Are all values in Column A unique? {df['A'].is_unique}")
print(f"Are there any missing values (NaNs)? {df.isnull().values.any()}")

# example of this is given in the coin_flip.py file