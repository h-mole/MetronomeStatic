import ast


class FunctionDeclVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_decl_nodes = []

    def visit_Assign(self, node):
        if (
            isinstance(node.targets[0], ast.Attribute)
            and isinstance(node.targets[0].value, ast.Name)
            and node.targets[0].value.id == "CursorKind"
        ):
            if (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "CursorKind"
                and isinstance(node.value.args[0], ast.Constant)
            ):
                self.function_decl_nodes.append(
                    (node.targets[0].attr, node.value.args[0].value)
                )
        self.generic_visit(node)


def extract_function_decl_nodes(code):
    tree = ast.parse(code)
    visitor = FunctionDeclVisitor()
    visitor.visit(tree)
    return visitor.function_decl_nodes
