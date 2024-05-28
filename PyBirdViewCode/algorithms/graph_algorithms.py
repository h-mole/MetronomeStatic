from typing import List, Tuple, Union
import networkx as nx

ValidNodeKinds = Union[str, int, tuple]


class graph_algorithms:

    def __init__(self, *args, **kwargs) -> None:
        raise ValueError(
            f"The class {self.__class__.__name__} is just a wrapper, please do not instantiate it"
        )

    @classmethod
    def get_entries_and_exits(
        cls,
        G: nx.DiGraph,
    ) -> Tuple[List[ValidNodeKinds], List[ValidNodeKinds]]:
        """
        Get all the entry nodes and exit nodes of the graph
        """
        entries = list(filter(lambda n: G.in_degree(n) == 0, G.nodes))
        exits = list(filter(lambda n: G.out_degree(n) == 0, G.nodes))
        return entries, exits

    @classmethod
    def get_entry_and_exit(cls, G: nx.DiGraph) -> Tuple[ValidNodeKinds, ValidNodeKinds]:
        """
        Get the entry and exit node of the graph,
        requiring the graph to have only one entry and one exit

        """
        entries, exits = cls.get_entries_and_exits(G)
        assert len(entries) == 1
        assert len(exits) == 1
        return entries[0], exits[0]
