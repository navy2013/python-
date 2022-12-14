import numpy as np
import pandas as pd



# ⽆论是numpy中的NAN还是Python中的None在pandas中都以缺失数据NaN对待
l1 = [0, 1, 7, 9, np.NAN, None, 1024, 512]
# pandas自动添加索引
s1 = pd.Series(data=l1)
# 指定行索引
s2 = pd.Series(data=11, index=list('abcdefhi'), dtype='float32')
# 传入字典创建，key行索引
s3 = pd.Series(data={'a': 99, 'b': 137, 'c': 149}, name='Python_score')
display(s1, s2, s3)
