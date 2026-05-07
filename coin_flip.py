# coin flip

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42) # seed will set the timing to fix
flips = np.random.randint(0, 2, size=1000)
df = pd.DataFrame({'Result': flips})


# calcualtion of the probability
df['Cumulative_Heads'] = df['Result'].cumsum()
df['Trial_Number'] = range(1, 1001)
df['Running_Prob'] = df['Cumulative_Heads'] / df['Trial_Number']

# boolean checking
final_prob = df['Running_Prob'].iloc[-1]
is_exactly_half = pd.Series([final_prob == 0.5])

print(f"Final Probability: {final_prob}")
print(f"Is it exactly 0.5? {is_exactly_half.item()}")


# plotting
# plt.figure(figsize=(12, 5))

# bar chart
# plt.subplot(1, 2, 1)
df['Result'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Final Count: Heads vs Tails')
plt.xticks([0, 1], ['Tails', 'Heads'], rotation=0)
plt.ylabel('Total Count')
plt.show()

# scattered plot
# plt.subplot(1, 2, 2)
plt.plot(df['Trial_Number'], df['Running_Prob'], color='green', label='Actual Probability')
plt.axhline(y=0.5, color='red', linestyle='--', label='Theoretical Target (0.5)')
plt.title('How Probability Stabilizes Over Time')
plt.xlabel('Number of Flips')
plt.ylabel('Probability of Heads')
plt.legend()

plt.tight_layout()
plt.show()
# plt.savefig('coin_flip_analysis.png')