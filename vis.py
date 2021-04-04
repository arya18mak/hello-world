import matplotlib.pyplot as plt
import pandas as pd

col_list = ["Sno", "Date", "Confirmed", "Deaths", "Cured"]
df = pd.read_csv("covid_19_india.csv", usecols=col_list)
xy = df.groupby("Date", as_index=False).sum()
z = xy.sort_values(by='Sno')

plt.plot(z["Date"], z["Confirmed"])
plt.plot(z["Date"], z["Deaths"])
plt.plot(z["Date"], z["Cured"])
print(z)
plt.grid(True)
plt.show()

