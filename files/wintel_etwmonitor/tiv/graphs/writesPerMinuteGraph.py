import datetime
from collections import OrderedDict
from core.graphData import GraphData
from misc.constants import (WPM_DATE_FORMAT, WPM_NAME, WPM_TYPE, WPM_LABEL,
                       WPM_TITLE, WPM_FILENAME, JS_EXTENSION,
                       WPM_GRAPH_WITH_TIME, WPM_DISPLAY_LEGEND
                       )
from graphs.graph import Graph

class WritesPerMinuteGraph(Graph):
    def __init__(self): 
        self.writes_per_minute = OrderedDict()

    def _manually_scale(self):
        """

        """
        one_minute = datetime.timedelta(minutes=1)
        dates_to_add = []
        for date in self.writes_per_minute.keys():
            next_date = date+one_minute
            if next_date not in self.writes_per_minute.keys():
                dates_to_add.append(next_date)

        for date in dates_to_add:
            self.writes_per_minute.update({date:0})

    def _add_all_datetimes_between_bounds(self, first, last):
        """
        """
        all_btwn_datetimes = []
        one_minute = datetime.timedelta(minutes=1)
        new_datetime = first
        while (new_datetime != last):
            new_datetime = new_datetime + one_minute
            all_btwn_datetimes.append(new_datetime)
        
        for date in all_btwn_datetimes:
            if date not in self.writes_per_minute.keys():
                self.writes_per_minute.update({date:0})

    def build_graph_data(self, writes_info):
        """ 
            This function builds all the data for the graph
        """
        for write_info in writes_info:
            date = write_info.get_date().get_date()
            date_trimmed = date.replace(second=0, microsecond=0)
            if date_trimmed in self.writes_per_minute.keys():
                self.writes_per_minute[date_trimmed] +=1 
            else:
                self.writes_per_minute.update({date_trimmed:1})

    def get_graph_data(self):
        """
            Return the GraphData object related to the data of this graph
        """
        list_format = list(self.writes_per_minute.items())
        labels = [elem[0].strftime(WPM_DATE_FORMAT) for elem in list_format]
        values = [elem[1] for elem in list_format]

        return GraphData(WPM_NAME, WPM_TYPE,values, labels, WPM_LABEL, WPM_TITLE,
                         WPM_FILENAME + JS_EXTENSION, WPM_DISPLAY_LEGEND,
                         WPM_GRAPH_WITH_TIME)
        
        