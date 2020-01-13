from collections import OrderedDict
from core.service import Service

class ServicesDatabase:
    def __init__(self):
        self.db = OrderedDict()

    def dump_as_list(self):
        return list(self.db.items())

    def add_service(self, service):
        tag = service.get_tag()
        name = service.get_name()
        self.db.update({tag:name})

    def get_service_name_from_tag(self, tag):
        """ 
            TAG is an heximal str value.
        """
        return self.db.get(int(tag,16))

    def parse(self, services_db_data):
        """
        <service_name1>
        <service_name2>
        ...
        <service_nameN>
        """
        self.db = OrderedDict()
        tag = 1
        for service_name in services_db_data.split("\n"):
            service = Service(name=service_name, tag=tag)
            self.add_service(service)
            tag += 1

    def __str__():
        output = ""
        for tag, name in self.db.items():
            output += "{}: {}\n".format(tag, name)
        return output       
        
    

    
