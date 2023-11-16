import pandas as pd
import json


def load_alias_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def update_df(df, column_name, alias_dict):
    for index, row in df.iterrows():
        if pd.notnull(row[column_name]) and isinstance(row[column_name], str):
            new_item = ''
            for item in row[column_name].split(','):
                if item in alias_dict:
                    new_item += alias_dict[item]
                else:
                    new_item += item
                new_item += ','
            df.loc[index, column_name] = new_item[:-1]  # 去掉最后的逗号
    return df


def main():
    df = pd.read_excel('v3d0_no_category.xlsx')
    theme_alias_dict = load_alias_dict('主题_alias_dict.json')
    ability_alias_dict = load_alias_dict('能力项_alias_dict.json')
    language_alias_dict = load_alias_dict('语言_alias_dict.json')

    df = update_df(df, '主题', theme_alias_dict)
    df = update_df(df, '能力项', ability_alias_dict)
    df = update_df(df, '语言', language_alias_dict)

    df.to_excel('v3d0_no_category_还原.xlsx', index=False)


if __name__ == "__main__":
    main()
