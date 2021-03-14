import numpy as np
import pandas as pd

def load_and_process(df):

    # Method Chain 1 (Load data and deal with missing data)
    
    df1 = (pd.read_excel(df).rename(columns={"Jitter(Abs)": "Jitter_ms"})
           .sort_values("subject#", ascending=True)
           .reset_index(drop=True)
           #.loc[:, ["subject#", "Jitter_ms","age"]]
           
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1.drop(columns=['Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','Jitter:RAP','Jitter:PPQ5','Jitter:DDP'])
        #.assign(color_filter=lambda x: np.where((x.age > 70) & (x.Jitter_ms > .00002), 1, 0))
      )

    # Make sure to return the latest dataframe

    return df2