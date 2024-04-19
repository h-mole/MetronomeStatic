===========
Clang Utils
===========

Submodule `clang_utils` is a low-level API taking advantage of Clang and its python binding 
`libclang`, making it easier to extract program information from C/CPP source code.

Example files are stored in ``docs/source/examples``.

Loading Source Code & Printing AST
==================================

Now, we have C file ``assets/load_ast.c``

.. literalinclude:: /examples/assets/load_ast.c
   :language: cpp
   :linenos:

The Python script ``load_ast.py`` can parse this C file and dump AST.

Note that ``sys.path.append`` expression is used to let the interpreter 
know where ``PyBirdViewCode`` package is placed when in development.
**If you have installed** ``PyBirdViewCode`` **by pip, expression** ``sys.path.append`` **is not necessary.**
This is also true for the other Python scripts below.

.. literalinclude:: /examples/load_ast.py
   :language: python
   :linenos:

The output message below (some lines were omitted) showed that
we could convert Clang AST of function ``main``  to JSON in this way.

.. literalinclude:: /examples/outputs/load_ast.out.txt
   :language: plaintext

Querying The AST Interactively
==============================

Querying AST can be annoying when handling a lot of recursions and loops.
In this framework, inspired by **Joern**, a Scala-based code-analysis framework,
we developed a functional API to access the AST. 

For C file ``assets/interactive_query.c`` shown below:

.. literalinclude:: /examples/assets/interactive_query.c
   :language: cpp
   :linenos:

To get the AST of function ``main``, we could write code like this:

.. literalinclude:: /examples/interactive_query_1.py
   :language: python
   :linenos:

The output is:

.. literalinclude:: /examples/outputs/interactive_query_1.out.txt
   :language: plaintext
   :linenos:

Querying Code Attributes
========================

---------------------
Queries for Variables
---------------------

Now, we have C file ``assets/query_variables.c``.

.. literalinclude:: /examples/assets/query_variables.c
   :language: cpp
   :linenos:

The Python script ``query_variables.py`` can parse this C file and query variables in this file or specific function.

In this script, we took some advantage of **functional programming**.

* For functions like ``get_local_var_defs``, it returns a generator ``SkyGenerator``, yielding a ``clang.cindex.Cursor`` object for each iteration. 

* This generator supports some common patterns of functional programming, such as ``map``, ``filter`` and ``head``. Visit `here <../api/common_utils.html#PyBirdViewCode.utils.SkyGenerator>`_ for details.

* Method ``.attribute("spelling")`` is a shortcut for ``.map(lambda node: node.spelling)``

.. literalinclude:: /examples/query_variables.py
   :language: python
   :linenos:

As the output message shown below:

* In file ``assets/query_variables.c``, global variable ``a`` was defined.
* Function ``demo_1`` defined local variables ``b`` and ``c`` inside, had parameter variable ``d``, and referenced global variable ``a``.


.. literalinclude:: /examples/outputs/query_variables.out.txt
   :language: plaintext
   :linenos:

-------------------
Parsing Expressions
-------------------

Now, we have C file ``assets/parse_expression.c``.
This file contains a series of operators.

.. literalinclude:: /examples/assets/parse_expression.c
   :language: cpp
   :linenos:

The Python script ``parse_expression.py`` can parse all binary/unary operators inside function ``demo``:

.. literalinclude:: /examples/parse_expression.py
   :language: python
   :linenos:

As the output shown below:

* For unary operator, the third returning parameter of ``split_unary_operator`` (local variable ``pos``), indicated the position of operator.  
   * UnaryOpPos is an ``Enum`` with optional values ``UnaryOpPos.AFTER`` and ``UnaryOpPos.BEFORE``.
   *  ``UnaryOpPos.AFTER`` indicates that the operator appears after the operated expression, such as ``p++``
   *  ``UnaryOpPos.BEFORE`` indicates that the operator appears before the operated expression, such as ``++i``, ``&p``

* Assignment operator is one of binary operator

.. literalinclude:: /examples/outputs/parse_expression.out.txt
   :language: plaintext
   :linenos: