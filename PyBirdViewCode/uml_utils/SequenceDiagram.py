from .Visitor import *
import sys
from ..universal_ast import universal_ast_nodes as nodes


class NoClassExists(Exception):
    def __init__(self, className):
        self.value = "No class named: " + className + " exists in the file"


class NoMethodExists(Exception):
    def __init__(self, methodName):
        self.value = "No method name: " + methodName + " exists"


def ast_to_diagram(ast: nodes.MethodDecl, output_file: str):
    invocationList = []
    ast.accept(UniASTVisitor(invocationList))
    className = "default"
    if len(invocationList) == 0:
        print("Method was not found, or it does not contain any method invocations")
    else:
        with open(output_file, "w") as f:
            f.write("@startuml \n")
            for invocation in invocationList:
                if isinstance(invocation, LoopStart):
                    f.write("loop \n")
                elif isinstance(invocation, LoopEnd):
                    f.write("end\n")
                else:
                    if invocation.getClass() == None:
                        # self referential -- method invocation is member of class
                        f.write(
                            className
                            + " -> "
                            + className
                            + " : "
                            + invocation.getName()
                            + "\n"
                        )
                    else:
                        f.write(
                            className
                            + " -> "
                            + invocation.getClass()
                            + " : "
                            + invocation.getName()
                            + "\n"
                        )
                        f.write(invocation.getClass() + " -> " + className + "\n")
            f.write("@enduml")
