import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt
pd.set_option("display.max_colwidth", 200)

list=[]
url="https://db.netkeiba.com/race/202106030811/"
dfs = pd.read_html(url)

race=dfs[5]
race_lap=race.iat[0,1]
race_lap_cell=race_lap.split(" - ")





list.append(race_lap_cell)

lists=[float(i) for i in list[0]]



plt.plot(lists)

plt.show()
