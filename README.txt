comfyui_fastapi_local
=====================

使用 FastAPI 封装 ComfyUI 的本地接口服务，方便程序化调用与集成。

功能特性
--------
- 提供 REST API 接口来调用 ComfyUI
- 本地运行，无需远程依赖
- 支持自定义配置与扩展

项目结构
--------
comfyui_fastapi_local/
├── main.py              # FastAPI 应用入口
├── config.py            # 配置文件
├── models.py            # 请求与响应数据模型
├── comfyui_client.py    # 与 ComfyUI 的交互逻辑
├── requirements.txt     # 依赖列表
├── test.py              # 测试脚本


快速开始
--------
1. 克隆仓库
   git clone https://github.com/xinyzzo/comfyui_fastapi_local.git
   cd comfyui_fastapi_local

2. 安装依赖
   pip install -r requirements.txt

3. 启动服务
   uvicorn main:app --reload

4. 访问接口
   打开浏览器访问: http://127.0.0.1:8000/docs


注意事项
- 确保本地已配置并能正常运行 ComfyUI
- 如果调用涉及大模型，需要注意内存和性能开销
- 根据需求修改 config.py 来适配你的环境


