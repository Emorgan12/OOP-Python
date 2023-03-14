read

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())


import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)



import pandas as pd

pd.options.display.max_rows = 6

df = pd.read_csv('data.csv')

print(df)























