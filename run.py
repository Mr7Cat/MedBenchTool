import os
import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url = 'http://*****/v1'
)

def call_openai_api(question):
    
    messages = [{"role": "user", "content": question}]
    try:
        # 调用OpenAI的API接口
        response = client.chat.completions.create(
            model="YOUR_MODEL",
            messages=messages,
            temperature=0.7
        )
        # 返回生成的文本
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return ""

def process_jsonl_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # 加载每一行的JSON数据
            data = json.loads(line.strip())
            question = data.get("question", "")
            if question:
                # 获取API返回的回答
                answer = call_openai_api(question)
                # 添加answer字段
                data['answer'] = answer
            # 将新的结果写入输出文件
            json.dump(data, outfile, ensure_ascii=False)
            outfile.write('\n')

# 获取 MedBench 目录下所有 _test.jsonl 文件
medbench_dir = './MedBench'
output_dir = './output/MedBench'  # 指定输出目录

# 如果输出目录不存在，则创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk(medbench_dir):
    for file in files:
        if file.endswith('_test.jsonl'):
            input_file = os.path.join(root, file)
            output_file = os.path.join(output_dir, file)  # 输出文件路径与输入文件名相同

            process_jsonl_file(input_file, output_file)
