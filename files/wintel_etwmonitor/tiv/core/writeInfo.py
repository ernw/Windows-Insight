class WriteInfo:
    def __init__(self, date, provider_guid, call_stack, process_info, peb_info, event_descriptor, event_json_format, service=None, offset=0):
        self.date = date
        self.provider_guid = provider_guid
        self.call_stack = call_stack
        self.process_info = process_info
        self.peb_info = peb_info
        self.event_descriptor = event_descriptor
        self.event_json_format = event_json_format
        self.service = service
        self.offset = offset

    def get_date(self):
        return self.date

    def get_provider_guid(self):
        return self.provider_guid

    def get_call_stack(self):
        return self.call_stack

    def get_process_info(self):
        return self.process_info

    def get_peb_info(self):
        return self.peb_info

    def get_event_descriptor(self):
        return self.event_descriptor

    def get_event_json_format(self):
        return self.event_json_format

    def get_service(self):
        return self.service

    def get_offset(self):
        return self.offset

    def __str__(self):
        output = "Write Info Number {}".format(self.offset) 
        output += "{}\n".format(self.date)
        output += "{}\n".format(self.provider_guid)
        output += "{}\n".format(self.call_stack)
        output += "{}\n".format(self.process_info)
        output += "{}\n".format(self.peb_info)
        output += "{}\n".format(self.event_descriptor)
        output += "{}\n".format(self.event_json_format)
        if self.service:
            output += "{}\n".format(self.service)
        return output        