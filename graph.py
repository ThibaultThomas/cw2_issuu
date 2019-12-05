from graphviz import Digraph


class Graph:

    def __init__(self, plot, document, uuid):
        self.data = plot
        self.graph = Digraph("test", format="ps")
        self.document = document
        self.uuid = uuid
        self.createNodes()
        self.view()


    def createNodes(self):
        self.graph.node(getNodeName(self.document), style='filled', shape="circle", color="green")
        #self.graph.edge(getNodeName(self.uuid), getNodeName(self.document))

        if self.data.userHasReadDocument(self.document, self.uuid):
            self.graph.edge(getNodeName(self.uuid), getNodeName(self.document))
            #self.graph.node(getNodeName(self.uuid), style='filled', shape="square", color="green")

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


def getNodeName(string):
    return string[-4:]
