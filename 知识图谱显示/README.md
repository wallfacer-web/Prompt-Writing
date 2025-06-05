# GraphRAG 提示词写作图书可视化与深度查询系统

## 🎯 项目概述

本项目是一个专门为分析提示词写作图书而设计的GraphRAG可视化和智能查询系统。它能够：

1. 📊 **可视化知识图谱** - 将GraphRAG索引的图书数据转换为直观的可视化图表
2. 🤔 **生成深度查询问题** - 自动生成10个英文问题，深度挖掘提示词的框架、写作方法和示例
3. 🔍 **智能查询路由** - 为每个问题选择最合适的查询方法（local/global/drift）

## 🛠️ 功能特点

### 可视化功能
- **知识图谱网络图** - 展示实体间的关系结构
- **节点度数分布** - 分析图谱的连接模式
- **中心性分析** - 识别关键节点和概念
- **社区检测** - 发现相关概念的聚类
- **实体类型分布** - 统计不同类型实体的数量
- **关键词频率分析** - 提取高频概念和术语

### 查询问题生成
- **框架类问题** (Global) - 整体方法论和系统性框架
- **示例类问题** (Local) - 具体模板和实际案例
- **比较类问题** (Global) - 不同技术的对比分析
- **趋势类问题** (Drift) - 发展历程和新兴趋势
- **技术类问题** (Local) - 具体实现细节
- **评估类问题** (Local) - 质量度量和评价方法

## 📋 环境要求

- Python 3.8+
- GraphRAG 0.50
- Conda环境

## 🚀 安装与使用

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行程序
```bash
python graphrag_visualization_and_query.py
```

### 3. 查看结果
程序会生成以下文件：
- `knowledge_graph_visualization.png` - 知识图谱可视化
- `entity_analysis.png` - 实体分析图表  
- `prompt_writing_deep_questions_*.md` - 深度查询问题集

## 📝 生成的问题类型

### 🌐 Global 查询问题 (4个)
适用于整体概述、比较分析和宏观视角：
- 基础框架和方法论
- 技术比较分析
- 领域特定策略
- 行业应用差异

### 🎯 Local 查询问题 (4个)  
适用于具体细节、特定示例和局部信息：
- 具体构建过程
- 成功模板示例
- 常见错误避免
- 技术实现细节
- 质量评估方法

### 🔄 Drift 查询问题 (2个)
适用于探索关联性、发现新模式和趋势：
- 发展趋势和演化
- 心理学和认知原理

## 🎨 可视化输出说明

### 知识图谱可视化
- **整体网络图**: 显示所有实体和关系的网络结构
- **度数分布**: 节点连接数的统计分布
- **中心性分析**: 最重要的10个概念节点
- **社区结构**: 相关概念的自然聚类

### 实体分析图表
- **实体类型分布**: 不同类型实体的数量统计
- **描述长度分布**: 实体描述的长度分析
- **高频关键词**: 最常出现的15个关键术语
- **统计摘要**: 整体数据概览

## 🔍 使用建议

1. **查看可视化图表** - 首先理解图书的整体知识结构
2. **按顺序执行查询** - 从框架类问题开始，逐步深入细节
3. **根据结果调整** - 基于查询结果优化后续问题
4. **交叉验证** - 使用不同查询方法验证重要信息

## 📊 项目结构

```
.
├── graphrag_visualization_and_query.py  # 主程序
├── requirements.txt                     # 依赖包列表
├── README.md                           # 项目说明
├── knowledge_graph_visualization.png   # 知识图谱可视化（生成）
├── entity_analysis.png                # 实体分析图表（生成）
└── prompt_writing_deep_questions_*.md  # 问题集（生成）
```

## 🎯 核心查询问题预览

1. **[GLOBAL] Framework**: What are the fundamental frameworks and methodologies for effective prompt engineering?

2. **[GLOBAL] Comparison**: How do different prompt writing techniques compare in terms of effectiveness and use cases?

3. **[LOCAL] Process**: What are the specific step-by-step processes for constructing high-quality prompts?

4. **[LOCAL] Examples**: Can you provide concrete examples of successful prompt templates for different AI tasks?

5. **[LOCAL] Best Practices**: What are the common pitfalls and mistakes to avoid when writing prompts?

6. **[DRIFT] Evolution**: How has prompt engineering evolved and what are the emerging trends in this field?

7. **[LOCAL] Technical**: What role does context length and structure play in prompt effectiveness?

8. **[GLOBAL] Domain-Specific**: How do domain-specific prompting strategies differ across various industries and applications?

9. **[DRIFT] Psychology**: What are the psychological and cognitive principles behind effective prompt design?

10. **[LOCAL] Evaluation**: How can prompt writers measure and evaluate the quality and performance of their prompts?

## 💡 注意事项

- 确保GraphRAG环境已正确配置
- 检查artifacts目录路径是否正确
- 程序会自动处理中文字体设置
- 可视化图片保存为高分辨率PNG格式
- 问题集保存为Markdown格式便于阅读和使用

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！ 