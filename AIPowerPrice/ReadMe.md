

# AI Power Price Project

## 项目简介
本项目围绕电力价格相关任务展开，涵盖预测工具、数据库管理等功能，致力于为电力市场数据分析与价格预测等场景提供支持 。

## 项目结构
```
AI Power Price/
├── pages/
│   ├── saved_model/
│   ├── 1__Prediction_Tool.py  # 预测工具脚本
│   ├── 2__Database_Manager.py  # 数据库管理脚本
│   ├── __init__.py
│   ├── market_data.db  # 数据库文件
├── __init__.py
├── database_setup.py  # 数据库初始化设置脚本
├── Home.py  # 项目主页面，streamlit 启动入口
├── mock_market_data_for_prediction.csv  # 预测用模拟市场数据
├── NCEPU.png  # 相关图片资源
├── sample_input.csv  # 示例输入数据
├── train_final.py  # 模型训练相关脚本 
```

## 功能说明
- **预测功能**：`1__Prediction_Tool.py` 可基于数据进行电力价格等预测任务，结合模型与输入数据输出预测结果。 
- **数据库管理**：`2__Database_Manager.py` 负责数据库的增删改查等操作，`database_setup.py` 用于初始化数据库配置，`market_data.db` 存储相关市场数据。 
- **模型训练**：`train_final.py` 承担模型训练工作，为预测功能提供模型支撑 。 
- **数据文件**：`mock_market_data_for_prediction.csv` 、`sample_input.csv` 分别为预测、输入示例数据，辅助功能调试与使用。 

## 启动步骤

### 环境依赖
确保已安装以下Python库：
- streamlit：构建Web应用界面
- torch、torch.nn：实现深度学习模型
- numpy、pandas：数据处理与分析
- scikit-learn：数据预处理（MinMaxScaler）
- scipy：提供插值功能（CubicSpline）
- plotly：数据可视化
- sqlite3：数据库操作（通常Python内置）

可通过以下命令安装主要依赖：
```bash
pip install streamlit torch numpy pandas scikit-learn scipy plotly
```
### 启动命令
在整个挑战杯项目中，即根目录为（BJ12）时，打开终端执行：

```bash
streamlit run AIPowerPrice/Home.py
```

在本项目（AIPowerPrice）根目录下,即只有一个电价预测软件时，打开终端执行：

```bash
streamlit run Home.py
```

执行后终端会输出本地访问链接（一般为 `http://localhost:8501` ），在浏览器打开该链接即可使用项目功能 。 

## 注意事项
- 首次运行若涉及数据库操作，需确保 `database_setup.py` 正确配置，避免数据库初始化失败。 
- 模型训练与预测需保证数据格式符合脚本要求，可参考 `mock_market_data_for_prediction.csv` 、`sample_input.csv` 调整输入数据 。 
- 若遇到库依赖问题，可根据报错信息使用 `pip install` 命令安装对应缺失库 。 
