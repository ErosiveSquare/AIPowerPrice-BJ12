# 导入必要库
import streamlit as st
from PIL import Image  # 用于处理图片
import os  # 新增：用于处理文件路径

# 此为首页，执行：streamlit run Home.py

# 页面配置（保持不变）
st.set_page_config(
    page_title="智能市场电价预测分析 | 首页",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接图片文件的完整路径（相对路径的本质实现）
logo_path = os.path.join(current_dir, "NCEPU.png")
# 打开图片
logo = Image.open(logo_path)

# 用columns创建一行两列布局，左侧放校徽，右侧放标题
col1, col2 = st.columns([1, 7])  # 比例可根据校徽大小调整
with col1:
    st.image(logo, width=80)  # width根据校徽实际尺寸调整
with col2:
    st.title("欢迎使用市场电价智能分析平台 ⚡")

st.markdown("---")

st.markdown("""
### 市场电价智能分析平台

本应用整合了自研深度学习电价预测工具与完善的数据库管理界面，作为题目的第一部分实现。

- 在侧边栏中导航至「预测工具」，使用我们先进的Transformer与GRU模型预测未来电价。

- 导航至「数据库管理」，查看、添加、编辑或删除为预测提供支持的历史市场数据记录。

**从侧边栏选择一个页面开始使用。**
""")

st.info("挑战杯“揭榜挂帅”", icon="⚡")