class Statistic:

    def __init__(self):
        pass

    def build_statistic(self, **kwrags):
        raise NotImplementedError
    
    def get_rendered_format(self):
        raise NotImplementedError

