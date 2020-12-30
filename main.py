# import tensorflow as tf
import pandas as pd
import numpy as np
# import ktrain
# from ktrain import text


data_train = pd.read_excel('data/train.xlsx', dtype=str)
data_test = pd.read_excel('data/test.xlsx', dtype=str)

print(data_test)