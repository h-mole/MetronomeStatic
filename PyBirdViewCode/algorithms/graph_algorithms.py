from typing import List, Tuple, Union
import networkx as nx

ValidNodeKinds = Union[str, int, tuple]


class graph_algorithms:

    def __init__(self, *args, **kwargs) -> None:
        raise ValueError(
            f"The class {self.__class__.__name__} is just a wrapper, please do not instantiate it"
        )

    @classmethod
    def get_entry(cls, G: nx.DiGraph):
        entries = list(filter(lambda n: G.in_degree(n) == 0, G.nodes))
        assert len(entries) == 1
        return entries[0]

    @classmethod
    def get_exit(cls, G: nx.DiGraph):
        exits = list(filter(lambda n: G.out_degree(n) == 0, G.nodes))
        assert len(exits) == 1
        return exits[0]

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

    @classmethod
    def update_out_edge_with_order(
        cls,
        G: nx.DiGraph,
        src: ValidNodeKinds,
        old_dst: ValidNodeKinds,
        new_dst: ValidNodeKinds,
    ):
        """
        更新出边的连接关系，并且保证连边的顺序。
        比如节点1，按顺序有2，3，4这三个邻居节点
        那么如果调用该方法，将边1->3改为1->5，那么这三个邻居节点的顺序为：
        2, 5, 4。

        注意：此方法会修改传入的图对象G
        """
        out_edges = list(G.out_edges(src))
        G.remove_edges_from(out_edges)
        old_edge_index = out_edges.index((src, old_dst))
        out_edges[old_edge_index] = (src, new_dst)
        G.add_edges_from(out_edges)
