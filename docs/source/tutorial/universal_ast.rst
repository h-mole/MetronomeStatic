====================
Universal AST (UAST)
====================

UAST is a universal representation of ASTs across different languages. The UAST from
MetronomeStatic comes from the project `PLYJ <https://github.com/musiKk/plyj>`_, and modified for
representing C/C++ ASTs.

The API document of UAST is 
:doc:`HERE </api/universal_ast>`.


Here is a C file, ``assets/uast-demo.c``:

.. literalinclude:: /examples/assets/uast-demo.c
   :language: cpp
   :linenos:

To convert this file to UAST, just code like ``get_uast.py``:

.. literalinclude:: /examples/get_uast.py
   :language: python
   :linenos:

The generated JSON representation of UAST is shown below:

.. literalinclude:: /examples/outputs/dumped-ast.json
   :language: json
   :linenos: