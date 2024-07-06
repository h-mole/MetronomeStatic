import json
import re

with open("README_zh_template.md", "r", encoding="utf8") as f:
    content = f.read()

for label in filter(lambda line: line.startswith("MACRO"), content.splitlines()):
    macro = label.strip("MACRO").strip()
    print(macro)
    payload = json.loads(macro)
    if payload.get("kind") == "file":

        with open(payload["path"], encoding="utf-8") as f:
            file_content = f.read()
            if (lang := payload.get("language")) is not None:
                file_content = (
                    (f"`{payload['path']}`\n")
                    + f"\n```{lang}\n"
                    + file_content
                    + "\n```"
                )
            content = content.replace(label, file_content)
    else:
        raise ValueError(f"Unknown type: {payload['type']}")


with open("README_zh.md", "w") as f:
    f.write(content)
