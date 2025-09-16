import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

#HTTP地址:端口号
COMFYUI_API_URL="http://127.0.0.1:8188"
#工作流模板路径
WORKFLOW_TEMPLATE_PATH=os.path.join(BASE_DIR,"workflows/ltxv_text_to_video.json")
#视频输出路径
VIDEO_OUTPUT_PATH=os.path.join(BASE_DIR,"output_video")
#视频输出名
VIDEO_FILENAME_TEMPLATE="video_{timestamp}.webp"


