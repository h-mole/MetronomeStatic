import ast


class FunctionDeclVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_decl_nodes = []

    def visit_Assign(self, node):
        print(ast.dump(node))
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


# def unparse_function_decl_nodes(nodes):
#     return [astunparse.unparse(node).strip() for node in nodes]

if __name__ == "__main__":
    import clang.cindex as cindex

    print(cindex.__file__)
    with open(cindex.__file__) as f:
        function_decl_nodes = extract_function_decl_nodes(f.read())
        print(function_decl_nodes)
