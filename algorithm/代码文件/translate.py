import random
from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role

def translate(string:str):
    prompt = ["如果句子是中文则翻译成英文，如果句子是英文则翻译成中文，返回翻译结果"]
    messages = [
        {'role': Role.SYSTEM, 'content': "翻译句子（句子为英文则翻译为中文，句子为中文则翻译为英文），返回翻译结果"},
            {'role': 'user', 'content':string}]
    response = dashscope.Generation.call(
        'qwen2-7b-instruct',
        messages=messages,
        #prompt= prompt,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        result_format='message',  # set the result to be "message" format.
    )
    
    if response.status_code == HTTPStatus.OK:
        string = response.output['choices'][0]['message']['content']
        string = string.strip('\n')

        return string
    else:  
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return None
if __name__ == '__main__':
    translate("The hybrid five-level single-phase rectifier proposed in the paper utilizes a quadtree data structure for efficient point cloud representation and compression.")