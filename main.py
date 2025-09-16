from fastapi import FastAPI,responses,HTTPException
import uvicorn
from fastapi.responses import FileResponse
from models import Video_Request_Params
from comfyui_client import create_video,COMFYUI_OUTPUT_DIR
import config
import os


app_comfyui_api = FastAPI()


@app_comfyui_api.get("/")
async def init():
    print("comfyui_api 已初始化")
    return {
        "message":f"该api接口可通过使用ltxv文生图工作流生成视频",
        "usage":f"请访问{config.COMFYUI_API_URL}/docs查看接口文档"


    }


@app_comfyui_api.post("/generate_video")
async def generate_video(req:Video_Request_Params):
    try:
        video_path=create_video(req)

        filename=os.path.basename(video_path)
        return {
            "status":"视频生成成功！",
            "video_url":f"{config.COMFYUI_API_URL}/videos/{filename}"
        }
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


@app_comfyui_api.get("/video/{filename}")
async def get_video(filename:str):
    file_path=os.path.join(COMFYUI_OUTPUT_DIR,filename)
    if os.path.exists(file_path):
        return FileResponse(file_path,media_type='video/webp')
    raise HTTPException(status_code=404,detail="Video not found")

