from pydantic import BaseModel,Field
import random


S_seed=random.randrange(0,10**16)

class Video_Request_Params(BaseModel):
    prompt: str = Field(...,description="视频生成的正面提示词")
    negative_prompt: str = Field(
        "low quality, worst quality, deformed, distorted, disfigured",
        description="视频生成的负面提示词")
    fps:int =Field(default=24,description="视频帧率")
    quality:int = Field(default=90,description="视频质量")
    width:int = Field(default=640,description="视频宽度")
    height:int = Field(default=360,description="视频高度")
    length:int = Field(default=72)
    sampler_seed:int =Field(default=S_seed,description="噪波种子值")
    sampler_cfg:float=Field(default=3.2,description="提示词相关度")
    steps:int = Field(default=20,description="视频生成步长，影响图形质量")






