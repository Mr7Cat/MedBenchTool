# MedBenchTool

## 1. 环境配置

```bash
conda create -n medbench python=3.10
```

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

## 3. 部署模型
e.g qwen2.5-7b-instruct

```bash
python3 -m vllm.entrypoints.openai.api_server --model /root/model/qwen/Qwen2___5-7B-Instruct --trust-remote-code  --tensor-parallel-size 1 --gpu-memory-utilization 0.75 --max-model-len 4096 --rope-scaling "{\"type\":\"yarn\",\"factor\":4.0,\"original_max_position_embeddings\": 131072}" --served-model-name qwen2.5-7b
```

## 4. 运行MedBenchTool

```bash
python run_medbench.py
```

## 5. 查看生成的数据

```bash
ls -l
total 424
-rw-r--r--  1 Will  staff  139521 Nov  5 14:56 CHIP-CTC_test.jsonl
-rw-r--r--  1 Will  staff   15805 Nov  5 14:58 MedMC_test.jsonl
....
```




## 6. 提交数据

https://medbench.opencompass.org.cn/medbench-submission
