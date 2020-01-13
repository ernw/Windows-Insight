from collections import namedtuple
from misc.constants import (CALL_STACK_INFO_TITLE, AMOUNT_OF_TIMES_USED,
                       PROVIDERS_THAT_USED_IT,ID, COUNT,CALL_STACK_COLUMN)
from core.renderedFormat import RenderedFormat
from statistics.statistic import Statistic

CallStackInfo = namedtuple("CallStackInfo",["times_used", "providers_used_it", "id"])

class CallStacksInfoStatistic(Statistic): 
    def __init__(self):
        self.callStacksInfo = {}

    def build_statistic(self, writes_info, **kwargs):
        """
            This statistic will show the amount of times the callstack
            was used, by who and also will provide an identifier.
        """
        for write_info in writes_info:
            prov_guid = write_info.get_provider_guid().get_guid()
            call_stack = write_info.get_call_stack().get_call_stack_as_string()
            call_stack_info = None
            if call_stack in self.callStacksInfo.keys():
                call_stack_info = self.callStacksInfo[call_stack]
            else:
                call_stack_info = CallStackInfo(0,set(),-1)

            new_times_used = call_stack_info.times_used + 1
            new_providers = call_stack_info.providers_used_it.copy()
            new_providers.add(prov_guid)
            new_id = call_stack_info.id if call_stack_info.id != -1 else len(self.callStacksInfo.keys())

            new_call_stack_info = CallStackInfo(new_times_used, new_providers, new_id)
            self.callStacksInfo.update({call_stack: new_call_stack_info })   

    def get_rendered_format(self):
        """
            This function return a rendered format object with the data
            related to the statistic fullfilled.
        """
        title = CALL_STACK_INFO_TITLE
        columns = [COUNT, CALL_STACK_COLUMN, AMOUNT_OF_TIMES_USED, PROVIDERS_THAT_USED_IT, ID ]
        count = 1
        rows = []
        for call_stack, call_stack_info in self.callStacksInfo.items():
            row = [count, call_stack, call_stack_info.times_used,
                   "".join(call_stack_info.providers_used_it), call_stack_info.id] 
            rows.append(row)
            count +=1
        return RenderedFormat(title, columns, rows)
