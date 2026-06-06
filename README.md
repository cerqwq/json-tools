# 🔧 JSON Tools

AI JSON工具集，支持JSON转换、验证、Schema生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📐 Schema生成
- 🔄 格式转换
- ✅ JSON验证
- 🔍 JSON查询
- 🔧 JSON转换
- 🔗 JSON合并
- 🌱 示例数据生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from json_tools import create_tools

tools = create_tools()

# 生成Schema
schema = tools.generate_schema('{"name": "张三", "age": 25}')

# 格式转换
csv = tools.convert_format(json_data, "JSON", "CSV")

# 验证JSON
result = tools.validate_json(json_data, schema)

# 查询JSON
value = tools.query_json(json_data, "获取所有用户的邮箱")

# 转换JSON
transformed = tools.transform_json(json_data, "将所有字段名转为驼峰命名")

# 合并JSON
merged = tools.merge_json([json1, json2, json3])

# 生成示例
samples = tools.generate_sample(schema, 10)
```

## 📁 项目结构

```
json-tools/
├── tools.py       # JSON工具核心
└── README.md
```

## 📄 许可证

MIT License
