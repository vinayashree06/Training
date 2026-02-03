#position based indexing
import pandas as pd
import numpy as np
data=np.array(['g','e','e','k','s'])
s=pd.Series(data)
print(s[0])
print(s[1])
print(s[:5])

#label based indexing
import pandas as pd
data=np.array(['g','e','e','k','s'])
s1=pd.Series(data,index=[10,20,30,40,50])
print(s1[10])