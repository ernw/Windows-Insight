from misc.constants import SVCHOST_PROCESS_NAME,SVC_NAME, SVC_TYPE, SVC_LABEL, SVC_TITLE, SVC_FILENAME, SVC_DISPLAY_LEGEND, SVC_GRAPH_WITH_TIME, JS_EXTENSION
from core.graphData import GraphData
from misc.logger import logger
from graphs.graph import Graph

class SVCHostGraph(Graph):
    def __init__(self):
        self.amount_of_calls_per_service = {}
    
    
    def build_graph_data(self, writes_info):
        """ 
            This function builds all the data for the graph
        """
        for write_info in writes_info:
            process_name = write_info.get_process_info().get_process_name()
            if process_name == SVCHOST_PROCESS_NAME:
                service = write_info.get_service()
                if service:
                    service_name = service.get_name()
                    if service_name in self.amount_of_calls_per_service.keys():
                        self.amount_of_calls_per_service[service_name] += 1
                    else:
                        self.amount_of_calls_per_service.update({service_name:1})
                else:
                    logger.warning("The {} write, is a svcinfo write and hasn't service associated!".format(write_info.get_offset()))


    def get_graph_data(self):
        """
            Returns the GraphData object related to the data of this graph
        """
        list_format = list(self.amount_of_calls_per_service.items())
        labels = [elem[0] for elem in list_format]
        values = [elem[1] for elem in list_format]

        return GraphData(SVC_NAME, SVC_TYPE,values, labels, SVC_LABEL,
                         SVC_TITLE, SVC_FILENAME + JS_EXTENSION,
                         SVC_DISPLAY_LEGEND, SVC_GRAPH_WITH_TIME)
         
