class Service:
    """ 
        Class only to respect the parse interface
    """
    def __init__(self, name=None, tag=None):
        self.name = name
        self.tag = tag
    
    def get_name(self):
        return self.name
        
    def get_tag(self):
        return self.tag

    def parse(self, service_data):
        """
        <serviceName>
        <serviceTag>
        """
        service_data = service_data.split('\n')            
        self.name = service_data[0].strip()
        self.tag  = int(service_data[1].strip(), 16)
    
    def __str__(self):
        return "Tag:{}, Name:{}".format(self.tag, self.name)
        
        

    