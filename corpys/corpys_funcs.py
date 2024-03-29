from corpys.corpys_data import CorpysData
import unicodedata
import spacy
nlp = spacy.load("en_core_web_lg")


class CorpysFunc:
    def __init__(self, input_text):
        self.documents = []
        print(len(self.documents))
        text_list = self.split_text(input_text)
        for doc in text_list:
            self.documents.append(CorpysData(self.clean_text(doc)))
        print(len(self.documents))

    def clean_text(self, input_text, upper=False):
        text_string = ''.join(cat for cat in unicodedata.normalize('NFKD',
                                                                   input_text) if unicodedata.category(cat) != 'Mn')
        string_list = text_string.split()
        text_string = " ".join(string_list)
        for entry in [(",,", ","), (" ,", ","), ("  ", " ")]:
            text_string = text_string.replace(entry[0], entry[1])
        if upper:
            text_string = text_string.upper()
        return text_string

    def split_text(self, input_text):
        doc = nlp(input_text)
        return [sent.text for sent in doc.sents]

    def print_docs(self):
        for entry in self.documents:
            print(entry.sent_id)
            print(entry.text)
