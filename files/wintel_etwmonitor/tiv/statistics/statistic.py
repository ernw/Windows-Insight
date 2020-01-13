class Statistic(object):

    def __init__(self):
        pass

    def build_statistic(self, **kwrags):
        """
            This function will have to prepare all the data that the statistic
            will need/use. Usually, prepares internal structures.
            Doesn't returns anything.
        """
        raise NotImplementedError
    
    def get_rendered_format(self):
        """
            This function returns a rendered format object (RenderFormat class)
            with the corresponding data fulfilled with the statistic internal structures.
        """
        raise NotImplementedError

