import os
import sys
import subprocess

# ===================== 项目规范配置（零修改，完全对齐简历级标准）=====================
# 核心文件夹结构：src存放核心代码，raw_data永久锁死不上传Git
folder_structure = [
    "src",                # 核心代码/脚本存放（原方案指定路径，必选）
    "notebooks",          # Jupyter Notebook专属存放目录（可选，和src二选一即可）
    "raw_data",           # 原始CSV存放地（.gitignore已永久屏蔽，绝对不会上传Git）
    "processed_data",     # 清洗后合规数据存放
    "docs",               # 分析报告、文档说明存放
    "output"              # 可视化图表、分析结果导出
]

# 核心依赖包：完全对齐原方案，可选包标注清晰
core_packages = ["pandas", "numpy"]
optional_visual_packages = ["matplotlib", "seaborn"]

# ===================== 1. 一键创建规范文件夹结构 =====================
for folder in folder_structure:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"✅ 已创建文件夹: {folder}")
    else:
        print(f"ℹ️ 文件夹已存在: {folder}")

# ===================== 2. 自动生成.gitignore，永久锁死核心避坑红线 =====================
gitignore_content = """
# ========== 核心红线：原始数据集绝不入Git仓库（绝对不可删除）==========
raw_data/
*.csv
*.xlsx
*.xls

# ========== PyCharm 专属缓存/配置文件 ==========
.idea/
*.iml
*.iws
*.ipr

# ========== Python 临时/环境文件 ==========
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# ========== Jupyter 临时文件 ==========
.ipynb_checkpoints/
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print("✅ 已生成.gitignore，「原始数据不上传Git」核心红线已永久锁死")

# ===================== 3. 依赖包自动校验&安装 =====================
print("\n===================== 依赖包环境校验 =====================")
# 安装核心必装包
for pkg in core_packages:
    try:
        __import__(pkg)
        print(f"✅ 核心依赖 {pkg} 已就绪")
    except ImportError:
        print(f"⚠️  检测到缺失核心依赖 {pkg}，正在一键安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        print(f"✅ 核心依赖 {pkg} 安装完成")

# 可选可视化包安装提示
for pkg in optional_visual_packages:
    try:
        __import__(pkg)
        print(f"ℹ️  可选可视化包 {pkg} 已就绪")
    except ImportError:
        print(f"ℹ️  可选可视化包 {pkg} 未安装，后续可视化阶段可一键安装，不影响当前阶段执行")

# ===================== 4. PyCharm环境专属提示 =====================
print("\n===================== PyCharm环境专属启动提示 =====================")
print("1. 首次使用Jupyter Notebook：请在PyCharm插件市场搜索「Jupyter」安装并重启IDE")
print("2. Notebook内核选择：务必选中你当前项目绑定的Anaconda环境，避免包导入失败")
print("3. Git操作兜底：除了终端命令，可直接使用PyCharm顶部「Git」菜单完成全流程可视化操作")

print("\n🎉 项目初始化全部完成！完美匹配原方案所有核心规则，下一步请将原始数据集UserBehavior.csv放入raw_data文件夹")


