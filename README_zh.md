# PyBirdViewCode��̬��������

## ���

PyBirdViewCode��һ�����ھ�̬���������Python����Ŀ���ǽ������������ϵ���߼���ϵ��ͼ�λ������󻯵���ʽ��ʾ���������ڳ�����⡣ϣ��������ܹ�������ҴӸ��ߵĽǶȷ������룬������壬����ȫ�֡�

������PyBirdViewCode�Ĺ���ͼ������ֻ֧��C/C++������libclangʵ�֡���δ�����ƻ���һ�����Python�� AST

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

�������ͼ�У�AST��������﷨��������һ�����νṹ
��ĳ�����Ա�ʾ����ṹ��UAST����ͨ��AST��һ��ͨ�õĳ����﷨��(AST)�粻ͬ���Եı�ʾ

����ͼ��C/C++�ڵ��·��Ϊ����C/C++ͨ��LibClangת��ΪClang�����﷨��(Clang AST)��Ȼ��Clang AST����ת��ΪPyBirdViewCode�ж����UAST��UAST������������������ͼ(CFG)����������ͼ(DDG)

����UAST���Ա�ʾ��ͬ���Ե�AST����˿��Խ��п��������������ķ���������������ͼ����������ͼ�ȳ���ͼ��������һ����������UAST�����ı�������޹أ���˾Ϳ��Ա������������ʱ����дһ�鹹������ͼ���߼��ķ��������

### ֧�ֵı������

- C��Ŀǰ����ʹ��
- C++�����ڿ���
- Python����δ��ʼ

## ��װ

```bash
pip install PyBirdViewCode
```

## ʾ��

### ��ȡUAST & UAST �ı������ȡ

- UAST���ĵ�����[UAST Docs](https://hzy15610046011.gitee.io/metronome-static/html/api/universal_ast.html)

- ��ʾ��λ��`examples/uast-conversion`��

����һ����������C�ļ�:

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

�ɰ����²������Խ��з���:

`examples/uast-conversion/demo.py`

```python
import json

from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import *

# ��ȡ Clang AST ��Cursor����
file_cursor = parse_file("uast-demo.c").cursor

# ��ȡ����main��Cursor����
cursor = get_func_decl(file_cursor, "main")

# ʹ��ClangASTConverter��Cursor����ת��ΪUAST
converter = ClangASTConverter()
uast = converter.eval(cursor)
print(uast)

# ��UASTת��ΪJSON��ʽ�����浽�ļ�
with open("dumped-ast.json", "w") as f:
    json.dump(uast.to_dict(), f, indent=2, ensure_ascii=False)

```

�������:

`examples/uast-conversion/expected_out.txt`

```plaintext
MethodDeclaration(name='main', modifiers=[], type_parameters=[], parameters=[None, None], return_type='NotImplemented', body=Block(statements=[IfThenElse(predicate=BinaryExpression(operator='<', lhs=Name(value='paramA'), rhs=Literal(value=0)), if_true=Block(statements=[Return(result=Unary(sign='p-', expression=Literal(value=1)))]), if_false=None), Return(result=BinaryExpression(operator='+', lhs=Name(value='paramA'), rhs=Name(value='paramB')))]), abstract=False, extended_dims=0, throws=None)
```

���Կ�����ֱ��print����Ľ���ɶ��Բ���̫�ã����鿴��ӡ����JSON�����ɶ��ˣ�

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

���ϵ�JSON��һ��Ƕ�׽ṹ��ÿһ���`_cls`���Լ�¼��UAST�ڵ�����������಻���»��߿�ͷ�����Զ��Ǹýڵ���Ӧ��������ԡ�

��ȻUAST���Ա��棬��ôҲ��������ȡ��

`examples/uast-conversion/load_uast.py`

```python
import json

from PyBirdViewCode import universal_ast_nodes as nodes


# ��json�ļ��м���AST
with open("dumped-ast.json", "r") as f:
    ast = nodes.SourceElement.from_dict(json.load(f))
    print(ast)

```

### ����UAST

����һ��C�ļ���

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

ͨ�����·��������Ա�����C�ļ�������FuncCall�ڵ㣬����ӡ���亯������

`examples/uast-traverse/demo.py`

```python
from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import universal_ast_nodes as nodes, ClangASTConverter


class UniASTVisitor(nodes.Visitor):
    def visit_FuncCall(self, node: nodes.CallExpr):
        print(node.name)




# ��ȡ Clang AST ��Cursor����
file_cursor = parse_file("demo.c").cursor

# ��ȡ����main��Cursor����
cursor = get_func_decl(file_cursor, "main")

# ��ȡUAST
ast = ClangASTConverter().eval(cursor)

# ʹ��UniASTVisitor����UAST
ast.accept(UniASTVisitor())

```

�����

`examples/uast-traverse/out.txt`

```plaintext
Name(value='scanf')
Name(value='printf')
```

### ��ȡ������ͼCFG

����һ��C�ļ���

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

��������Python�ļ�����ת��Ϊ������ͼ���������Dot�ļ���

`examples/cfg-extraction/demo.py`

```python
import networkx as nx
from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import universal_ast_nodes as nodes, ClangASTConverter, CFGBuilder


# ��ȡ Clang AST ��Cursor����
file_cursor = parse_file("demo.c").cursor

# ��ȡ����main��Cursor����
cursor = get_func_decl(file_cursor, "main")

# ��ȡUAST
ast = ClangASTConverter().eval(cursor)

# ʹ��CFGBuilder����CFG
cfg_builder = CFGBuilder()
cfg_builder.build(ast)

# ��CFGת��Ϊnetworkx�����磬���ұ���Ϊdot
# �õ�.dot�ļ�֮�󣬿�����
#  `dot -Tpng cfg.dot -o cfg.png`ת��cfg.dotΪͼƬ
g = cfg_builder.to_networkx()
nx.nx_pydot.write_dot(g, "cfg.dot")

```

�õ�.dot�ļ�֮�󣬿�����`dot -Tpng cfg.dot -o cfg.png`ת��cfg.dotΪpng��ʽ��ͼƬ������ͼ��

![���ɵĿ�����ͼ](examples/cfg-extraction/cfg.png)

ע�⣬�����ʾû�а�װdot�����԰���<https://graphviz.org/download/> ����ķ�ʽ���а�װ

## Interfaces

### Clang

Clang interface included some useful functionalities.

## δ���ƻ�

### Supporting DDG

### Supporting other languages such as Python

### Code to UML
