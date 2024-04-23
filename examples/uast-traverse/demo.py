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
