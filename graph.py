from graphviz import Digraph
import data_analyzer


class Graph:

    def __init__(self, plot_instance: data_analyzer, document: str, uuid: str) -> None:
        """

        Create a Graph object

        :param plot_instance: The plot instance
        :param document: The document uuid
        :param uuid: The user uuid
        """
        self.data = plot_instance
        self.graph = Digraph("test", format="ps")
        self.document = document
        self.uuid = uuid
        self.createNodes()
        self.view()

    def createNodes(self) -> None:
        """
            This function create nodes
        """
        self.graph.node(getNodeName(self.document), style='filled', shape="circle", color="green")

        if self.data.userHasReadDocument(self.document, self.uuid):
            self.graph.edge(getNodeName(self.uuid), getNodeName(self.document))
            self.graph.node(getNodeName(self.uuid), style='filled', shape="square", color="green")

        mp = self.data.topTenDocumentsWithAuthor(self.document, self.uuid)
        for key, value in mp.items():
            for z in value:
                self.graph.edge(getNodeName(z), getNodeName(key))
        buffer = []
        for value in mp.values():
            for z in value:
                if z not in buffer:
                    self.graph.edge(getNodeName(z), getNodeName(self.document))
                    buffer.append(z)

    def view(self):
        self.graph.view()


def getNodeName(string: str) -> str:
    """

    :param string: The string to crop
    :return: The cropped string (4 character from the end)
    """
    if len(string) > 4:
        return string[-4:]
    return string
