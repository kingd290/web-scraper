class DataModel:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def to_dict(self):
        return {
            'field1': self.field1,
            'field2': self.field2,
            'field3': self.field3
        }
