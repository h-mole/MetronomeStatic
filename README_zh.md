# MetronomeStatic静态分析工具

## 安装

```bash
pip install MetronomeStatic
```

## 架构图

```mermaid
graph TD
    C/C++ -->|LibClang| ClangAST
    Python["Python (Implement later...)"] --> ClangAST

    ClangAST -->|Conversion| UAST[Universal AST]
    UAST -->|Control Flow Building| CFG
    UAST -->|Data Dependency Building| DDG["DDG: To be developed..."]
    
```

## Interfaces

### Clang

Clang interface included some useful functionalities.

## Plannings

### Supporting DDG

### Supporting other languages such as Python

### Code to UML
