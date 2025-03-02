import pandas as pd

def lst_to_csv(lst):
# 创建一个列表

    # 创建一个DataFrame
    df = pd.DataFrame({'id': range(1, len(lst) + 1), 'answer': lst})

    # 设置列名
    df.columns = ['id', 'answer']

    # 将DataFrame写入.csv文件
    df.to_csv('D:\Langchain-Chatchat\webui_pages\dialogue\\result_b.csv', index=False,encoding='utf-8')

if __name__ =="__main__":
    lst_to_csv(['h','k'])
