from collections import namedtuple
from misc.constants import (ALL_EVENTS_WRITTEN_TITLE, EVENT_CHANNEL, EVENT_TYPE,
                       EVENT_VERSION, EVENT_LEVEL, EVENT_OPCODE, EVENT_TASK,
                       EVENT_KEYWORD, EVENT_DATE, EVENT_SENDER, EVENT_MSG,
                       EVENT_ID)
from core.renderedFormat import RenderedFormat
from statistics.statistic import Statistic

EventInfo = namedtuple("EventInfo",["descriptor","date","sender","msg"])


class AllEventsWrittenStatistic(Statistic):
    def __init__(self):
        self.events_info = []

    def build_statistic(self, writes_info, **kwargs):
        """
            This statistic will show the amount of times the callstack
            was used, by who and also will provide an identifier.
        """
        for write_info in writes_info:
            event_descriptor = write_info.get_event_descriptor()
            event_date = str(write_info.get_date())
            event_sender = write_info.get_event_json_format().get_sender()
            event_msg = write_info.get_event_json_format().get_event_json()
            event_info = EventInfo(event_descriptor, event_date, event_sender, event_msg)
            self.events_info.append(event_info)

    def get_rendered_format(self):
        """
            This function return a rendered format object with the data
            related to the statistic fullfilled.
        """
        title = ALL_EVENTS_WRITTEN_TITLE
        columns = [EVENT_ID, EVENT_VERSION, EVENT_CHANNEL, EVENT_LEVEL, EVENT_OPCODE, EVENT_TASK, 
                    EVENT_KEYWORD, EVENT_DATE, EVENT_SENDER, EVENT_MSG]
        rows = []
        for event_info in self.events_info:
            _id =  hex(event_info.descriptor.get_id())
            version =  hex(event_info.descriptor.get_version())
            channel =  hex(event_info.descriptor.get_channel())
            level =  hex(event_info.descriptor.get_level())
            opcode =  hex(event_info.descriptor.get_opcode())
            task = hex(event_info.descriptor.get_task())
            keyword =  hex(event_info.descriptor.get_keyword())
            date = event_info.date
            sender = event_info.sender
            msg = event_info.msg

            row = [_id, version, channel, level, opcode, task, keyword, date, sender, msg]
            rows.append(row)
        return RenderedFormat(title, columns, rows)