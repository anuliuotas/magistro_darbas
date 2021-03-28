import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

file = 'dashboard_data_2020-01-01_2020-11-30.csv'

price_df = pd.read_csv(file, sep=';', decimal=',')

price_df['Time'] = pd.to_datetime(price_df['Time'])
price_df['Nord Pool Lietuva'] = pd.to_numeric(price_df['Nord Pool Lietuva'], errors='coerce').fillna(0).astype(np.int64)
price_df = price_df.set_index('Time')

print(price_df.index)
print(price_df.head())
print(price_df.dtypes)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(11, 3)})
gr = price_df.loc['2020-01-27':'2020-03-01']['Nord Pool Lietuva'].plot(linewidth=0.5)

#gr.xaxis.set_major_locator(mdates.DayLocator(interval=24))
#gr.xaxis.set_major_formatter(mdates.DateFormatter('%D'))
#for tick in gr.get_xticklabels():
#    tick.set_rotation(90)

plt.show()