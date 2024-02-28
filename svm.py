# importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# reading data
cell_df = pd.read_csv("cell_samples.csv")
cell_df.head()