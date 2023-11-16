import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('V3评测体系0921.xlsx')

# 初始化一个空字典来存储数据
data_dict = {}

# 遍历DataFrame的每一行
for index, row in df.iterrows():
    # 获取文本
    text = row[0]
    # 使用"->"分割文本
    split_text = text.split('->')
    # 获取第二级的文本作为键
    key = split_text[1] if len(split_text) > 1 else '其他'
    # 如果键不在字典中，初始化一个空字典
    if key not in data_dict:
        data_dict[key] = {}
    # 获取最后一级的文本作为子键
    sub_key = split_text[-1]
    # 如果子键已经在字典中，就在子键后面加入数字
    if sub_key in data_dict[key]:
        i = 1
        new_sub_key = sub_key + str(i)
        while new_sub_key in data_dict[key]:
            i += 1
            new_sub_key = sub_key + str(i)
        sub_key = new_sub_key
    # 将完整文本作为值
    data_dict[key][sub_key] = text

# 对每个分类的字典进行排序并保存为json文件
for key, value in data_dict.items():
    sorted_dict = dict(sorted(value.items()))
    with open(f'./评测体系/{key}.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_dict, f, ensure_ascii=False, indent=4)
