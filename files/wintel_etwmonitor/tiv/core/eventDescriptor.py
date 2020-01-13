from misc.constants import  ED_ID,ED_VERSION,ED_CHANNEL,ED_LEVEL,ED_OPCODE,ED_TASK,ED_KEYWORD
class EventDescriptor:
    def __init__(self):
        self.id = None
        self.version = None
        self.channel = None
        self.level = None
        self.opcode = None
        self.task = None
        self.keyword = None
    
    def get_id(self):
        return self.id

    def get_version(self):
        return self.version

    def get_channel(self):
        return self.channel

    def get_level(self):
        return self.level

    def get_opcode(self):
        return self.opcode

    def get_task(self):
        return self.task

    def get_keyword(self):
        return self.keyword

    def _parse_event_descriptor_value(self, value):
        if "'" in value:
            return int(value.split(" ")[0],16)
        elif "`" in value:
            return int(value.replace("`","").strip(),16)
        else:
            return int(value.strip(),16)

    def parse(self, event_descriptor_data):
        """
            +0x000 Id               : 0x30ea
            +0x002 Version          : 0 ''
            +0x003 Channel          : 0xb ''
            +0x004 Level            : 0x5 ''
            +0x005 Opcode           : 0 ''
            +0x006 Task             : 0
            +0x008 Keyword          : 0x00008000`00000000
        """
        
        for line in event_descriptor_data.split('\n'):
            if line:    
                address_and_attribute, value = line.split(":")
                address, attribute = address_and_attribute.strip().split(" ")
                real_value = self._parse_event_descriptor_value(value.strip())
                if ED_ID in attribute.lower():
                    self.id = real_value
                elif ED_VERSION in attribute.lower():
                    self.version = real_value
                elif ED_CHANNEL in attribute.lower():
                    self.channel = real_value
                elif ED_LEVEL in attribute.lower():
                    self.level = real_value
                elif ED_OPCODE in attribute.lower():
                    self.opcode = real_value
                elif ED_TASK in attribute.lower():
                    self.task = real_value
                elif ED_KEYWORD in attribute.lower():
                    self.keyword = real_value
                else:
                    raise Exception("Invalid attribute when trying to parse Event Descriptor data. Line: {}".format(line))
    

    def __str__(self):
        output = ""
        for key, value in self.__dict__.items():
            output += "{}: {}\n".format(key,hex(value))
        return output
