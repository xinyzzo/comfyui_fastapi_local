"""import json
import requests

# 加载你的 workflow 模板（未修改任何内容的原始版本）
with open("workflows/ltxv_text_to_video.json", "r", encoding="utf-8") as f:
    workflow = json.load(f)

# 构造 API 正确格式
request_data = {
    "prompt": workflow,
    "prompt_inputs": {
        "41": {}  # ✅ 节点 41 是 SaveAnimatedWEBP，表示从此节点往上执行整条链
    }
}

response = requests.post("http://127.0.0.1:8188/prompt", json=request_data)

print("状态码：", response.status_code)
print("响应内容：", response.text)
"""