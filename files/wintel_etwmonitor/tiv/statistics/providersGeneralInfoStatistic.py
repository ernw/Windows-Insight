from collections import namedtuple
from misc.constants import (KERNEL_IMAGE, PROVIDER_GENERAL_INFO_TITLE, COUNT, PROVIDER_GUID,
                        AMOUNT_OF_WRITES, AMOUNT_OF_USER_WRITES, AMOUNT_OF_KERNEL_WRITES)
from core.renderedFormat import RenderedFormat
from statistics.statistic import Statistic

ProviderGeneralInfo = namedtuple("ProviderGeneralInfo",["total_amount","user_writes","kernel_writes"])

class ProvidersGeneralInfoStatistic(Statistic):
    
    def __init__(self):
        self.providers_gen_info = {}
    
    def _is_kernel_write(self, write_info):
        return write_info.get_process_info().get_process_name().lower() == KERNEL_IMAGE

    def build_statistic(self, writes_info, **kwargs):
        """ 
            This statistic will display the amount of writes
            for each provider plus the type (user or kernel)
        """
        for write_info in writes_info:
            guid = write_info.get_provider_guid().get_guid()
            prov_gen_info = None
            if guid in self.providers_gen_info.keys():
                prov_gen_info = self.providers_gen_info[guid]
            else:
                prov_gen_info = ProviderGeneralInfo(0,0,0)
            
            total, user, kernel = prov_gen_info.total_amount, prov_gen_info.user_writes, prov_gen_info.kernel_writes
            total +=1
            if self._is_kernel_write(write_info):
                kernel += 1 
            else:
                user += 1
            prov_gen_info = ProviderGeneralInfo(total, user, kernel)
            self.providers_gen_info.update({guid:prov_gen_info})

    def get_rendered_format(self):
        """
            This function return a rendered format object with the data
            related to the statistic fullfilled.
        """
        title = PROVIDER_GENERAL_INFO_TITLE
        columns = [COUNT, PROVIDER_GUID, AMOUNT_OF_WRITES, AMOUNT_OF_USER_WRITES, AMOUNT_OF_KERNEL_WRITES]
        rows = []
        count = 1 
        for guid, pgi in self.providers_gen_info.items():
            row = [count, guid, pgi.total_amount, pgi.user_writes, pgi.kernel_writes ]
            rows.append(row)
            count +=1
        
        return RenderedFormat(title, columns, rows)


        
