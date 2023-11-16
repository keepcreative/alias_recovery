import pandas as pd
import json

df = pd.read_excel('1113标注结果.xlsx')

alias = set()
for item in df['能力项'].dropna():
    if isinstance(item, str):
        for i in item.split(','):
            # if i.split('->')[0] != '评测体系':
            alias.add(i.strip())

alias_dict = {key: "" for key in alias}

# ability_types = ['应用能力', '认知能力', '推理能力', '知识储备', '交互能力', '学习能力', '指令遵循']
# for key in alias:
#     if key.split('->')[0] in ability_types:
#         alias_dict[key] = f"评测体系->能力项->{key}"

# 将字典分为两部分，一部分是值不为空的，一部分是值为空的
non_empty_dict = {k: v for k, v in alias_dict.items() if v}

empty_dict = {k: v for k, v in alias_dict.items() if not v}

# 合并两个字典，将值为空的字典放在后面
final_dict = {**non_empty_dict, **empty_dict}
sorted_final_dict = dict(sorted(final_dict.items()))
with open('能力项2_alias_dict.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_final_dict, f, ensure_ascii=False, indent=4)
