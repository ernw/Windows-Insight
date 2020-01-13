class RenderedFormat:
    def __init__(self, title, columns, rows):
        self.title = title
        self.columns = columns
        self.rows = rows

    def get_title(self):
        return self.title

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows
