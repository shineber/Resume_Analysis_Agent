# import pdfplumber
# import ollama
# import textwrap

# def extract_text_from_pdf(pdf_path):
#     """从PDF简历中提取文本内容"""
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text

# def evaluate_resume(jd, resume_text):
#     """使用qwen模型评估简历匹配度"""
#     # 构造提示词
# #     prompt = textwrap.dedent(f"""
# #     你是一个专业的招聘专家，请严格根据以下职位描述(JD)评估候选人简历：
# #     ========= 职位描述 =========
# #     {jd}
# #     ========= 简历内容 =========
# #     {resume_text[:8000]}  # 限制输入长度

# #     请按照以下结构化格式输出评估结果：
# #     1. 总体匹配度评分（满分10分）
# #     2. 候选人的主要优势（列举3-5点）
# #     3. 候选人的主要短板（列举2-4点）
# #     4. 是否推荐该候选人进入下一轮面试？为什么？（50-100字）
# #     请按照以下结构化格式输出评估结果：
# #     1. 总体匹配度评分（满分10分）
# #     2. 候选人的主要优势（列举3-5点）
# #     3. 候选人的主要短板（列举2-4点）
# #     4. 是否推荐该候选人进入下一轮面试？为什么？（50-100字）

# #     输出要求：
# #     - 评分基于JD要求与简历内容的匹配程度
# #     - 优势和短板需具体说明与JD的相关性
# #     - 使用简洁专业的语言
# #     """)
    
#     prompt = textwrap.dedent(f"""
#     你是一个专业的招聘专家，请严格根据以下职位描述(JD)评估候选人简历：
#     ========= 职位描述 =========
#     {jd}
#     ========= 简历内容 =========
#     {resume_text[:8000]}  # 限制输入长度

#     请按照以下结构化格式输出评估结果：
#     1. 是否与岗位的要求匹配？
#     2. 候选人的主要优势（列举3-5点）
#     3. 候选人的主要短板（列举2-4点）
#     4. 是否推荐该候选人进入下一轮面试？为什么？（50-100字）

#     输出要求：
#     - 评分基于JD要求与简历内容的匹配程度
#     - 优势和短板需具体说明与JD的相关性
#     - 使用简洁专业的语言
#     """)

#     # 调用Ollama的qwen模型
#     response = ollama.chat(model='qwen', messages=[
#         {'role': 'system', 'content': '你是一个资深计算机行业招聘专家，擅长分析简历与职位的匹配度。'},
#         {'role': 'user', 'content': prompt}
#     ])
    
#     return response['message']['content']

# if __name__ == "__main__":
#     # 用户输入
#     # job_description = input("请输入职位描述(JD): ")
    
# #     job_description = """
# #         职位：Python 开发工程师
        
# #         岗位要求：
# #         1. 本科及以上学历，计算机相关专业
# #         2. 3年以上 Python 开发经验
# #         3. 熟悉 Django/Flask 等 Web 框架
# #         4. 熟悉 MySQL、Redis 等数据库
# #         5. 有良好的代码风格和文档习惯
# #         6. 有团队协作精神和沟通能力
        
# #         工作职责：
# #         1. 负责公司核心业务系统的设计和开发
# #         2. 参与系统架构设计和技术方案制定
# #         3. 编写技术文档和单元测试
# #         4. 解决系统运行中的技术问题
# #         """
    
#     job_description = """
#         职位：生产型会计
        
#         岗位职责：
#         1、 负责生产型企业的账务处理，各项成本费用，包括原材料、人工、制造费用等；
#         2、 完成月度成本报告和财务报表；
#         3、 参加每月末的存货盘点、库存准确率、帐实相符性
#         4、 完成领导安排的其他事宜。
        
#         任职要求：
#         1、 本科以上学历，财务会计相关专业，具备会计中级职称
#         2、 3年以上财务工作经验，3年以上制造业财务相关工作经验，3年以上硬件成本核算经验，有工厂成本核算经验优先考虑
#         3、 熟悉供应链业务流程
#         4、 熟悉用友ERP操作，熟练掌握基本的办公软件，如word、excel、ppt等
#         5、 具有较强的责任心和良好的沟通协调能力，有一定抗压能力，学习意愿强。
#         """
    
#     # resume_path = input("请输入简历PDF文件路径: ")
#     resume_path = "./ResumeAgent_V1/data/resumes/candidate1.pdf"
    
#     # 处理PDF
#     resume_text = extract_text_from_pdf(resume_path)
#     print("\n简历文本提取完成，开始评估...\n")
#     print(resume_text)
    
#     # 获取评估结果
#     result = evaluate_resume(job_description, resume_text)
    
#     # 输出结果
#     print("="*50)
#     print("简历匹配评估报告：")
#     print("="*50)
#     print(result)
#     print("="*50)



### 读取单个简历跑通 ###

# import pdfplumber
# import ollama
# import textwrap
# import time

# def extract_text_from_pdf(pdf_path):
#     """从PDF简历中提取文本内容"""
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text

# def evaluate_resume(jd, resume_text):
#     """使用DeepSeek模型评估简历匹配度"""
#     # 构造提示词 - 针对DeepSeek模型优化
#     prompt = textwrap.dedent(f"""
#     ### 角色
#     你是一位制造业资深招聘专家，擅长分析简历与职位的匹配度。
    
#     ### 任务
#     根据以下职位描述(JD)评估候选人简历：
    
#     ========= 职位描述 =========
#     {jd}
    
#     ========= 简历内容 =========
#     {resume_text[:12000]}  # 增加输入长度限制
    
#     ### 评估要求（不用输出）
#     请按照以下结构化格式输出评估结果：
#     1. 是否与任职要求的要求匹配？（是/部分符合/否）
#     2. 对于候选人的学历，需要检索是否是985/211院校，并对比岗位要求里的学历要求。
#     2. 候选人的主要优势和短板（优势和短板不需要和岗位描述保持一致，但是一定要严格对应简历）
#     3. 要求候选人技能和任职要求严格匹配（至少满足一半的要求）
#     4. 是否推荐该候选人进入下一轮面试（回答推荐或者不推荐）？
    
#     ### 输出内容（这部分需要输出）
#     - 是否推荐候选人进入面试？（至少满足一半的任职要求才能推荐进入）
#     - 优势和短板（需具体说明与JD的相关性）
#     - 确保输出是和简历、职位描述是严格匹配的，不要输出无关内容，如果不满足候选人技能和任职要求严格匹配（至少满足一半的要求），直接认为是不推荐的。
#     """)

#     # 调用Ollama的DeepSeek模型 - 使用7B参数版本
#     try:
#         start_time = time.time()
#         response = ollama.chat(
#             model='deepseek-llm:7b',  # 使用7B参数版本，适合24GB显存
#             messages=[
#                 {'role': 'system', 'content': '你专注于计算机岗位的简历评估，特别关注计算机的技能经验和工作年限。'},
#                 {'role': 'user', 'content': prompt}
#             ],
#             options={
#                 'num_ctx': 8192,  # 更大的上下文窗口
#                 'temperature': 0.001  # 更低的随机性，确保专业评估
#             }
#         )
#         processing_time = time.time() - start_time
#         print(f"模型处理时间: {processing_time:.2f}秒")
#         return response['message']['content']
#     except Exception as e:
#         print(f"模型调用错误: {str(e)}")
#         return "评估失败，请检查模型是否已下载或服务是否运行"

# def save_evaluation_report(result, output_file="评估报告.txt"):
#     """保存评估报告到文件"""
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write("="*50 + "\n")
#         f.write("简历匹配评估报告\n")
#         f.write("="*50 + "\n")
#         f.write(result)
#     print(f"评估报告已保存至: {output_file}")

# if __name__ == "__main__":
#     # 检查Ollama服务
#     print("检查可用模型...")
#     try:
#         models = ollama.list()['models']
#         print(f"可用模型: {[m['name'] for m in models]}")
#         if not any('deepseek' in m['name'] for m in models):
#             print("警告: 未找到DeepSeek模型，请使用 'ollama pull deepseek-llm:7b' 下载")
#     except:
#         print("无法连接Ollama服务，请确保Ollama已运行")
    
#     # 职位描述
# #     job_description = """
# #     职位：数字设计工程师
    
# #     岗位职责：
# #     1.带领数字团队负责MCU产品数字IP或集成设计实现和验证；
# #     2.和架构，模拟及后端等其它团队合作评估并制定设计规格；
# #     3.和测试应用等其它团队合作分析解决芯片设计问题；
# #     4.推动或参与设计流程改进和优化；
# #     5.负责本团队建设和员工培养。
    
# #     任职要求：
# #     1.微电子，电子工程或相关专业本科及以上；
# #     2.5年以上MCU或大规模SoC直接相关产品设计经验；
# #     3.具有32位ARM Based产品设计经验，熟悉AMBA总线协议
# #     4.具有良好的数字电路原理知识，有实际数字电路设计和成功流片经验；
# #     5.熟练掌握数字电路设计流程及方法学，熟悉相关EDA设计和验证工具；
# #     6.具有深亚微米(如40nm)产品设计经验优先；
# #     7.具有高性能MCU或车规产品设计经验优先，熟悉ISO26262功能安全标准和设计优先；
# #     8.具有一定团队管理经验或项目管理能力;
# #     9.具有良好的学习能力、团队精神、责任感和沟通能力。
# #     """
    
# #     job_description = """
# #     职位：应用层软件开发工程师（功能安全方向）_BCSC 
    
# #     岗位职责：
# #     主要工作内容： 

# #     1.负责动力域相关控制器L2的功能安全软件开发及验证. 

# #     2.解读功能安全系统FSR, TSR，熟悉动力域控制器L2系统架构，针对需求进行影响分析，需求分解和软件设计 

# #     3.编写功能安全L2软件需求文档，软件架构设计 

# #     4.进行功能安全L2软件代码实现 

# #     5.负责功能安全L2软件单元测试，软件需求验证 

# #     6.基于架构进行安全分析，包括故障树分析，相关性失效分析，FMEA等 

# #     7.进行软件bug分析和修复 

# #     任职要求：
# #     1.熟悉动力域相关控制器系统知识，如ECU,VCU,TCU,MCU等系统知识 
# #     2.熟悉ISO 26262/ IEC61508, E-gas 等 
# #     3.熟悉当前功能安全最先进设计思路及方案（state of art） 
# #     4.熟练使用各类安全分析工具，如IQ-RM, isograph等 
# #     5.熟悉Simulink/ASCET, C语言 
# #     6.功能安全L2软件开发经验3年及以上 
# #     7.良好的英语读写/沟通能力 
# #     """

#     job_description = """
#         职位：辅助驾驶规控软件开发工程师 

#         岗位职责：
#         主要工作内容： 

#         1. 负责客户需求的分析；
#         2. 负责商用车ADAS运动控制软件开发，进行需求分解与软件设计；
#         3. 支持产品开发及质量流程相关工作；
#         4. 支持车辆匹配，完成运动控制功能的车辆调试；
#         5. 与项目团队成员保持协作，共同应对全新挑战。

#         任职要求：
#         1. 985硕士以上学历；
#         2. 熟练掌握C++, C编程语言；MATLAB建模；
#         3. 嵌入式系统开发经验尤佳；
#         4. 积极主动，优秀的沟通能力和团队合作精神；
#         5. 英语听说读写流利；
#         6. 积极融入并在国际化的团队中发挥作用；
#         7. 工作地无锡，同时可以全职在岗超过4个月。
#     """
    
#     # 简历路径 - 替换为您的实际路径
#     resume_path = "./data/resumes/candidate1.pdf"
#     # resume_path = input("请输入简历PDF文件路径: ")
    
#     print("\n开始处理简历...")
#     resume_text = extract_text_from_pdf(resume_path)
#     print(f"简历文本提取完成，共{len(resume_text)}字符")
    
#     print("\n开始评估简历匹配度...")
#     result = evaluate_resume(job_description, resume_text)
    
#     # 输出结果
#     print("\n" + "="*50)
#     print("简历匹配评估报告：")
#     print("="*50)
#     print(result)
#     print("="*50)
    
#     # 保存评估报告
#     save_evaluation_report(result)

### END ###



### 批量读取简历并写入Excel ###
# import pdfplumber
# import textwrap
# import ollama
# import os
# import pandas as pd
# import re
# import time
# from datetime import datetime

# def extract_text_from_pdf(pdf_path):
#     """从PDF简历中提取文本内容"""
#     text = ""
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
#         return text
#     except Exception as e:
#         print(f"读取PDF失败: {pdf_path}, 错误: {str(e)}")
#         return ""

# def evaluate_resume(jd, resume_text):
#     """使用DeepSeek模型评估简历匹配度"""
#     # 构造优化后的提示词
# #     prompt = textwrap.dedent(f"""
# #     ### 角色
# #     你是制造业资深招聘专家，正在评估简历与职位描述的匹配度。
    
# #     ### 职位描述
# #     {jd}
    
# #     ### 简历内容
# #     {resume_text[:10000]}  # 限制输入长度
    
# #     ### 评估任务
# #     请严格按以下要求输出评估结果：
# #     1. 从简历中提取候选人姓名
# #     2. 分析最高学历院校（标注是否985/211）
# #     3. 评估是否推荐进入面试（满足至少一半任职要求才推荐）
# #     4. 列出主要优缺点（需具体说明与JD的相关性）
    
# #     ### 输出格式
# #     <姓名>候选人姓名</姓名>
# #     <学历院校>最高学历院校 (985/211/普通)</学历院校>
# #     <是否推荐>推荐/不推荐</是否推荐>
# #     <优缺点>
# #     - 优势1
# #     - 优势2
# #     - 短板1
# #     - 短板2
# #     </优缺点>
# #     """)
    
#     prompt = textwrap.dedent(f"""
#     ### 角色
#     你是一位制造业资深招聘专家，擅长分析简历与职位的匹配度。
    
#     ### 任务
#     根据以下职位描述(JD)评估候选人简历：
    
#     ========= 职位描述 =========
#     {jd}
    
#     ========= 简历内容 =========
#     {resume_text[:12000]}  # 增加输入长度限制
    
#     ### 评估要求（不用输出）
#     请按照以下结构化格式输出评估结果：
#     1. 是否与任职要求的要求匹配？（是/部分符合/否）
#     2. 对于候选人的学历，需要检索是否是985/211院校，并对比岗位要求里的学历要求。
#     2. 候选人的主要优势和短板（优势和短板不需要和岗位描述保持一致，但是一定要严格对应简历）
#     3. 要求候选人技能和任职要求严格匹配（至少满足一半的要求）
#     4. 是否推荐该候选人进入下一轮面试（回答推荐或者不推荐,至少满足一半的任职要求才能推荐进入）？
    
#     ### 输出内容（这部分需要输出）
#     <姓名>候选人姓名</姓名>
#     <学历院校>最高学历院校 (985/211/普通)</学历院校>
#     <是否推荐（确保输出是和简历、职位描述是严格匹配的，不要输出无关内容，如果不满足候选人技能和任职要求严格匹配（至少满足一半的要求），直接认为是不推荐的。）>推荐/不推荐</是否推荐>
#     <优缺点（需具体说明与JD的相关性）>
#     - 优势1
#     - 优势2
#     - 短板1
#     - 短板2
#     </优缺点>
#     """)

#     try:
#         start_time = time.time()
#         response = ollama.chat(
#             model='deepseek-llm:7b',
#             messages=[
#                 {'role': 'system', 'content': '你专注于技术岗位的简历评估，特别关注技能匹配度和学历背景'},
#                 {'role': 'user', 'content': prompt}
#             ],
#             options={
#                 'num_ctx': 8192,
#                 'temperature': 0.001
#             }
#         )
#         processing_time = time.time() - start_time
#         print(f"模型处理时间: {processing_time:.2f}秒")
#         return response['message']['content']
#     except Exception as e:
#         print(f"模型调用错误: {str(e)}")
#         return ""

# def parse_evaluation_result(result_text):
#     """解析模型评估结果"""
#     data = {
#         "姓名": "未识别",
#         "最高学历院校": "未识别",
#         "是否推荐": "不推荐",
#         "优缺点": "解析失败"
#     }
    
#     try:
#         # 使用正则表达式提取结构化数据
#         name_match = re.search(r'<姓名>(.*?)</姓名>', result_text, re.DOTALL)
#         school_match = re.search(r'<学历院校>(.*?)</学历院校>', result_text)
#         recommend_match = re.search(r'<是否推荐>(.*?)</是否推荐>', result_text)
#         pros_cons_match = re.search(r'<优缺点>(.*?)</优缺点>', result_text, re.DOTALL)
        
#         if name_match: data["姓名"] = name_match.group(1).strip()
#         if school_match: data["最高学历院校"] = school_match.group(1).strip()
#         if recommend_match: data["是否推荐"] = recommend_match.group(1).strip()
#         if pros_cons_match: 
#             # 清理多余空格和换行
#             pros_cons = pros_cons_match.group(1).strip()
#             pros_cons = re.sub(r'\n\s+', '\n- ', pros_cons)
#             data["优缺点"] = pros_cons
            
#         return data
#     except Exception as e:
#         print(f"结果解析失败: {str(e)}")
#         return data

# if __name__ == "__main__":
#     # 检查Ollama服务
#     print("检查可用模型...")
#     try:
#         models = ollama.list()['models']
#         print(f"可用模型: {[m['name'] for m in models]}")
#         if not any('deepseek' in m['name'] for m in models):
#             print("警告: 未找到DeepSeek模型，请使用 'ollama pull deepseek-llm:7b' 下载")
#     except:
#         print("无法连接Ollama服务，请确保Ollama已运行")
    
#     # 职位描述
#     job_description = """
#     职位：辅助驾驶规控软件开发工程师 
    
#     岗位职责：
#     1. 负责客户需求的分析
#     2. 负责商用车ADAS运动控制软件开发
#     3. 支持产品开发及质量流程相关工作
#     4. 支持车辆匹配调试
#     5. 与项目团队协作
    
#     任职要求：
#     1. 985硕士以上学历
#     2. 熟练掌握C++, C编程语言；MATLAB建模
#     3. 嵌入式系统开发经验尤佳
#     4. 优秀的沟通能力和团队合作精神
#     5. 英语听说读写流利
#     6. 工作地无锡，全职在岗超过4个月
#     """
    
#     # 准备数据收集
#     results = []
#     pdf_folder = "./data/resumes/"
#     processed_count = 0
    
#     # 遍历文件夹中的所有PDF文件
#     for filename in os.listdir(pdf_folder):
#         if filename.lower().endswith('.pdf'):
#             pdf_path = os.path.join(pdf_folder, filename)
#             print(f"\n处理简历: {filename}")
            
#             # 提取文本
#             resume_text = extract_text_from_pdf(pdf_path)
#             if not resume_text:
#                 print(f"跳过空文件: {filename}")
#                 continue
#             print(f"简历文本提取完成，共{len(resume_text)}字符")
            
#             # 评估简历
#             print("开始评估简历匹配度...")
#             eval_result = evaluate_resume(job_description, resume_text)
            
#             # 解析结果
#             parsed_data = parse_evaluation_result(eval_result)
#             parsed_data["文件名"] = filename  # 保留原始文件名
#             results.append(parsed_data)
#             processed_count += 1
            
#             # 显示进度
#             print(f"【{parsed_data['姓名']}】评估完成: {parsed_data['是否推荐']}")
    
#     # 保存到Excel
#     if results:
#         df = pd.DataFrame(results)
#         # 调整列顺序
#         df = df[['姓名', '最高学历院校', '是否推荐', '优缺点', '文件名']]
        
#         # 生成带时间戳的文件名
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M")
#         excel_path = f"简历评估报告_{timestamp}.xlsx"
        
#         df.to_excel(excel_path, index=False)
#         print(f"\n成功处理{processed_count}份简历，结果已保存至: {excel_path}")
#     else:
#         print("未找到可处理的PDF简历")
### END ###



# import pdfplumber
# import ollama
# import os
# import pandas as pd
# import re
# import time
# from datetime import datetime
# import textwrap

# def extract_text_from_pdf(pdf_path):
#     """从PDF简历中提取文本内容"""
#     text = ""
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
#         return text
#     except Exception as e:
#         print(f"读取PDF失败: {pdf_path}, 错误: {str(e)}")
#         return ""

# def evaluate_resume(jd, resume_text):
#     """使用DeepSeek模型评估简历匹配度"""
#     # 使用优化后的提示词
#     prompt = textwrap.dedent(f"""
#     ### 角色
#     你是一位制造业资深招聘专家，擅长分析简历与职位的匹配度。
    
#     ### 任务
#     根据以下职位描述(JD)评估候选人简历：
    
#     ========= 职位描述 =========
#     {jd}
    
#     ========= 简历内容 =========
#     {resume_text[:10000]}  # 增加输入长度限制
    
#     ### 评估要求
#     请按照以下结构化格式输出评估结果：
#     1. 从简历中提取候选人姓名
#     2. 分析最高学历院校（标注是否985/211）
#     3. 评估是否推荐进入面试（满足至少一半任职要求才推荐）
#     4. 列出主要优缺点（需具体说明与JD的相关性）
    
#     ### 输出格式（必须严格遵循）
#     <姓名>候选人姓名</姓名>
#     <学历院校>最高学历院校 (985/211/普通)</学历院校>
#     <是否推荐>推荐/不推荐</是否推荐>
#     <优缺点>
#     - 优势1
#     - 优势2
#     - 短板1
#     - 短板2
#     </优缺点>
    
#     ### 注意事项
#     1. 必须使用上述XML标签格式输出，不要添加额外解释
#     2. 如果不确定姓名或院校，使用"未知"
#     3. 优缺点必须基于简历内容，不要编造信息
#     """)

#     try:
#         start_time = time.time()
#         response = ollama.chat(
#             model='deepseek-llm:7b',
#             messages=[
#                 {'role': 'system', 'content': '你专注于技术岗位的简历评估，特别关注技能匹配度和学历背景'},
#                 {'role': 'user', 'content': prompt}
#             ],
#             options={
#                 'num_ctx': 8192,
#                 'temperature': 0.001
#             }
#         )
#         processing_time = time.time() - start_time
#         print(f"模型处理时间: {processing_time:.2f}秒")
#         return response['message']['content']
#     except Exception as e:
#         print(f"模型调用错误: {str(e)}")
#         return ""

# def parse_evaluation_result(result_text):
#     """解析模型评估结果 - 更健壮的解析逻辑"""
#     data = {
#         "姓名": "未识别",
#         "最高学历院校": "未识别",
#         "是否推荐": "不推荐",
#         "优缺点": "解析失败"
#     }
    
#     try:
#         # 更健壮的标签解析逻辑
#         patterns = {
#             "姓名": r'<姓名>\s*(.*?)\s*</姓名>',
#             "最高学历院校": r'<学历院校>\s*(.*?)\s*</学历院校>',
#             "是否推荐": r'<是否推荐>\s*(.*?)\s*</是否推荐>',
#             "优缺点": r'<优缺点>\s*([\s\S]*?)\s*</优缺点>'
#         }
        
#         for key, pattern in patterns.items():
#             match = re.search(pattern, result_text, re.DOTALL)
#             if match:
#                 content = match.group(1).strip()
#                 # 清理内容中的多余标签
#                 content = re.sub(r'</?[a-zA-Z]+>', '', content)
#                 data[key] = content
#             else:
#                 print(f"警告: 未找到'{key}'标签")
        
#         return data
#     except Exception as e:
#         print(f"结果解析失败: {str(e)}")
#         return data

# if __name__ == "__main__":
#     # 检查Ollama服务
#     print("检查可用模型...")
#     try:
#         models = ollama.list()['models']
#         print(f"可用模型: {[m['name'] for m in models]}")
#         if not any('deepseek' in m['name'] for m in models):
#             print("警告: 未找到DeepSeek模型，请使用 'ollama pull deepseek-llm:7b' 下载")
#     except:
#         print("无法连接Ollama服务，请确保Ollama已运行")
    
#     # 职位描述
#     job_description = """
#     职位：辅助驾驶规控软件开发工程师 
    
#     岗位职责：
#     1. 负责客户需求的分析
#     2. 负责商用车ADAS运动控制软件开发
#     3. 支持产品开发及质量流程相关工作
#     4. 支持车辆匹配调试
#     5. 与项目团队协作
    
#     任职要求：
#     1. 985硕士以上学历
#     2. 熟练掌握C++, C编程语言；MATLAB建模
#     3. 嵌入式系统开发经验尤佳
#     4. 优秀的沟通能力和团队合作精神
#     5. 英语听说读写流利
#     6. 工作地无锡，全职在岗超过4个月
#     """
    
#     # 准备数据收集
#     results = []
#     pdf_folder = "./data/resumes/"
#     processed_count = 0
    
#     # 遍历文件夹中的所有PDF文件
#     for filename in os.listdir(pdf_folder):
#         if filename.lower().endswith('.pdf'):
#             pdf_path = os.path.join(pdf_folder, filename)
#             print(f"\n处理简历: {filename}")
            
#             # 提取文本
#             resume_text = extract_text_from_pdf(pdf_path)
#             if not resume_text:
#                 print(f"跳过空文件: {filename}")
#                 continue
#             print(f"简历文本提取完成，共{len(resume_text)}字符")
            
#             # 评估简历
#             print("开始评估简历匹配度...")
#             eval_result = evaluate_resume(job_description, resume_text)
#             print("原始模型输出:")
#             print("-"*50)
#             print(eval_result[:1000])  # 打印部分输出以便调试
#             print("-"*50)
            
#             # 解析结果
#             parsed_data = parse_evaluation_result(eval_result)
#             print("解析结果:")
#             print(f"姓名: {parsed_data['姓名']}")
#             print(f"学历院校: {parsed_data['最高学历院校']}")
#             print(f"是否推荐: {parsed_data['是否推荐']}")
#             print(f"优缺点: {parsed_data['优缺点'][:200]}...")  # 截断显示
            
#             # 添加文件名到数据
#             parsed_data["文件名"] = filename
#             results.append(parsed_data)
#             processed_count += 1
    
#     # 保存到Excel - 修复数据映射问题
#     if results:
#         # 创建DataFrame时直接使用我们需要的列
#         excel_data = []
#         for result in results:
#             excel_data.append({
#                 "姓名": result["姓名"],
#                 "最高学历院校": result["最高学历院校"],
#                 "是否推荐进入面试": result["是否推荐"],
#                 "优缺点": result["优缺点"],
#                 "文件名": result["文件名"]
#             })
        
#         df = pd.DataFrame(excel_data)
        
#         # 调整列顺序
#         df = df[["姓名", "最高学历院校", "是否推荐进入面试", "优缺点", "文件名"]]
        
#         # 生成带时间戳的文件名
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         excel_path = f"简历评估报告_{timestamp}.xlsx"
        
#         # 保存Excel文件
#         df.to_excel(excel_path, index=False, engine='openpyxl')
#         print(f"\n成功处理{processed_count}份简历，结果已保存至: {excel_path}")
        
#         # 显示前几行作为预览
#         print("\nExcel预览:")
#         print(df.head())
#     else:
#         print("未找到可处理的PDF简历")




# import pdfplumber
# import ollama
# import os
# import pandas as pd
# import re
# import time
# from datetime import datetime
# import textwrap

# def extract_text_from_pdf(pdf_path):
#     """从PDF简历中提取文本内容"""
#     text = ""
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
#         return text
#     except Exception as e:
#         print(f"读取PDF失败: {pdf_path}, 错误: {str(e)}")
#         return ""

# def evaluate_resume(jd, resume_text):
#     """使用DeepSeek模型评估简历匹配度"""
#     # 使用优化后的提示词
#     prompt = textwrap.dedent(f"""
#     ### 角色
#     你是一位制造业资深招聘专家，擅长分析简历与职位的匹配度。
    
#     ### 任务
#     根据以下职位描述(JD)评估候选人简历：
    
#     ========= 职位描述 =========
#     {jd}
    
#     ========= 简历内容 =========
#     {resume_text[:10000]}  # 增加输入长度限制
    
#     ### 评估要求
#     请按照以下结构化格式输出评估结果：
#     1. 从简历中提取候选人姓名
#     2. 分析最高学历院校（标注是否985/211）
#     3. 评估是否推荐进入面试（满足至少一半任职要求才推荐）
#     4. 列出主要优缺点（需具体说明与JD的相关性）
    
#     ### 输出格式（必须严格遵循）
#     <姓名>候选人姓名</姓名>
#     <学历院校>最高学历院校 (985/211/普通)</学历院校>
#     <是否推荐>推荐/不推荐</是否推荐>
#     <优缺点>
#     - 优势1
#     - 优势2
#     - 短板1
#     - 短板2
#     </优缺点>
    
#     ### 注意事项
#     1. 必须使用上述XML标签格式输出，不要添加额外解释
#     2. 如果不确定姓名或院校，使用"未知"
#     3. 优缺点必须基于简历内容，不要编造信息
#     """)

#     try:
#         start_time = time.time()
#         response = ollama.chat(
#             model='deepseek-llm:7b',
#             messages=[
#                 {'role': 'system', 'content': '你专注于技术岗位的简历评估，特别关注技能匹配度和学历背景'},
#                 {'role': 'user', 'content': prompt}
#             ],
#             options={
#                 'num_ctx': 8192,
#                 'temperature': 0.001
#             }
#         )
#         processing_time = time.time() - start_time
#         print(f"模型处理时间: {processing_time:.2f}秒")
#         return response['message']['content']
#     except Exception as e:
#         print(f"模型调用错误: {str(e)}")
#         return ""

# def parse_evaluation_result(result_text):
#     """从模型自然语言输出中提取信息"""
#     data = {
#         "姓名": "未识别",
#         "最高学历院校": "未识别",
#         "是否推荐进入面试": "不推荐",
#         "优点": "未识别",
#         "缺点": "未识别"
#     }
    
#     try:
#         # 提取姓名（第一行内容）
#         first_line = result_text.split('\n')[0].strip()
#         if "候选人" in first_line:
#             data["姓名"] = first_line.replace("候选人", "").strip()
#         else:
#             data["姓名"] = first_line
        
#         # 提取最高学历院校（匹配包含"最高学历"的行）
#         for line in result_text.split('\n'):
#             if "最高学历" in line:
#                 data["最高学历院校"] = line.strip()
#                 break
        
#         # 提取是否推荐（匹配"推荐进入面试"或"不推荐"）
#         if "推荐进入面试" in result_text:
#             data["是否推荐进入面试"] = "推荐"
#         elif "不推荐" in result_text:
#             data["是否推荐进入面试"] = "不推荐"
        
#         # 提取优点（"主要优点："之后的内容）
#         if "主要优点：" in result_text:
#             start_idx = result_text.index("主要优点：") + len("主要优点：")
#             end_idx = result_text.find("主要短板：", start_idx)
#             if end_idx == -1:
#                 end_idx = len(result_text)
#             data["优点"] = result_text[start_idx:end_idx].strip()
        
#         # 提取缺点（"主要短板："之后的内容）
#         if "主要短板：" in result_text:
#             start_idx = result_text.index("主要短板：") + len("主要短板：")
#             end_idx = result_text.find("\n\n", start_idx)  # 查找双换行作为结束
#             if end_idx == -1:
#                 end_idx = len(result_text)
#             data["缺点"] = result_text[start_idx:end_idx].strip()
        
#         return data
#     except Exception as e:
#         print(f"结果解析失败: {str(e)}")
#         return data

# if __name__ == "__main__":
#     # 职位描述
#     job_description = """
#     职位：辅助驾驶规控软件开发工程师 
    
#     岗位职责：
#     1. 负责客户需求的分析
#     2. 负责商用车ADAS运动控制软件开发
#     3. 支持产品开发及质量流程相关工作
#     4. 支持车辆匹配调试
#     5. 与项目团队协作
    
#     任职要求：
#     1. 985硕士以上学历
#     2. 熟练掌握C++, C编程语言；MATLAB建模
#     3. 嵌入式系统开发经验尤佳
#     4. 优秀的沟通能力和团队合作精神
#     5. 英语听说读写流利
#     6. 工作地无锡，全职在岗超过4个月
#     """
    
#     # 准备Excel数据
#     excel_data = []
#     pdf_folder = "./data/resumes/"  # 简历文件夹路径
    
#     # 遍历文件夹中的所有PDF文件
#     for filename in os.listdir(pdf_folder):
#         if filename.lower().endswith('.pdf'):
#             pdf_path = os.path.join(pdf_folder, filename)
#             print(f"\n处理简历: {filename}")
            
#             # 提取文本
#             resume_text = extract_text_from_pdf(pdf_path)
#             if not resume_text:
#                 print(f"跳过空文件: {filename}")
#                 continue
#             print(f"简历文本提取完成，共{len(resume_text)}字符")
            
#             # 评估简历
#             print("开始评估简历匹配度...")
#             eval_result = evaluate_resume(job_description, resume_text)
#             print("原始模型输出:")
#             print("-"*50)
#             print(eval_result)  # 打印完整输出
#             print("-"*50)
            
#             # 解析结果
#             parsed_data = parse_evaluation_result(eval_result)
#             print("解析结果:")
#             print(f"姓名: {parsed_data['姓名']}")
#             print(f"最高学历院校: {parsed_data['最高学历院校']}")
#             print(f"是否推荐进入面试: {parsed_data['是否推荐进入面试']}")
#             print(f"优点: {parsed_data['优点'][:100]}...")
#             print(f"缺点: {parsed_data['缺点'][:100]}...")
            
#             # 添加到Excel数据
#             excel_data.append({
#                 "姓名": parsed_data["姓名"],
#                 "最高学历院校": parsed_data["最高学历院校"],
#                 "是否推荐进入面试": parsed_data["是否推荐进入面试"],
#                 "优点": parsed_data["优点"],
#                 "缺点": parsed_data["缺点"]
#             })
    
#     # 保存到Excel
#     if excel_data:
#         # 创建DataFrame
#         df = pd.DataFrame(excel_data)
        
#         # 生成带时间戳的文件名
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         excel_path = f"简历评估报告_{timestamp}.xlsx"
        
#         # 保存Excel文件
#         df.to_excel(excel_path, index=False, engine='openpyxl')
#         print(f"\n成功处理{len(excel_data)}份简历，结果已保存至: {excel_path}")
        
#         # 显示Excel内容预览
#         print("\nExcel内容预览:")
#         print(df)
#     else:
#         print("未找到可处理的PDF简历")




import pdfplumber
import ollama
import os
import pandas as pd
import re
import time
from datetime import datetime
import textwrap

def extract_text_from_pdf(pdf_path):
    """从PDF简历中提取文本内容"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"读取PDF失败: {pdf_path}, 错误: {str(e)}")
        return ""

def evaluate_resume(jd, resume_text):
    """使用DeepSeek模型评估简历匹配度"""
    # 使用优化后的提示词
    prompt = textwrap.dedent(f"""
    ### 角色
    你是一位制造业资深招聘专家，擅长分析简历与职位的匹配度。
    
    ### 任务
    根据以下职位描述(JD)评估候选人简历：
    
    ========= 职位描述 =========
    {jd}
    
    ========= 简历内容 =========
    {resume_text[:10000]}  # 增加输入长度限制
    
    ### 评估要求
    请按照以下结构化格式输出评估结果：
    1. 从简历中提取候选人姓名
    2. 分析最高学历院校（标注是否985/211）
    3. 评估是否推荐进入面试（满足至少一半任职要求才推荐）
    4. 列出主要优缺点（需具体说明与JD的相关性）
    
    ### 输出格式（必须严格遵循）
    <姓名>候选人姓名</姓名>
    <学历院校>最高学历院校 (985/211/普通)</学历院校>
    <是否推荐>推荐/不推荐</是否推荐>
    <优缺点>
    - 优势1
    - 优势2
    - 短板1
    - 短板2
    </优缺点>
    
    ### 注意事项
    1. 必须使用上述XML标签格式输出，不要添加额外解释
    2. 如果不确定姓名或院校，使用"未知"
    3. 优缺点必须基于简历内容，不要编造信息
    """)

    try:
        start_time = time.time()
        response = ollama.chat(
            model='mistral:7b',
            messages=[
                {'role': 'system', 'content': '你专注于技术岗位的简历评估，特别关注技能匹配度和学历背景'},
                {'role': 'user', 'content': prompt}
            ],
            options={
                'num_ctx': 8192,
                'temperature': 0.001
            }
        )
        processing_time = time.time() - start_time
        print(f"模型处理时间: {processing_time:.2f}秒")
        return response['message']['content']
    except Exception as e:
        print(f"模型调用错误: {str(e)}")
        return ""

def parse_evaluation_result(result_text):
    """更健壮的解析逻辑，处理不同格式的输出"""
    data = {
        "姓名": "未识别",
        "最高学历院校": "未识别",
        "是否推荐进入面试": "不推荐",
        "优点": "未识别",
        "缺点": "未识别"
    }
    
    try:
        # 1. 尝试XML标签解析（更可靠）
        if "<姓名>" in result_text and "</姓名>" in result_text:
            name_match = re.search(r'<姓名>(.*?)</姓名>', result_text, re.DOTALL)
            if name_match:
                data["姓名"] = name_match.group(1).strip()
        
        if "<学历院校>" in result_text and "</学历院校>" in result_text:
            school_match = re.search(r'<学历院校>(.*?)</学历院校>', result_text, re.DOTALL)
            if school_match:
                data["最高学历院校"] = school_match.group(1).strip()
        
        if "<是否推荐>" in result_text and "</是否推荐>" in result_text:
            rec_match = re.search(r'<是否推荐>(.*?)</是否推荐>', result_text, re.DOTALL)
            if rec_match:
                data["是否推荐进入面试"] = rec_match.group(1).strip()
        
        if "<优缺点>" in result_text and "</优缺点>" in result_text:
            pros_cons_match = re.search(r'<优缺点>(.*?)</优缺点>', result_text, re.DOTALL)
            if pros_cons_match:
                pros_cons = pros_cons_match.group(1).strip()
                # 尝试从优缺点中分离优点和缺点
                if "优势" in pros_cons or "优点" in pros_cons:
                    pros_match = re.search(r'(优势.*?)(?=短板|缺点|$)', pros_cons, re.DOTALL)
                    if pros_match:
                        data["优点"] = pros_match.group(1).strip()
                
                if "短板" in pros_cons or "缺点" in pros_cons:
                    cons_match = re.search(r'(短板.*?)(?=优势|优点|$)', pros_cons, re.DOTALL)
                    if cons_match:
                        data["缺点"] = cons_match.group(1).strip()
        
        # 2. 如果XML解析失败，尝试自然语言解析
        if data["姓名"] == "未识别":
            # 尝试从第一行提取姓名
            first_line = result_text.split('\n')[0].strip()
            if "候选人" in first_line:
                data["姓名"] = first_line.replace("候选人", "").strip()
            else:
                # 尝试提取中文名字（2-4个中文字符）
                name_match = re.search(r'[\u4e00-\u9fa5]{2,4}', first_line)
                if name_match:
                    data["姓名"] = name_match.group(0)
        
        if data["最高学历院校"] == "未识别":
            # 尝试查找包含"学历"或"院校"的行
            for line in result_text.split('\n'):
                if "学历" in line or "院校" in line:
                    # 提取关键部分
                    school_match = re.search(r'(最高学历|学历院校|院校)[：:](.*?)$', line)
                    if school_match:
                        data["最高学历院校"] = school_match.group(2).strip()
                    else:
                        data["最高学历院校"] = line.strip()
                    break
        
        if data["是否推荐进入面试"] == "不推荐":
            # 尝试查找推荐状态
            if "推荐进入面试" in result_text or "推荐" in result_text:
                data["是否推荐进入面试"] = "推荐"
            elif "不推荐" in result_text:
                data["是否推荐进入面试"] = "不推荐"
        
        # 3. 优点和缺点提取（使用更灵活的关键词）
        if data["优点"] == "未识别":
            # 尝试多种关键词匹配优点
            pros_keywords = ["主要优点：", "优势：", "优点：", "优势\d+：", "优点\d+："]
            for keyword in pros_keywords:
                if keyword in result_text:
                    start_idx = result_text.index(keyword) + len(keyword)
                    end_idx = result_text.find("主要短板：", start_idx)
                    if end_idx == -1:
                        end_idx = result_text.find("短板：", start_idx)
                    if end_idx == -1:
                        end_idx = len(result_text)
                    data["优点"] = result_text[start_idx:end_idx].strip()
                    break
        
        if data["缺点"] == "未识别":
            # 尝试多种关键词匹配缺点
            cons_keywords = ["主要短板：", "短板：", "缺点：", "短板\d+：", "缺点\d+："]
            for keyword in cons_keywords:
                if keyword in result_text:
                    start_idx = result_text.index(keyword) + len(keyword)
                    end_idx = result_text.find("\n\n", start_idx)
                    if end_idx == -1:
                        end_idx = result_text.find("优势：", start_idx)
                    if end_idx == -1:
                        end_idx = result_text.find("优点：", start_idx)
                    if end_idx == -1:
                        end_idx = len(result_text)
                    data["缺点"] = result_text[start_idx:end_idx].strip()
                    break
        
        return data
    except Exception as e:
        print(f"结果解析失败: {str(e)}")
        return data

if __name__ == "__main__":
    # 职位描述
    job_description = """
    职位：辅助驾驶规控软件开发工程师 
    
    岗位职责：
    1. 负责客户需求的分析
    2. 负责商用车ADAS运动控制软件开发
    3. 支持产品开发及质量流程相关工作
    4. 支持车辆匹配调试
    5. 与项目团队协作
    
    任职要求：
    1. 985硕士以上学历
    2. 熟练掌握C++, C编程语言；MATLAB建模
    3. 嵌入式系统开发经验尤佳
    4. 优秀的沟通能力和团队合作精神
    5. 英语听说读写流利
    6. 工作地无锡，全职在岗超过4个月
    """
    
    # 准备Excel数据
    excel_data = []
    pdf_folder = "./data/resumes/"  # 简历文件夹路径
    
    # 遍历文件夹中的所有PDF文件
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"\n处理简历: {filename}")
            
            # 提取文本
            resume_text = extract_text_from_pdf(pdf_path)
            if not resume_text:
                print(f"跳过空文件: {filename}")
                continue
            print(f"简历文本提取完成，共{len(resume_text)}字符")
            
            # 评估简历
            print("开始评估简历匹配度...")
            eval_result = evaluate_resume(job_description, resume_text)
            print("原始模型输出:")
            print("-"*50)
            print(eval_result)  # 打印完整输出
            print("-"*50)
            
            # 解析结果
            parsed_data = parse_evaluation_result(eval_result)
            print("解析结果:")
            print(f"姓名: {parsed_data['姓名']}")
            print(f"最高学历院校: {parsed_data['最高学历院校']}")
            print(f"是否推荐进入面试: {parsed_data['是否推荐进入面试']}")
            print(f"优点: {parsed_data['优点'][:100] + '...' if len(parsed_data['优点']) > 100 else parsed_data['优点']}")
            print(f"缺点: {parsed_data['缺点'][:100] + '...' if len(parsed_data['缺点']) > 100 else parsed_data['缺点']}")
            
            # 添加到Excel数据
            excel_data.append({
                "姓名": parsed_data["姓名"],
                "最高学历院校": parsed_data["最高学历院校"],
                "是否推荐进入面试": parsed_data["是否推荐进入面试"],
                "优点": parsed_data["优点"],
                "缺点": parsed_data["缺点"]
            })
    
    # 保存到Excel
    if excel_data:
        # 创建DataFrame
        df = pd.DataFrame(excel_data)
        
        # 生成带时间戳的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_path = f"简历评估报告_{timestamp}.xlsx"
        
        # 保存Excel文件
        df.to_excel(excel_path, index=False, engine='openpyxl')
        print(f"\n成功处理{len(excel_data)}份简历，结果已保存至: {excel_path}")
        
        # 显示Excel内容预览
        print("\nExcel内容预览:")
        print(df)
    else:
        print("未找到可处理的PDF简历")
