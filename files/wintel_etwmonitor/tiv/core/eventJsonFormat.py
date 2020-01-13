from core.exceptions import ErrorWhenParsing
from misc.constants import (OPENING_BRACKET, EJF_FOUND_BUFFERS, CLOSING_BRACKET, OPENING_BRACE,
                      CLOSING_BRACE, EJF_NO_BUFFERS_FOUND)
class EventJsonFormat:
    def __init__(self):
        self.event_json = None
        self.sender = None

    def get_event_json(self):
        return self.event_json

    def get_sender(self):
        return self.sender

    def _parse_line_with_event_json_format(self, line_with_event_json_format):
        # Skip first the characters
        line_with_event_json_format = line_with_event_json_format[3:]
        index_of_opening_bracket = line_with_event_json_format.index(OPENING_BRACKET)
        index_of_closing_bracket = line_with_event_json_format.index(CLOSING_BRACKET)
        index_of_opening_brace = line_with_event_json_format.index(OPENING_BRACE)
        index_of_closing_brace = line_with_event_json_format.index(CLOSING_BRACE)

        self.sender = line_with_event_json_format[index_of_opening_bracket+1:index_of_closing_bracket]
        self.event_json = line_with_event_json_format[index_of_opening_brace:index_of_closing_brace+1]

    
    def parse(self,event_json_format_data):
        """
            (WmiTrace) LogDump for Logger Id 0x21
            Reading Buffer   1 /   4
            Reading Buffer   2 /   4
            Reading Buffer   3 /   4
            Reading Buffer   4 /   4
            Found Buffers: 4 Messages: 2, sorting entries
            [0]0AB4.0AF4::  131804496926295220 [Microsoft-Windows-Shell-NotificationCenter/ActionCenterButtonStateOnLaunching/]{"messageState": 0, "notificationState": 1}
            Total of 2 Messages from 4 Buffers
        """
        line_with_event_json_format = ""
        index = 0
        index_of_found_buffers = -1
        for line in event_json_format_data.split("\n"):
            if EJF_FOUND_BUFFERS in line.lower():
                index_of_found_buffers = index 
                break
            elif EJF_NO_BUFFERS_FOUND in line.lower():
                self.sender = "<NO_DATA_FOUND>"
                self.event_json = "<NO_DATA_FOUND>"
                return 
            else:
                index += 1
        if index_of_found_buffers == -1:
            raise ErrorWhenParsing("\" Found buffers\" wasn't found in the Json event format provided: {}".format(event_json_format_data))
        line_with_event_json_format = event_json_format_data.split("\n")[index_of_found_buffers+1]
        
        self._parse_line_with_event_json_format(line_with_event_json_format)

    def __str__(self):
        output = ""
        for key, value in self.__dict__.items():
            output += "{}: {}\n".format(key,value)
        return output

    