# %%
from langchain_community.document_loaders import PyPDFLoader
import os
files = os.listdir('data-test')
for file in files:
    loader = PyPDFLoader(f'data-test/{file}')
    docs = loader.load()
    with open('all_data.txt', 'a') as f:
        for doc in docs:
            doc.page_content = doc.page_content.replace('\n', '')
            f.write(doc.page_content)
# print(docs)
# print(len(docs))
# with open('exam

# %%
with open('example.txt', 'a') as f:
    for doc in docs:
        doc.page_content = doc.page_content.replace('\n', '')
        f.write(doc.page_content)

# %% [markdown]
# 

# %%
#eval('["quadtree", "data structure", "point cloud", "representation", "compression"]')

# %%



