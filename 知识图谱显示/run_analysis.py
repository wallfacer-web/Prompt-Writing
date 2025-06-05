#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速启动脚本 - GraphRAG提示词写作图书分析
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """检查依赖包是否已安装"""
    required_packages = ['networkx', 'matplotlib', 'seaborn', 'pandas', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ 缺少以下依赖包: {', '.join(missing_packages)}")
        print("请运行: pip install -r requirements.txt")
        return False
    
    print("✅ 所有依赖包已安装")
    return True

def check_artifacts_path():
    """检查artifacts目录是否存在"""
    artifacts_path = Path("C:/Users/13694/ragtest/output/20250602-151653/artifacts")
    
    if not artifacts_path.exists():
        print(f"❌ 找不到artifacts目录: {artifacts_path}")
        print("请检查GraphRAG输出路径是否正确")
        return False
    
    print(f"✅ 找到artifacts目录: {artifacts_path}")
    return True

def main():
    """主函数"""
    print("🚀 GraphRAG提示词写作图书分析 - 快速启动")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        return
    
    # 检查数据路径
    if not check_artifacts_path():
        return
    
    # 运行主程序
    print("\n🎯 开始运行分析程序...")
    try:
        from graphrag_visualization_and_query import main as run_main
        run_main()
    except Exception as e:
        print(f"❌ 运行出错: {e}")
        print("请检查graphrag_visualization_and_query.py文件是否存在")

if __name__ == "__main__":
    main() 