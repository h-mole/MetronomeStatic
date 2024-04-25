# PyBirdViewCode静态分析工具

## 简介

PyBirdViewCode是一个用于静态代码分析的Python包，目标是将代码的依赖关系和逻辑关系以图形化、抽象化的形式表示出来，便于程序理解。希望这个包能够帮助大家从更高的角度分析代码，鸟瞰整体，把握全局。

以下是PyBirdViewCode的功能图。现在只支持C/C++，基于libclang实现。在未来，计划进一步添加Python的 AST

```mermaid
graph TD
    C/C++ -->|LibClang| ClangAST
    Python["Python (Implement later...)"] --> PythonAST[Python AST] --> UAST
    
    ClangAST -->|Conversion| UAST

    subgraph `PyBirdViewCode Package Functionalities`

        UAST[Universal AST]
        CommonUtils["Common Utils"]
        
        UAST -->|Control Flow Building| CFG
        UAST -->|Data Dependency Building| DDG["DDG: To be developed..."]
    
    end

    ClangAST --> |Interface| CommonUtils
```

在上面的图中，AST代表抽象语法树，这是一个树形结构
用某种语言表示程序结构。UAST代表通用AST，一个通用的抽象语法树(AST)跨不同语言的表示

以上图中C/C++节点的路径为例。C/C++通过LibClang转换为Clang抽象语法树(Clang AST)，然后Clang AST可以转换为PyBirdViewCode中定义的UAST。UAST可以用来构建控制流图(CFG)和数据依赖图(DDG)

由于UAST可以表示不同语言的AST，因此可以进行控制流和数据流的分析，构建控制流图、数据依赖图等程序图。由于这一过程依赖的UAST与具体的编程语言无关，因此就可以避免添加新语言时重新写一遍构建程序图的逻辑的繁琐情况。

### 支持的编程语言

- C：目前可以使用
- C++：正在开发
- Python：尚未开始

## 安装

```bash
pip install PyBirdViewCode
```

## 示例

### 获取UAST & UAST 的保存与读取

- UAST的文档见：[UAST Docs](https://hzy15610046011.gitee.io/metronome-static/html/api/universal_ast.html)

- 该示例位于`examples/uast-conversion`下

给定一个待分析的C文件:

`examples/uast-conversion/uast-demo.c`

```c
int main(int paramA, int paramB)
{
    if (paramA < 0)
    {
        return -1;
    }
    return paramA + paramB;
}
```

可按如下步骤编程以进行分析:

`examples/uast-conversion/demo.py`

```python
import json

from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import *

# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("uast-demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 使用ClangASTConverter将Cursor对象转换为UAST
converter = ClangASTConverter()
uast = converter.eval(cursor)
print(uast)

# 将UAST转换为JSON格式并保存到文件
with open("dumped-ast.json", "w") as f:
    json.dump(uast.to_dict(), f, indent=2, ensure_ascii=False)

```

运行输出:

`examples/uast-conversion/expected_out.txt`

```plaintext
MethodDeclaration(name='main', modifiers=[], type_parameters=[], parameters=[None, None], return_type='NotImplemented', body=Block(statements=[IfThenElse(predicate=BinaryExpression(operator='<', lhs=Name(value='paramA'), rhs=Literal(value=0)), if_true=Block(statements=[Return(result=Unary(sign='p-', expression=Literal(value=1)))]), if_false=None), Return(result=BinaryExpression(operator='+', lhs=Name(value='paramA'), rhs=Name(value='paramB')))]), abstract=False, extended_dims=0, throws=None)
```

可以看出，直接print输出的结果可读性并不太好，但查看打印出的JSON就轻松多了：

`examples/uast-conversion/dumped-ast.json`

```json
{
  "_cls": "MethodDeclaration",
  "name": "main",
  "modifiers": [],
  "type_parameters": [],
  "parameters": [
    null,
    null
  ],
  "return_type": "NotImplemented",
  "body": {
    "_cls": "Block",
    "statements": [
      {
        "_cls": "IfThenElse",
        "predicate": {
          "_cls": "BinaryExpression",
          "operator": "<",
          "lhs": {
            "_cls": "Name",
            "value": "paramA"
          },
          "rhs": {
            "_cls": "Literal",
            "value": 0
          }
        },
        "if_true": {
          "_cls": "Block",
          "statements": [
            {
              "_cls": "Return",
              "result": {
                "_cls": "Unary",
                "sign": "p-",
                "expression": {
                  "_cls": "Literal",
                  "value": 1
                }
              }
            }
          ]
        },
        "if_false": null
      },
      {
        "_cls": "Return",
        "result": {
          "_cls": "BinaryExpression",
          "operator": "+",
          "lhs": {
            "_cls": "Name",
            "value": "paramA"
          },
          "rhs": {
            "_cls": "Name",
            "value": "paramB"
          }
        }
      }
    ]
  },
  "abstract": false,
  "extended_dims": 0,
  "throws": null
}
```

以上的JSON是一个嵌套结构，每一项的`_cls`属性记录了UAST节点的类名，其余不以下划线开头的属性都是该节点相应对象的属性。

既然UAST可以保存，那么也可这样读取：

`examples/uast-conversion/load_uast.py`

```python
import json

from PyBirdViewCode import universal_ast_nodes as nodes


# 从json文件中加载AST
with open("dumped-ast.json", "r") as f:
    ast = nodes.SourceElement.from_dict(json.load(f))
    print(ast)

```

### 遍历UAST

给定一个C文件：

`examples/uast-traverse/demo.c`

```c
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", a, b);
    printf("Hello World!\n");
}

```

通过以下方法，可以遍历该C文件的所有FuncCall节点，并打印出其函数名：

`examples/uast-traverse/demo.py`

```python
from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import universal_ast_nodes as nodes, ClangASTConverter


class UniASTVisitor(nodes.Visitor):
    def visit_FuncCall(self, node: nodes.CallExpr):
        print(node.name)




# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 获取UAST
ast = ClangASTConverter().eval(cursor)

# 使用UniASTVisitor遍历UAST
ast.accept(UniASTVisitor())

```

输出：

`examples/uast-traverse/out.txt`

```plaintext
Name(value='scanf')
Name(value='printf')
```

### 获取控制流图CFG

给定一个C文件：

`examples/cfg-extraction/demo.c`

```c
#include <stdio.h>

int main(int a, int b)
{
    if (a < 0)
    {
        return -1;
    }
    for (int i = 0; i < b; i++)
    {
        a += i;
    }
}

```

运行如下Python文件将其转换为控制流图，并且输出Dot文件：

`examples/cfg-extraction/demo.py`

```python
import networkx as nx
from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import universal_ast_nodes as nodes, ClangASTConverter, CFGBuilder


# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 获取UAST
ast = ClangASTConverter().eval(cursor)

# 使用CFGBuilder构建CFG
cfg_builder = CFGBuilder()
cfg_builder.build(ast)

# 将CFG转换为networkx的网络，并且保存为dot
# 得到.dot文件之后，可以用
#  `dot -Tpng cfg.dot -o cfg.png`转化cfg.dot为图片
g = cfg_builder.to_networkx()
nx.nx_pydot.write_dot(g, "cfg.dot")

```

得到.dot文件之后，可以用`dot -Tpng cfg.dot -o cfg.png`转化cfg.dot为png格式的图片，如下图：

![生成的控制流图](examples/cfg-extraction/cfg.png)

注意，如果提示没有安装dot，可以按照<https://graphviz.org/download/> 这里的方式进行安装

## Interfaces

### Clang

Clang interface included some useful functionalities.

## 未来计划

### Supporting DDG

### Supporting other languages such as Python

### Code to UML
