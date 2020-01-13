from misc.auxiliaries import guid_structure_to_guid_representation

class ProviderGUID:
    def __init__(self):
        self.guid = None

    def get_guid(self):
        return self.guid
    
    def parse(self, guid_data):
        """
            46D31B9D487D6E37 538ADF8BCE54FDA8
        """
        self.guid = guid_structure_to_guid_representation(guid_data.strip().replace(" ",""))

    def __str__(self):
        return self.guid
