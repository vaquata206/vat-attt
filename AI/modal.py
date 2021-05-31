from pyvi import ViTokenizer, ViPosTagger
import types
import re
import AI.navieBayes.multinomialNavieBayes as mnb


def predict(text: str, modal_code: str):
    modal = None
    if modal_code == "mnb":
        modal = mnb.predict
    if isinstance(modal, types.FunctionType):
        t = TextProcessing([text])
        cls, prd = modal(t[0])
        return {"cls": cls, "percent": prd[cls]/sum(prd)}
    else:
        return ""


def TextProcessing(texts):
    # Xử lý dữ liệu đầu vào
    documents = []
    for sen in range(0, len(texts)):
        document = str(texts[sen])

        # Remove all the special characters
        document = re.sub(r'\W', ' ', document)

        # remove all single characters
        # document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        # document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b' ?
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        document = ViTokenizer.tokenize(document)

        # Lemmatization
        document = document.split()

        # todo so sánh stopword...
        document = ' '.join(document)

        documents.append(document)
    return documents


def load_modals():
    mnb.load_modal()
