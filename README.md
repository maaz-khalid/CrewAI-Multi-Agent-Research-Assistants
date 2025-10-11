# 🤖 CrewAI News Research & Writing Agent

> An AI-powered crew that researches and writes insightful articles about emerging technologies! 📚✨

## 🎯 Overview

This project uses **CrewAI** to create a collaborative AI crew consisting of a senior researcher and a technical writer. The crew works together to research any given technology topic and produce well-structured, informative articles.

## 🔧 Tech Stack

- **🚀 CrewAI** - Multi-agent AI framework
- **🧠 Google Gemini 1.5 Flash** - Language model for AI agents
- **🔍 SerperDev** - Web search tool for research
- **🐍 Python** - Core programming language
- **🔗 LangChain** - LLM integration

## 🤝 Meet the Crew

### 👨‍🔬 Senior Researcher Agent
- **Role**: Uncover groundbreaking technologies
- **Mission**: Research when, how, and why technologies were introduced
- **Tools**: Web search capabilities via SerperDev

### ✍️ News Writer Agent  
- **Role**: Transform research into engaging content
- **Mission**: Create easy-to-understand, insightful articles
- **Output**: Structured markdown articles with bullet points

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file with:
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

3. **Run the crew:**
   ```bash
   python crew.py
   ```

## 📋 How It Works

1. **Research Phase** 📖 - The researcher agent investigates the given topic
2. **Writing Phase** ✏️ - The writer agent creates a comprehensive article
3. **Sequential Process** 🔄 - Tasks are executed one after another for quality output

## 🎯 Current Example

The crew is currently configured to research **RAG (Retrieval Augmented Generation) architecture** and produce a detailed article about it.

## 📁 Project Structure

```
crewai/
├── agents.py      # AI agent definitions
├── tasks.py       # Task configurations  
├── tools.py       # Web search tools
├── crew.py        # Main execution script
├── requirements.txt
└── .env          # API keys
```


*Built with ❤️ using CrewAI framework*
