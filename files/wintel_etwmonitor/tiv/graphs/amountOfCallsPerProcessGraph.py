from misc.constants import (CPP_NAME, CPP_TYPE, CPP_LABEL, CPP_TITLE,
                      CPP_FILENAME, JS_EXTENSION, CPP_DISPLAY_LEGEND,
                      CPP_GRAPH_WITH_TIME)
from core.graphData import GraphData
from graphs.graph import Graph

class AmountOfCallsPerProcessGraph(Graph):
    def __init__(self):
        self.calls_per_process_name = {}

    def build_graph_data(self, writes_info):
        """ 
            This function builds all the data for the graph
        """
        for write_info in writes_info:
            process_name = write_info.get_process_info().get_process_name()
            if process_name in self.calls_per_process_name.keys():
                self.calls_per_process_name[process_name] += 1
            else:
                self.calls_per_process_name.update({process_name:1})
        
    def get_graph_data(self):
        """
            Returns the GraphData object related to the data of this graph
        """
        list_format = list(self.calls_per_process_name.items())
        labels = [elem[0] for elem in list_format]
        values = [elem[1] for elem in list_format]

        return GraphData(CPP_NAME, CPP_TYPE,values, labels, CPP_LABEL,
                         CPP_TITLE, CPP_FILENAME + JS_EXTENSION,
                         CPP_DISPLAY_LEGEND, CPP_GRAPH_WITH_TIME)
         

    