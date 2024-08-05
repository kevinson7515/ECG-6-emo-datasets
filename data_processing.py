import pandas as pd
import json

# 读取 Excel 文件
df = pd.read_excel('ecg_3_positive_emo.xlsx')

# 创建 JSON 数据结构
data = []
for i, row in df.iterrows():
    conversation = {
        "conversation": [
            {
                # "system": "现在你是一个冷酷恶棍潘多拉,请你用暴躁的语气回复我。",
                "system": "现在你是一个温柔御姐爱丽丝，请你用温柔的口吻回复我。",
                "input": row['post'],
                "output": row['response']
            }
        ]
    }
    data.append(conversation)

# 将数据写入 JSON 文件
with open('ecg_3_positive_emo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)