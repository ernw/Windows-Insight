from graphs.writesPerMinuteGraph import WritesPerMinuteGraph
from graphs.amountOfCallsPerProcessGraph import AmountOfCallsPerProcessGraph
from graphs.svchostGraph import SVCHostGraph
from graphs.graph import Graph

class GraphsHelper:
    def __init__(self, writes_info):
        self.writes_info = writes_info
        self.graphs = Graph.__subclasses__()
        self.graphs_built_data = []

    def build_graphs_data(self):
        """ 
            This function will build all the data related to graphs for 
            each particular graph but an uniformed way.
        """
        for graph in self.graphs:
            gph = graph()
            gph.build_graph_data(self.writes_info)
            self.graphs_built_data.append(gph)

    def get_all_graphs_data(self):
        """    
            This function will return a list of graphs data.
        """
        graphs_data = []
        for graph_built_data in self.graphs_built_data:
            graphs_data.append(graph_built_data.get_graph_data())
        return graphs_data
    