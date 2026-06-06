"""
JSON Tools - AI JSON工具集
支持JSON转换、验证、Schema生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class JSONTools:
    """
    AI JSON工具集
    支持：转换、验证、Schema生成、查询
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_schema(self, json_data: str) -> Dict:
        """从JSON生成Schema"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请从以下JSON数据生成JSON Schema：

{json_data}

请返回完整的JSON Schema："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"schema": content}

    def convert_format(self, data: str, source_format: str, target_format: str) -> str:
        """格式转换"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下{source_format}格式数据转换为{target_format}格式：

{data}

只返回转换后的数据："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def validate_json(self, json_data: str, schema: str = "") -> Dict:
        """验证JSON"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请验证以下JSON数据：

{json_data}

{f'Schema：{schema}' if schema else ''}

请返回JSON格式：
{{
    "valid": true/false,
    "errors": ["错误1", "错误2"],
    "warnings": ["警告1", "警告2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"validation": content}

    def query_json(self, json_data: str, query: str) -> str:
        """查询JSON"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下查询从JSON数据中提取信息：

数据：{json_data}
查询：{query}

只返回查询结果："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def transform_json(self, json_data: str, transformation: str) -> str:
        """转换JSON"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请按以下要求转换JSON数据：

数据：{json_data}
转换要求：{transformation}

只返回转换后的JSON："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def merge_json(self, json_list: List[str]) -> str:
        """合并JSON"""
        if not self.client:
            return "LLM客户端未配置"

        json_text = "\n\n".join(f"JSON {i+1}:\n{j}" for i, j in enumerate(json_list))

        prompt = f"""请合并以下JSON数据：

{json_text}

要求：
1. 合并相同字段
2. 保留所有数据
3. 处理冲突

只返回合并后的JSON："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_sample(self, schema: str, count: int = 5) -> str:
        """生成示例数据"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下Schema生成{count}条示例数据：

Schema：
{schema}

只返回JSON数组："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> JSONTools:
    """创建JSON工具"""
    return JSONTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("JSON Tools")
    print()

    # 测试
    sample = '{"name": "张三", "age": 25, "skills": ["Python", "JavaScript"]}'
    schema = tools.generate_schema(sample)
    print("Schema:")
    print(json.dumps(schema, ensure_ascii=False, indent=2))
