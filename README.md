# 面向专业招聘的简历分析智能体
本项目是一个基于Ollma本地部署大模型的简历分析智能体，能够实现多种格式的简历自动解析、候选人简历理解、岗位需求智能匹配、输出结构化推荐建议。

## 功能特点
+ 多种格式的简历文本解析与关键信息提取
+ 基于大语言模型的简历与岗位需求的匹配度评估
+ 详细的匹配分析报告输出（结构化的推荐建议、优势、短板分析）

## 项目结构
+ data/resumes存放所有候选人简历
+ 主程序在根目录的ResumeAgent.py
  
## 快速上手
### 环境配置
1. 克隆仓库
``` bash
git clone https://github.com/yourusername/ResumeAgent.git
cd ResumeAgent
```

2. 创建并激活虚拟环境并安装依赖
``` bash
conda create -n ResumeAgent python=3.12 -y
pip install -r requirements.txt
```

3. 安装并配置ollama

+ 从Ollama官网(https://ollama.com/)下载
+ 拉取所需模型
  ``` bash
  ollama pull mistral:7b
  ```
  
### 使用方法
1. 启动ollama
  ``` bash
  ollama serve
  ```

2. 激活环境
   ``` bash
   source activate ResumeAgent
   或者
   conda activate ResumeAgent
   ```
3. 将简历放入data/resumes文件夹里面（命名为candidate1.pdf、candidate2.pdf、...、candidaten.pdf）

4. 根据需要的岗位要求JD更改ResumeAgent.py
 
   只需更改job_description即可

5. 运行根目录下的ResumeAgent.py
``` bash
python ResumeAgent.py
```

1. 在根目录生成详细的结果

## 问题提问
+ 欢迎通过Issue提交和Pull Request来帮助持续改进此项目。
+ 发送邮件至zhoushenbo23@mails.ucas.ac.cn
