# 智能文档分析与提示词写作平台

一个基于Gradio的综合性AI工具平台，集成了文档分析、提示词写作、知识图谱、RAG系统等多种功能。

## 🌟 主要功能

### 1. 文档智能分析
- 支持PDF、DOCX、TXT格式文档
- 多种思维模式分析：标准模式、创新模式、批判性思维等
- 多任务并行处理
- 自动生成分析报告

### 2. 提示词写作增强
- 多种提示词增强方法
- 实时预览和编辑
- 专业写作指导
- 模板库支持

### 3. RAG知识库系统
- 文档向量化存储
- 智能问答系统
- 上下文理解
- 知识检索优化

### 4. 知识图谱可视化
- 自动构建知识图谱
- 交互式图谱展示
- 关系分析
- 实体提取

### 5. Ollama集成聊天
- 本地大模型支持
- 多模型切换
- 流式对话
- 历史记录管理

### 6. 深度研究系统
- 集成搜索引擎
- 自动文献收集
- 研究报告生成
- 多源信息整合

### 7. GraphRAG查询
- 图数据库查询
- 复杂关系分析
- 智能问答
- 结果优化

## 🚀 快速开始

### 环境要求
- Python 3.8+
- pip

### 安装步骤

1. 克隆项目
```bash
git clone https://github.com/wallfacer-web/document-analyzer.git
cd document-analyzer
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动应用
```bash
python document_analyzer.py
```

4. 打开浏览器访问 `http://localhost:7860`

## 📁 项目结构

```
├── document_analyzer.py          # 主程序文件
├── 提示词写作-final.py            # 提示词写作模块
├── 知识图谱显示/                   # 知识图谱相关文件
│   ├── graphrag_visualization_and_query.py
│   ├── run_analysis.py
│   └── README.md
├── requirements.txt              # 依赖包列表
├── .gitignore                   # Git忽略文件
└── README.md                    # 项目说明
```

## 🔧 配置说明

### Ollama配置
确保Ollama服务在本地运行（默认端口11434）：
```bash
ollama serve
```

### Docker服务（可选）
如果使用深度研究功能，需要启动相关Docker服务：
```bash
docker start searxng
docker start local-deep-research
```

### GraphRAG配置（可选）
如果使用GraphRAG功能，需要配置GraphRAG环境：
```bash
conda activate graphrag-0.50
```

## 💡 使用说明

### 文档分析
1. 上传文档（支持PDF、DOCX、TXT格式）
2. 选择分析任务和思维模式
3. 等待分析完成
4. 下载分析报告

### 提示词写作
1. 输入原始提示词
2. 选择增强方法
3. 获取优化后的提示词
4. 保存或进一步编辑

### 知识库问答
1. 上传文档建立知识库
2. 输入问题
3. 获取基于文档的智能回答

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

## 📄 许可证

本项目采用MIT许可证 - 查看[LICENSE](LICENSE)文件了解详情

## 🙏 致谢

- [Gradio](https://gradio.app/) - 快速构建机器学习界面
- [Ollama](https://ollama.ai/) - 本地大模型运行
- [GraphRAG](https://github.com/microsoft/graphrag) - 图检索增强生成

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- GitHub Issues: [项目Issues页面](https://github.com/wallfacer-web/document-analyzer/issues)
- Email: [您的邮箱]

---

⭐ 如果这个项目对您有帮助，请给个star支持一下！ 