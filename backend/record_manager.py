class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_last_record(self):
        if self.records:
            return self.records[-1]
        return None