import json
import os
import re
import shutil
import pandas as pd


def csv_to_md(csv_file):
    # 读取CSV文件
    data = pd.read_csv(csv_file)

    # 将数据转换为MD格式
    md_data = data.to_markdown()

    return md_data


file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.dirname(file_dir)))


def format_md_templates(md_file: str, output_file: str):
    with open(md_file, "r", encoding="utf8") as f:
        content = f.read()

    for label in filter(lambda line: line.startswith("MACRO"), content.splitlines()):
        macro = label.strip("MACRO").strip()
        print(macro)
        payload = json.loads(macro)
        if payload.get("kind") == "file":

            with open(payload["path"], encoding="utf-8") as f:
                file_content = f.read()
                if (lang := payload.get("language")) is not None:
                    if payload.get("with_path"):
                        file_content = (
                            (f"`{payload['path']}`\n")
                            + f"\n```{lang}\n"
                            + file_content
                            + "\n```"
                        )
                    else:
                        file_content = f"\n```{lang}\n" + file_content + "\n```"
                content = content.replace(label, file_content, 1)
        elif payload.get("kind") == "table":
            content = content.replace(label, csv_to_md(payload["path"]), 1)
        else:
            raise ValueError(f"Unknown type: {payload['type']}")

    with open(output_file, "w", encoding="utf8") as f:
        f.write(content)


TEMPLATES_PATH = "docs-zh/templates"
OUTPUT_PATH = "docs-zh"

for file in os.listdir(TEMPLATES_PATH):
    if file.endswith(".txt"):
        name, _ = os.path.splitext(file)
        format_md_templates(
            os.path.join(TEMPLATES_PATH, file), os.path.join(OUTPUT_PATH, name + ".md")
        )
shutil.copy("docs-zh/1.项目简介.md", "README_zh.md")