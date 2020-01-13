class ServiceTag:
    def __init__(self):
        self.service_tag = None

    def get_tag(self):
        return self.service_tag

    def parse(self, service_tag_data):
        """ 
        <service_tag>
        """
        self.service_tag = service_tag_data.strip()
    
    def __str__(self):
        return "Service Tag: {}".format(self.service_tag)