from datetime import datetime
from misc.constants import DATE_FORMAT
class Date:
    def __init__(self):
        self.date = None

    def get_date(self):
        return self.date
    
    def parse(self, date_data):
        """
            Debugger (not debuggee) time: Mon Jun  4 11:29:31.215 2018 (UTC + 2:00)
        """     
        # Get the value of the line
        date_line = date_data
        # Remove prefix of date
        date_line = ":".join((date_line.split(":")[1:])).rstrip()
        # Remove the timezone part
        date_line = date_line[:date_line.index('(')].strip()
        self.date = datetime.strptime(date_line, DATE_FORMAT)

    def __str__(self):
        return self.date.strftime(DATE_FORMAT)