import json
import os
import re
import shutil
import sys
import pandas as pd
import networkx as nx


def csv_to_md(csv_file):
    # 读取CSV文件
    data = pd.read_csv(csv_file)

    # 将数据转换为MD格式
    md_data = data.to_markdown()

    return md_data


def format_multiline_docs(doc_str: str):
    lines = doc_str.split("\n")
    new_text_lines = []
    for l in lines:
        if l.startswith(" " * 4):
            new_text_lines.append(l[4:])
        elif not l.startswith(" "):
            new_text_lines.append(l)
    return "\n".join(new_text_lines)


def parse_annotation(annotation) -> str:

    if annotation is None:
        return "Any"
    if type(annotation) == type:
        CLASS_ALIASES = {nx.DiGraph: "nx.DiGraph"}
        if annotation in CLASS_ALIASES:
            return CLASS_ALIASES[annotation]
        return annotation.__name__
    raise NotImplementedError(annotation)


def get_function_doc(func: "function"):
    func_name = func.__name__
    doc_content = format_multiline_docs(func.__doc__)
    lines = doc_content.splitlines()
    annotations = func.__annotations__
    print(annotations)
    args_desc = []
    descs = []
    for line in lines:
        if (
            (matched := re.search(r":([a-zA-Z0-9_]+):", line)) is not None
        ) and matched.group() is not None:
            arg_name = matched.groups()[0]
            doc_str = line.split(":", 2)[2].lstrip()
            args_desc.append(
                f"- **{arg_name} (`{parse_annotation(annotations.get(arg_name))}`)**: {doc_str}"
            )
        else:
            descs.append(line)
    args_str = "\n".join(args_desc)
    descs_str = "\n".join(descs)
    return f"### {func_name}\n\n**说明：**\n\n{descs_str}\n\n**参数列表**:\n\n{args_str}\n\n**返回类型**：\n\n- {parse_annotation(annotations.get('return'))}"


file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.dirname(file_dir)))
sys.path.append(".")


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
        elif payload.get("kind") == "docs":
            from importlib import import_module

            module_name = payload["module"]
            module = import_module(module_name)
            docs_list = []
            match payload:
                case {"function": func_name}:
                    func = module.__dict__[func_name]
                    doc_content = get_function_doc(func)
                    content = content.replace(label, doc_content)
                case _:
                    for name, obj in module.__dict__.items():
                        if not name.startswith("__") and callable(obj):
                            docs_list.append(
                                f"{name}: {format_multiline_docs(obj.__doc__) if obj.__doc__ is not None else ''}"
                            )
                    content = content.replace(label, "\n".join(docs_list))
        else:
            raise ValueError(f"Unknown type: {payload}")

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
