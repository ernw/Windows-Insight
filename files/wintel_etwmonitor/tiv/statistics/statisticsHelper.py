from statistics.providersGeneralInfoStatistic import ProvidersGeneralInfoStatistic
from statistics.callStacksInfoStatistic import CallStacksInfoStatistic
from statistics.eventsIdPerProviderStatistic import EventsIDPerProviderStatistic
from statistics.allEventsWrittenStatistic import AllEventsWrittenStatistic
from statistics.servicesDBStatistic import ServicesDBStatistic
from statistics.statistic import Statistic

class StatisticsHelper:
    def __init__(self, writes_info, services_db):
        self.writes_info = writes_info
        self.services_db = services_db
        self.statistics = Statistic.__subclasses__()
        self.built_statistics = []

    def build_statistics(self):
        for statistic in self.statistics:
            st = statistic()
            params = {"writes_info": self.writes_info, "services_db": self.services_db}
            st.build_statistic(**params)
            self.built_statistics.append(st)
    
    def get_all_rendered_formats(self):
        rendered_formats = []
        for built_statistic in self.built_statistics:
            rendered_formats.append(built_statistic.get_rendered_format())
        return rendered_formats

    
