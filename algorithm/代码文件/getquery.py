import pandas as pd
#From translate import translate
from translate import translate
data = pd.read_csv(r'test_B.csv',encoding='utf-8')
data1 = data.iloc[:,1]
prompt = []
#print(translate(data1[1],'zh'))
import random
from http import HTTPStatus
import dashscope

hanjian = []
def call_with_messages(string:str):
    #prompt = ["提取句子里面的2个比较长的罕见短语,越罕见越好,返回一个列表,格式为：['罕见短语1', '罕见短语2'],不要加上其他任何内容"]
    messages = [
        {'role': 'system', 'content': "提取句子里面的2个罕见词,每个罕见词不超过八个字且不少于三个字，按照下面的格式返回一个列表:['罕见词1', '罕见词2']"},
            {'role': 'user', 'content':"提取句子里面的2个罕见词,注意每个罕见词不超过八个字且不少于三个字，如果是英文句子则罕见词为两以上个单词组成的词组，越罕见越好,返回一个列表,格式为：['罕见词1', '罕见词2'],不要加上其他任何内容，"+"句子为:"+string}]
    response = dashscope.Generation.call(
        'chatglm3-6b',
        messages=messages,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        result_format='message',  # set the result to be "message" format.
    )
    
    if response.status_code == HTTPStatus.OK:
        string = response.output['choices'][0]['message']['content']
        #print(string.strip('\n').strip(" "))
        string = string.strip('\n').strip(" ")
        print(string)
        list_items = eval(string)
        #print(list_items)
        changyong = ['中兴','ZTE',"data",'中兴通讯','One',"ZTE公司","算法",'point cloud',"网络","network"]
        for i in changyong:
            if i in list_items:
                list_items.remove(i)
        return list_items
    else:  
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return None

#call_with_messages(data1[88])
for i in range(len(data1)):
    trans = translate(data1[i])
    print(data1[i])
    print(trans)
    prompt.append(data1[i]+trans)
    hanjian += call_with_messages(data1[i])
    hanjian += call_with_messages(trans)
    print(hanjian)

# for i in range(len(data1)):
#     zh = translate(data1[i],"zh")
#     en = translate(data1[i],"en")
#     print(zh)
#     print(en)
#     hanjian += call_with_messages(zh)
#     hanjian += call_with_messages(en)
#     prompt.append(zh+en)

df = pd.DataFrame(prompt)
print(df)
df.to_csv('prompt_B.csv', index=False)
print(hanjian)
#print(hanjian)


# import random,os
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# os.chdir('D:\Langchain-Chatchat\webui_pages\dialogue')

# # f_tar = open('example.txt', 'r', encoding='utf-8')


# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=400,
#     chunk_overlap=30,
#     length_function=len,
#     is_separator_regex=False,
# )
# with open('all_data.txt', 'r',encoding='utf-8') as f:
#     lines = f.read()
#     texts = text_splitter.create_documents([lines])
    
# def filter_text_blocks(word_list, text_blocks):
#     """
#     从给定的文本块中过滤出包含单词列表中任意一个单词的块。
    
#     参数:
#     word_list (list): 包含需要检查的单词的列表
#     text_blocks (list): 包含需要检查的文本块的列表
    
#     返回:
#     list: 过滤后的文本块列表
#     """
#     filtered_blocks = []
#     for block in text_blocks:
#         for word in word_list:
#             if word in block.page_content:
#                 if block.page_content not in filtered_blocks:
#                     filtered_blocks.append(block.page_content)
#                 break
#     return filtered_blocks

# # 示例用法



# result = filter_text_blocks(hanjian, texts)
# print(result)
# with open('useful_data.txt', 'w',encoding='utf-8') as f:
#     for line in result:
#         f.write(line)
#         f.write('\n')