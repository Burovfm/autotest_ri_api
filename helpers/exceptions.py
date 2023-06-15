class StatusCode4XX(Exception):
    def __init__(self, text):
        self.txt = text
