from core.renderedFormat import RenderedFormat
from misc.constants import (EVENT_ID_PROVIDER_TITLE, EVENT_ID, AMOUNT_OF_EVENTS,
                        PROVIDER_GUID,  EVENT_ID_PROVIDER_TITLE)
from statistics.statistic import Statistic

class EventsIDPerProviderStatistic(Statistic):

    def __init__(self):
        self.eventIDProvidersInfo = {}

    def build_statistic(self, writes_info, **kwargs):
        """ 
            This statistic will display the amount of writes
            for each provider plus the type (user or kernel)
        """
        for write_info in writes_info:
            provider_guid = write_info.get_provider_guid().get_guid()
            event_id = write_info.get_event_descriptor().get_id()
            current_key = (provider_guid,event_id)
            if current_key in self.eventIDProvidersInfo.keys():
                self.eventIDProvidersInfo[current_key] += 1
            else:
                self.eventIDProvidersInfo.update({current_key:1})

    def get_rendered_format(self):
        """
            This function return a rendered format object with the data
            related to the statistic fullfilled.
        """
        title = EVENT_ID_PROVIDER_TITLE
        columns = [PROVIDER_GUID, EVENT_ID, AMOUNT_OF_EVENTS]
        rows = []
        for guid_event_id, amount_of_events in self.eventIDProvidersInfo.items():
            guid, event_id = guid_event_id
            row = [guid, hex(event_id), amount_of_events]
            rows.append(row)
        return RenderedFormat(title, columns, rows)





