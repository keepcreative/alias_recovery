import pandas as pd

# 读取两个Excel文件
predict = pd.read_excel('v3d0_no_category_还原.xlsx')
groundtruth = pd.read_excel('V3评测体系0921.xlsx')

# 获取groundtruth的第一列数据
groundtruth_data = groundtruth.iloc[:, 0]
not_in_groundtruth = set()
# 遍历predict的第2、3、4列
for i in range(1, 4):
    # 获取predict的第i列数据
    predict_data = predict.iloc[:, i]

    # 遍历每一个单元格
    for cell in predict_data:
        # 将内容用逗号分割
        items = str(cell).split(',')

        # 对比，找出不在groundtruth表格中的条目
        for item in items:
            if item not in groundtruth_data.values:
                not_in_groundtruth.add(item)
for item in not_in_groundtruth:
    print(item)