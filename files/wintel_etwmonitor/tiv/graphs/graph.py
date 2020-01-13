class Graph:    
    def build_graph_data(self, writes_info):
        """
            This functions build the necessary internal structure 
            that afterwards will be provided to the GraphData object
        """
        return NotImplementedError

    def get_graph_data(self):
        """
            Returns the GraphData object related with the data
            fullfilled of the corresponding graph.
        """
        return NotImplementedError
        