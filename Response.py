class Response:
    def __init__(self, list_of_words, single_response=False, required_words=[], db = False):
        self.list_of_words = list_of_words
        self.single_response = single_response
        self.required_words = required_words
        self.db = db