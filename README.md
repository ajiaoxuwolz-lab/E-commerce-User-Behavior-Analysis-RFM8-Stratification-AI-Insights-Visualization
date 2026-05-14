# 电商用户行为数据分析项目 | E-Commerce User Behavior Data Analysis Project
> 基于淘宝用户行为数据集全流程分析 | Full-process analysis based on Taobao user behavior dataset
> 适配实习简历 · GitHub 开源项目专用 | Perfect for internship resume & GitHub portfolio

---

## 项目简介 | Project Introduction
### 中文
本人为信息管理与信息系统大一学生，独立完成**数据清洗、指标统计、RFM八象限用户分层、商品品类挖掘、专业可视化、AI智能业务洞察**完整数据分析闭环。
采用Python模块化工程开发规范，复刻企业真实数据分析流程，项目可直接用于数据分析、电商数据运营相关暑期实习简历。

### English
As a freshman majoring in Information Management and Information System, I independently completed the full data analysis loop, including **data cleaning, indicator statistics, RFM 8-dimension user segmentation, category mining, professional visualization, and AI intelligent business insight**.
Following Python modular programming standards, this project reproduces the real enterprise data analysis workflow, which can be directly used for internship resumes of data analysis and e-commerce data operation.

---

## 技术栈 | Tech Stack
### 中文
- 数据处理：Python、Pandas、NumPy
- 可视化：Matplotlib、Seaborn
- 业务模型：RFM 八象限用户价值分层模型
- 工程规范：Git、模块化编程、路径统一配置、.gitignore 版本忽略

### English
- Data Processing: Python, Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Business Model: RFM 8-dimension User Value Segmentation Model
- Engineering Standard: Git, Modular Programming, Unified Path Configuration, .gitignore

---

## 项目结构 | Project Structure
Project_myfirst/
├── raw_data/ # 原始数据集 Raw dataset
├── processed_data/ # 清洗后数据 Processed dataset
├── outputs/ # 分析结果 CSV Analysis CSV outputs
├── report/ # 可视化图表 Visual charts
├── docs/ # 业务分析文档 Business reports
├── notebooks/ # 分步分析脚本 Step-by-step notebooks
├── .gitignore # Git 忽略配置 Git ignore file
├── README.md # 项目说明 Project readme
└── requirements.txt # 依赖库列表 Dependencies

---

## 核心工作与成果 | Core Work & Achievements
### 1. 数据预处理与清洗 | Data Preprocessing & Cleaning
**中文**
处理百万级用户行为数据，过滤脏数据、标准化时间字段、构造用户行为标签，搭建多维度分析数据集。
**English**
Processed million-level user behavior data, filtered invalid data, standardized time fields, built behavior labels and multi-dimensional analysis datasets.

### 2. RFM 用户分层建模 | RFM User Segmentation Modeling
**中文**
采用互联网行业标准 RFM 八象限模型，将用户划分为8类价值层级，精准定位高价值、潜力、流失用户群体。
**English**
Adopted industry-standard RFM 8-dimension model to divide users into 8 value groups, accurately identifying high-value, potential and churn users.

### 3. 商品与转化分析 | Product & Conversion Analysis
**中文**
挖掘热销品类TOP10，识别高浏览低转化问题商品，给出商品定价、详情页、流量匹配优化方向。
**English**
Mined top10 hot categories, identified high-click low-conversion products, and provided optimization suggestions on pricing, product page and traffic matching.

### 4. 多维度专业可视化 | Multi-dimensional Professional Visualization
**中文**
制作用户分层饼图、购买贡献柱状图、RFM热力图，统一专业配色并添加数据标签，输出高清商用级图表。
**English**
Produced user segmentation pie chart, contribution bar chart and RFM heatmap with professional color scheme and data labels, exporting high-definition commercial-level charts.

### 5. AI 智能业务洞察 | AI Intelligent Business Insight
**中文**
自研规则式AI分析模块，自动根据数据生成运营结论、用户策略、商品优化及时段投放建议。
**English**
Built a rule-based AI insight module to automatically generate business conclusions, user operation strategies, product optimization and time scheduling suggestions.

---

## 项目亮点 | Project Highlights
### 中文
✅ 完整复刻企业数据分析全流程，具备系统化业务分析思维  
✅ 落地行业标准 RFM 八象限模型，区别于普通基础分层  
✅ 代码模块化工程化，符合 GitHub 开源项目规范  
✅ 结合 AI 自动洞察，紧跟人工智能+数据融合趋势  
✅ 不只做图表，输出可落地运营策略与 A/B 测试方案  

### English
✅ Reproduced the full enterprise data analysis workflow with systematic business thinking  
✅ Implemented industry-standard RFM 8-dimension model instead of basic segmentation  
✅ Modular & standardized code structure following GitHub open-source specification  
✅ Integrated AI automatic insight, keeping up with AI & data fusion trend  
✅ Delivered actionable operation strategies and A/B testing solutions beyond simple charts  

---

## 运行方式 | How to Run
```bash
# 克隆仓库 Clone repository
git clone https://github.com/ajiaoxuwolz-lab/E-commerce-User-Behavior-Analysis-RFM8-Stratification-AI-Insights-Visualization.git

# 安装依赖 Install dependencies
pip install -r requirements.txt

# 放入清洗后数据至 processed_data 目录，直接运行主脚本即可
# Put processed CSV into processed_data folder and run the main script
