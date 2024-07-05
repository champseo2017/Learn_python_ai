import pandas as pd

"""
เปลี่ยน input_ids ให้เป็น tensor 2 มิติของ one-hot vector
โดยทั่วไป one-hot vector มักถูกใช้ในการเข้ารหัสข้อมูล categorical ในงาน machine learning ไม่ว่าจะเป็นประเภท ordinal (มีลำดับ) หรือ nominal (ไม่มีลำดับ)
"""
categorical_df = pd.DataFrame(
    {"Name": ["Bumblebee", "Optimus Prime", "Megatron"], 
     "Label ID": [0,1,2]}
)

one_hot_df = pd.get_dummies(categorical_df["Name"]).astype(int)

print(one_hot_df)
# ผลลัพธ์
#    Bumblebee  Megatron  Optimus Prime
# 0          1         0              0
# 1          0         0              1
# 2          0         1              0