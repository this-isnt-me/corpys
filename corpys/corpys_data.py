import uuid


class CorpysData:
    def __init__(self, input_text):
        self.text = input_text
        self.sent_id = str(uuid.uuid4())
