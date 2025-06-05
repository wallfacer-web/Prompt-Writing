@echo off
chcp 65001 >nul
echo 🚀 GraphRAG提示词写作图书分析系统
echo ================================

echo.
echo 📋 检查Python环境...
python --version
if errorlevel 1 (
    echo ❌ Python未安装或未添加到PATH
    pause
    exit /b 1
)

echo.
echo 📦 安装依赖包...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ 依赖包安装失败
    pause
    exit /b 1
)

echo.
echo 🎯 运行分析程序...
python graphrag_visualization_and_query.py

echo.
echo ✅ 程序执行完成！
echo 📁 请查看生成的图片和Markdown文件
pause 