from misc.constants import PROCESS, CID, PEB, PARENTCID, IMAGE

class ProcessInfo:
    def __init__(self):
        self.process_number = None 
        self.cid = None 
        self.peb = None 
        self.parent_cid = None 
        self.process_name = None 

    def get_process_name(self):
        return self.process_name

    def get_process_number(self):
        return self.process_number
        
    def get_cid(self):
        return self.cid
        
    def get_peb(self):
        return self.peb
        
    def get_parent_cid(self):
        return self.parent_cid
        
    def parse(self, process_info_data):
        """
            PROCESS ffffe287bcbeb780
            SessionId: 1  Cid: 0ab4    Peb: 00f42000  ParentCid: 0a8c
            DirBase: 22ee6000  ObjectTable: ffff8f81b7679b00  HandleCount: <Data Not Accessible>
            Image: explorer.exe
        """
        all_parsed_items_or_values = []
        for process_info in process_info_data.split("\n"):
            for item_or_value in process_info.split(" "):
                if item_or_value.strip():
                    all_parsed_items_or_values.append(item_or_value)

        for index in range(len(all_parsed_items_or_values)):
            current_value = all_parsed_items_or_values[index].replace(":","")

            if index < len(all_parsed_items_or_values) - 1:
                next_value = all_parsed_items_or_values[index+1]
            else:
                break

            if  current_value == PROCESS:
                self.process_number = next_value
            elif current_value == CID:
                self.cid = next_value
            elif current_value == PEB:
                self.peb = next_value
            elif current_value == PARENTCID:
                self.parent_cid = next_value
            elif current_value == IMAGE:
                self.process_name = next_value
        
        # Replace with assert
        if not self.process_number or not self.cid or not self.peb or not self.parent_cid or not self.process_name:
            raise Exception("Not all values could be assinged when trying to parse Process Info")
    

    def __str__(self):
        output = ""
        for key, value in self.__dict__.items():
            output += "{}: {}\n".format(key, value)
        return output





        

