from core.renderedFormat import RenderedFormat
from misc.constants import (SERVICE_NAME, SERVICE_TAG)
from statistics.statistic import Statistic

class ServicesDBStatistic(Statistic):

    def build_statistic(self, services_db, **kwargs):
        self.services_db = services_db

    def get_rendered_format(self):
        title = "Services DB"      
        columns =  [SERVICE_TAG, SERVICE_NAME] 
        services_in_ordered_list = self.services_db.dump_as_list()
        rows = [ [hex(elem[0]), elem[1]] for elem in  services_in_ordered_list]
        return RenderedFormat(title, columns, rows)
