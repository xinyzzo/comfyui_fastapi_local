import json
import requests
import os
import time
from datetime import datetime
from config import COMFYUI_API_URL,VIDEO_OUTPUT_PATH,VIDEO_FILENAME_TEMPLATE,WORKFLOW_TEMPLATE_PATH
from models import Video_Request_Params


#comfyui默认输出目录
COMFYUI_OUTPUT_DIR = r"D:\comfyui\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\ComfyUI\output"

def wait_for_video_output(filename_prefix: str, timeout: int = 300) -> str:

    #轮询 ComfyUI 默认输出目录，查找以 filename_prefix 开头的视频文件
    #timeout：最多等待时间（秒）
    #返回生成的完整文件路径

    waited = 0
    while waited < timeout:
        for file in os.listdir(COMFYUI_OUTPUT_DIR):
            if file.startswith(filename_prefix) and file.endswith(".webp"):
                return os.path.join(COMFYUI_OUTPUT_DIR, file)
        time.sleep(3)
        waited += 3
    raise Exception(f"超时未找到生成视频文件，前缀={filename_prefix}")



def create_video(req_par:Video_Request_Params)->str:
    with open(WORKFLOW_TEMPLATE_PATH, "r", encoding="utf-8")as f:
        workflow=json.load(f)

    #生成时间戳、设置文件名前缀
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_prefix = f"video_{timestamp}"

    #替换参数
    workflow["6"]["inputs"]["text"]=req_par.prompt                   #正面提示词
    workflow["7"]["inputs"]["text"]=req_par.negative_prompt          #负面提示词
    workflow["41"]["inputs"]["fps"]=req_par.fps                      #视频帧率
    workflow["41"]["inputs"]["quality"]=req_par.quality              #视频质量
    workflow["70"]["inputs"]["width"]=req_par.width                  #视频宽度
    workflow["70"]["inputs"]["height"]=req_par.height                #视频高度
    workflow["70"]["inputs"]["length"]=req_par.length                #视频长度
    workflow["72"]["inputs"]["noise_seed"]=req_par.sampler_seed      #噪波种子值
    workflow["72"]["inputs"]["cfg"]=req_par.sampler_cfg              #提示词相关度
    workflow["71"]["inputs"]["steps"]=req_par.steps                  #视频生成步长

    workflow["41"]["inputs"]["filename_prefix"]=filename_prefix

    #print("🚨 准备发送给 ComfyUI 的 workflow：")
    #print(json.dumps(workflow, indent=2, ensure_ascii=False))

    #将请求发送至comfyui
    response = requests.post(f"{COMFYUI_API_URL}/prompt", json={
    "prompt": workflow,
    "prompt_inputs": {
        "41": {}
     }
})
    response.raise_for_status()

    prompt_id=response.json().get("prompt_id")
    if not prompt_id:
        raise Exception("没有prompt_id从comfyui返回")

    print(f"🚨 已发送给 ComfyUI 的 prompt_id：{prompt_id}")

    output_path = wait_for_video_output(filename_prefix)

    if not os.path.exists(output_path):
        raise Exception(f"video file not found:{output_path}")

    return output_path

