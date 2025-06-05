#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GraphRAG 图书可视化和智能查询系统
用于可视化提示词写作图书的知识图谱并生成深度挖掘问题
"""

import os
import json
import subprocess
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
import random
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

class GraphRAGVisualizer:
    def __init__(self, artifacts_path):
        """
        初始化GraphRAG可视化器
        
        Args:
            artifacts_path (str): GraphRAG输出的artifacts目录路径
        """
        self.artifacts_path = Path(artifacts_path)
        self.ragtest_path = Path("C:/Users/13694/ragtest")
        self.graph_data = {}
        self.entities = []
        self.relationships = []
        
    def load_graph_data(self):
        """加载GraphRAG生成的图数据"""
        try:
            # 加载GraphML文件
            graphml_file = self.artifacts_path / "summarized_graph.graphml"
            if graphml_file.exists():
                self.graph_data['graph'] = nx.read_graphml(str(graphml_file))
                print(f"✅ 成功加载图数据，包含 {len(self.graph_data['graph'].nodes)} 个节点和 {len(self.graph_data['graph'].edges)} 条边")
            
            # 加载实体数据
            entities_file = self.artifacts_path / "raw_extracted_entities.json"
            if entities_file.exists():
                with open(entities_file, 'r', encoding='utf-8') as f:
                    self.entities = json.load(f)
                print(f"✅ 成功加载 {len(self.entities)} 个实体")
            
            # 加载顶层节点
            top_nodes_file = self.artifacts_path / "top_level_nodes.json"
            if top_nodes_file.exists():
                with open(top_nodes_file, 'r', encoding='utf-8') as f:
                    self.graph_data['top_nodes'] = json.load(f)
                print(f"✅ 成功加载顶层节点数据")
                
            # 加载统计信息
            stats_file = self.artifacts_path / "stats.json"
            if stats_file.exists():
                with open(stats_file, 'r', encoding='utf-8') as f:
                    self.graph_data['stats'] = json.load(f)
                print(f"✅ 成功加载统计信息")
                
        except Exception as e:
            print(f"❌ 加载图数据时出错: {e}")
    
    def analyze_book_structure(self):
        """分析图书结构和主题"""
        print("\n📊 分析图书结构...")
        
        # 分析实体类型分布
        entity_types = Counter()
        entity_descriptions = []
        
        for entity in self.entities:
            if 'type' in entity:
                entity_types[entity['type']] += 1
            if 'description' in entity:
                entity_descriptions.append(entity['description'])
        
        print(f"📈 实体类型分布:")
        for entity_type, count in entity_types.most_common(10):
            print(f"  - {entity_type}: {count}")
        
        # 分析图结构
        if 'graph' in self.graph_data:
            G = self.graph_data['graph']
            print(f"\n🔗 图结构分析:")
            print(f"  - 节点数量: {G.number_of_nodes()}")
            print(f"  - 边数量: {G.number_of_edges()}")
            print(f"  - 密度: {nx.density(G):.4f}")
            print(f"  - 连通组件数: {nx.number_connected_components(G.to_undirected())}")
        
        return entity_types, entity_descriptions
    
    def visualize_knowledge_graph(self):
        """可视化知识图谱"""
        print("\n🎨 生成知识图谱可视化...")
        
        if 'graph' not in self.graph_data:
            print("❌ 无法加载图数据进行可视化")
            return
        
        G = self.graph_data['graph']
        
        # 创建子图显示
        fig, axes = plt.subplots(2, 2, figsize=(20, 16))
        fig.suptitle('提示词写作图书 - 知识图谱可视化', fontsize=16, fontweight='bold')
        
        # 1. 整体网络图
        ax1 = axes[0, 0]
        pos = nx.spring_layout(G, k=1, iterations=50)
        
        # 根据度数调整节点大小
        degrees = dict(G.degree())
        node_sizes = [degrees[node] * 20 + 50 for node in G.nodes()]
        
        nx.draw(G, pos, ax=ax1, node_size=node_sizes, node_color='lightblue', 
                edge_color='gray', alpha=0.7, with_labels=False)
        ax1.set_title('整体知识网络', fontsize=14)
        
        # 2. 度数分布
        ax2 = axes[0, 1]
        degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
        ax2.hist(degree_sequence, bins=20, alpha=0.7, color='skyblue')
        ax2.set_title('节点度数分布', fontsize=14)
        ax2.set_xlabel('度数')
        ax2.set_ylabel('频次')
        
        # 3. 中心性分析
        ax3 = axes[1, 0]
        centrality = nx.betweenness_centrality(G)
        central_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]
        
        nodes, values = zip(*central_nodes) if central_nodes else ([], [])
        ax3.barh(range(len(nodes)), values)
        ax3.set_yticks(range(len(nodes)))
        ax3.set_yticklabels([str(node)[:20] for node in nodes])
        ax3.set_title('中间中心性排名前10的节点', fontsize=14)
        ax3.set_xlabel('中间中心性值')
        
        # 4. 社区检测
        ax4 = axes[1, 1]
        try:
            communities = nx.community.greedy_modularity_communities(G.to_undirected())
            community_sizes = [len(c) for c in communities]
            ax4.pie(community_sizes, labels=[f'社区{i+1}' for i in range(len(communities))], 
                   autopct='%1.1f%%', startangle=90)
            ax4.set_title(f'社区结构 (共{len(communities)}个社区)', fontsize=14)
        except:
            ax4.text(0.5, 0.5, '无法进行社区检测', ha='center', va='center', transform=ax4.transAxes)
            ax4.set_title('社区结构', fontsize=14)
        
        plt.tight_layout()
        plt.savefig('knowledge_graph_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ 知识图谱可视化已保存为 knowledge_graph_visualization.png")
    
    def create_entity_analysis(self):
        """创建实体分析图表"""
        print("\n📈 生成实体分析图表...")
        
        if not self.entities:
            print("❌ 无法加载实体数据进行分析")
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('实体分析 - 提示词写作图书', fontsize=16, fontweight='bold')
        
        # 1. 实体类型分布
        ax1 = axes[0, 0]
        entity_types = Counter()
        for entity in self.entities:
            if 'type' in entity:
                entity_types[entity['type']] += 1
        
        if entity_types:
            top_types = dict(entity_types.most_common(10))
            ax1.bar(range(len(top_types)), list(top_types.values()), color='lightcoral')
            ax1.set_xticks(range(len(top_types)))
            ax1.set_xticklabels(list(top_types.keys()), rotation=45, ha='right')
            ax1.set_title('实体类型分布', fontsize=14)
            ax1.set_ylabel('数量')
        
        # 2. 实体描述长度分布
        ax2 = axes[0, 1]
        desc_lengths = []
        for entity in self.entities:
            if 'description' in entity and entity['description']:
                desc_lengths.append(len(entity['description']))
        
        if desc_lengths:
            ax2.hist(desc_lengths, bins=20, alpha=0.7, color='lightgreen')
            ax2.set_title('实体描述长度分布', fontsize=14)
            ax2.set_xlabel('描述长度（字符数）')
            ax2.set_ylabel('频次')
        
        # 3. 关键词云（模拟）
        ax3 = axes[1, 0]
        keywords = []
        for entity in self.entities:
            if 'name' in entity:
                keywords.extend(entity['name'].split())
        
        if keywords:
            keyword_counts = Counter(keywords)
            top_keywords = dict(keyword_counts.most_common(15))
            ax3.bar(range(len(top_keywords)), list(top_keywords.values()), color='lightskyblue')
            ax3.set_xticks(range(len(top_keywords)))
            ax3.set_xticklabels(list(top_keywords.keys()), rotation=45, ha='right')
            ax3.set_title('高频关键词', fontsize=14)
            ax3.set_ylabel('出现次数')
        
        # 4. 统计摘要
        ax4 = axes[1, 1]
        stats_text = f"""
        统计摘要:
        
        • 总实体数: {len(self.entities)}
        • 平均描述长度: {sum(desc_lengths)/len(desc_lengths):.1f} 字符
        • 实体类型数: {len(entity_types)}
        • 最常见类型: {entity_types.most_common(1)[0][0] if entity_types else 'N/A'}
        • 最高频词: {keyword_counts.most_common(1)[0][0] if keywords else 'N/A'}
        """
        ax4.text(0.1, 0.9, stats_text, transform=ax4.transAxes, fontsize=12, 
                verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')
        ax4.set_title('统计摘要', fontsize=14)
        
        plt.tight_layout()
        plt.savefig('entity_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ 实体分析图表已保存为 entity_analysis.png")

class PromptWritingQueryGenerator:
    """提示词写作深度查询生成器"""
    
    def __init__(self, ragtest_path):
        self.ragtest_path = Path(ragtest_path)
        self.questions = []
        
    def generate_deep_questions(self):
        """生成10个深度挖掘提示词写作的英文问题"""
        print("\n🤔 生成提示词写作深度挖掘问题...")
        
        # 定义问题类别和对应的查询方法
        questions_data = [
            {
                "question": "What are the fundamental frameworks and methodologies for effective prompt engineering?",
                "method": "global",
                "category": "Framework",
                "focus": "Overall structure and systematic approaches to prompt design"
            },
            {
                "question": "How do different prompt writing techniques compare in terms of effectiveness and use cases?",
                "method": "global", 
                "category": "Comparison",
                "focus": "Comparative analysis of various prompting methods"
            },
            {
                "question": "What are the specific step-by-step processes for constructing high-quality prompts?",
                "method": "local",
                "category": "Process",
                "focus": "Detailed procedural knowledge for prompt construction"
            },
            {
                "question": "Can you provide concrete examples of successful prompt templates for different AI tasks?",
                "method": "local",
                "category": "Examples",
                "focus": "Specific prompt examples and templates"
            },
            {
                "question": "What are the common pitfalls and mistakes to avoid when writing prompts?",
                "method": "local",
                "category": "Best Practices",
                "focus": "Error prevention and optimization techniques"
            },
            {
                "question": "How has prompt engineering evolved and what are the emerging trends in this field?",
                "method": "drift",
                "category": "Evolution",
                "focus": "Historical development and future directions"
            },
            {
                "question": "What role does context length and structure play in prompt effectiveness?",
                "method": "local",
                "category": "Technical",
                "focus": "Technical aspects of prompt design"
            },
            {
                "question": "How do domain-specific prompting strategies differ across various industries and applications?",
                "method": "global",
                "category": "Domain-Specific",
                "focus": "Industry-specific applications and adaptations"
            },
            {
                "question": "What are the psychological and cognitive principles behind effective prompt design?",
                "method": "drift",
                "category": "Psychology",
                "focus": "Human-AI interaction psychology"
            },
            {
                "question": "How can prompt writers measure and evaluate the quality and performance of their prompts?",
                "method": "local",
                "category": "Evaluation",
                "focus": "Metrics and assessment methods"
            }
        ]
        
        self.questions = questions_data
        return questions_data
    
    def execute_queries(self, max_queries=5):
        """执行GraphRAG查询（演示模式，仅显示前5个）"""
        print(f"\n🔍 执行GraphRAG查询（演示前{max_queries}个问题）...")
        
        results = []
        
        for i, q_data in enumerate(self.questions[:max_queries]):
            print(f"\n问题 {i+1}: {q_data['question']}")
            print(f"查询方法: {q_data['method']}")
            print(f"类别: {q_data['category']}")
            
            # 构建查询命令
            cmd = f'conda activate graphrag-0.50 && graphrag query --root {self.ragtest_path} --method {q_data["method"]} --query "{q_data["question"]}"'
            
            print(f"执行命令: {cmd}")
            print("=" * 80)
            
            # 实际项目中可以执行查询
            # 这里为了演示，我们跳过实际执行
            results.append({
                "question": q_data["question"],
                "method": q_data["method"],
                "category": q_data["category"],
                "command": cmd,
                "status": "准备执行"
            })
        
        return results
    
    def save_questions_to_file(self):
        """保存问题到文件"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"prompt_writing_deep_questions_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# 提示词写作深度挖掘问题集\n\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## 问题列表\n\n")
            
            for i, q_data in enumerate(self.questions, 1):
                f.write(f"### 问题 {i}\n\n")
                f.write(f"**问题**: {q_data['question']}\n\n")
                f.write(f"**查询方法**: `{q_data['method']}`\n\n")
                f.write(f"**类别**: {q_data['category']}\n\n")
                f.write(f"**关注点**: {q_data['focus']}\n\n")
                f.write(f"**执行命令**:\n```bash\n")
                f.write(f"conda activate graphrag-0.50\n")
                f.write(f"graphrag query --root ./ragtest --method {q_data['method']} --query \"{q_data['question']}\"\n")
                f.write("```\n\n")
                f.write("---\n\n")
            
            # 添加查询方法说明
            f.write("## 查询方法说明\n\n")
            f.write("- **local**: 适用于需要具体细节、特定示例或局部信息的问题\n")
            f.write("- **global**: 适用于需要整体概述、比较分析或宏观视角的问题\n")
            f.write("- **drift**: 适用于需要探索关联性、发现新模式或趋势的问题\n\n")
            
        print(f"✅ 问题集已保存到 {filename}")
        return filename

def main():
    """主函数"""
    print("🚀 GraphRAG 提示词写作图书可视化与深度查询系统")
    print("=" * 60)
    
    # 设置路径
    artifacts_path = "C:/Users/13694/ragtest/output/20250602-151653/artifacts"
    ragtest_path = "C:/Users/13694/ragtest"
    
    # 初始化可视化器
    visualizer = GraphRAGVisualizer(artifacts_path)
    
    # 1. 加载和分析数据
    print("\n📊 第一步：加载和分析图书数据")
    visualizer.load_graph_data()
    entity_types, descriptions = visualizer.analyze_book_structure()
    
    # 2. 生成可视化
    print("\n🎨 第二步：生成可视化图表")
    visualizer.visualize_knowledge_graph()
    visualizer.create_entity_analysis()
    
    # 3. 生成深度查询问题
    print("\n🤔 第三步：生成提示词写作深度查询问题")
    query_generator = PromptWritingQueryGenerator(ragtest_path)
    questions = query_generator.generate_deep_questions()
    
    # 4. 显示问题概览
    print("\n📋 生成的10个深度挖掘问题:")
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. [{q['method'].upper()}] {q['category']}")
        print(f"   {q['question']}")
    
    # 5. 保存问题到文件
    query_generator.save_questions_to_file()
    
    # 6. 演示查询执行
    print("\n🔍 第四步：演示查询执行")
    query_generator.execute_queries(max_queries=3)
    
    print("\n✅ 程序执行完成！")
    print("📁 生成的文件:")
    print("  - knowledge_graph_visualization.png: 知识图谱可视化")
    print("  - entity_analysis.png: 实体分析图表")
    print("  - prompt_writing_deep_questions_*.md: 深度查询问题集")
    
    print("\n💡 使用建议:")
    print("  1. 查看生成的可视化图表了解图书结构")
    print("  2. 使用问题集中的命令执行GraphRAG查询")
    print("  3. 根据查询结果调整和优化问题")

if __name__ == "__main__":
    main() 