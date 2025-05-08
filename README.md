
# 智能审计系统（AI Audit System）

本项目为一个面向中小企业与数据审计场景的全流程智能审计平台，集成多个模块，实现从原始PDF或图像账单中提取结构化数据，再通过大语言模型进行分类分析、异常检测、法规比对、自动报告撰写及可视化呈现，支持图形界面交互。

项目由以下功能模块构成：

- OCR文件识别与格式化
- 风险分析及异常检测模型
- 法规推送模拟接口构建及前端页面功能整合
- 智能问答机器人
- 账单分类统计并图表可视化

## 文件夹结构与功能说明

| 文件夹名称 | 功能描述 |
|------------|----------|
| `AuditAdvisor` | 智能问答机器人模块，基于 OpenAI 或 DeepSeek 实现财务审计领域的自然语言问答接口 |
| `AuditAndCompliance-main` | 风险分析与异常检测模型模块，整合审计流程逻辑与前端接口（如 FastAPI / PyQt5），同时包含 Teams 推送模拟功能，负责综合展示和主流程调度 |
| `Audit-chart` | 账单分类与图表生成模块，支持对分类结果进行 Excel/Markdown 导出、可视化图表绘制 |
| `ocr-main` | OCR识别与结构格式化模块，负责提取PDF、图像中的账单表格结构数据，支持 PaddleOCR、PyMuPDF、pdfplumber 等方式 |
| `test` | 测试与验证目录，存放系统各模块的样例账单文件、接口调试脚本、运行结果样例，用于开发与功能验证 |

## API 接口与环境配置说明

在运行项目前，请完成以下接口替换操作：

### 1. 替换大语言模型 API Key

在项目中的各模块代码中（如 `report_generation.py`、`anomaly_detection.py` 等），将以下代码中的占位内容替换为你自己申请的有效接口密钥：

```python
AZURE_OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

如使用 DeepSeek 模型，请至其官方网站申请：

API申请地址（DeepSeek）：https://platform.deepseek.com/usercenter/apikey

接口文档参考：https://platform.deepseek.com/docs

### 2. 替换 Microsoft Teams 群推送 Webhook 地址

在 `AuditAndCompliance-main` 文件夹中的 `.env` 文件内：

```
TEAMS_WEBHOOK_URL=https://mock-teams-webhook.com/webhook
```

请将其替换为你实际创建的 Teams 群组通知接口地址。该地址可在 Teams 群组的“连接器”功能中生成。

## 安装与依赖

请使用 Python 3.9 环境运行，建议在虚拟环境中安装以下依赖。你可通过以下命令进行配置：

```
pip install -r requirements.txt
```

主要依赖如下：

```
paddleocr==2.7.0.3
paddlepaddle==3.0.0
PyMuPDF==1.20.0
pdfplumber==0.11.6
pytesseract==0.3.10
opencv-python==4.6.0.66
gradio==5.29.0
fastapi==0.115.12
Flask==3.1.0
PyQt5==5.15.11
pandas==2.2.0
matplotlib==3.10.1
openpyxl==3.1.2
python-docx==1.1.2
requests==2.31.0
python-multipart==0.0.20
uvicorn==0.24.0
```

requirements.txt 已生成：[点击下载](sandbox:/mnt/data/requirements.txt)
