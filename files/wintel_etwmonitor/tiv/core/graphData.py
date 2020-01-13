class GraphData:
    def __init__(self, name, _type, values, labels, label, title, filename, display_legend, with_time):
        self.name = name
        self._type = _type
        self.values = values
        self.labels = labels
        self.label = label
        self.title  = title 
        self.filename = filename
        self.id = name
        self.display_legend = display_legend
        self.with_time = with_time

    def get_name(self):
        return self.name

    def get_type(self):
        return self._type

    def get_values(self):
        return self.values

    def get_labels(self):
        return self.labels

    def get_label(self):
        return self.label

    def get_title(self):
        return self.title

    def get_filename(self):
        return self.filename

    def get_id(self):
        return self.id

    def get_display_legend(self):
        return self.display_legend

    def get_with_time(self):
        return self.with_time








