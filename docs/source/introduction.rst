Introduction
============

MetronomeStatic is a Python package for static code analysis. 
It acts as an interface over a set of common static-analysis packages such as Clang and Joern.

Here is the map of the functionalities of MetronomeStatic. Now only a LibClang-based 
C/C++ AST is supported, and Python AST is planned to be extended further.

.. mermaid::

    graph TD
        C/C++ -->|LibClang| ClangAST
        Python["Python (Implement later...)"] --> PythonAST[Python AST] --> UAST
        
        ClangAST -->|Conversion| UAST

        subgraph `MetronomeStatic Package Functionalities`

            UAST[Universal AST]
            CommonUtils["Common Utils"]
            
            UAST -->|Control Flow Building| CFG
            UAST -->|Data Dependency Building| DDG["DDG: To be developed..."]
        
        end

        ClangAST --> |Interface| CommonUtils

In the graph above, AST stands for Abstract Syntax Tree, a tree-like structure that 
represents the program structure in a certain language. UAST stands for Universal AST, a universal
representation of Abstract Syntax Tree(AST)s across different languages. 

Take the route from node C/C++ in the graph above as an example. C/C++ code are converted to
Clang Abstract Syntax Tree (Clang AST) by `LibClang`, and then the Clang AST could be 
converted to the Universal AST defined in MetronomeStatic. After that, the Universal AST
could be used to build Control Flow Graph (CFG) and Data Dependency Graph (DDG).

As UAST could represent ASTs of different languages, the CFG-building and DDG-building
processes are language-agnostic, needing few rework when adding a new language.


Please visit `Tutorial <./tutorial/_index.html>`_ for details