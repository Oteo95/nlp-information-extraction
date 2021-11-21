import pandas as pd
import spacy


class PreprocessDocs:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def get_docs(self, raw_docs: pd.DataFrame) -> list:
        """
            Function to obtain the documents from the original csv

        Parameters:
            raw_docs : pd.DataFrame
                Object with, at least, id, title and text of the
                documents.

        Returns:
            List
                list of dicts with id, title, text and title+text
        """
        docs = []
        for _, row in raw_docs.iterrows():
            doc = {
                "id": row.ID,
                "title": row.Title,
                "text": row.Text,
                "full_text":  row.Title + '.\n' + row.Text,
                "creation": row.OriginalTimeUTC,
            }
            docs.append(doc)
        return docs

    def spacy_docs(self, texts: list) -> list:
        """Get a spacy object from raw text

        Parameters:
            texts : list
                List of dicts with the documents information

        Returns:
            List
                List of spacy objects
        """
        docs_gen = self.nlp.pipe(
            (text["text"] for text in texts),
            disable=['ner']
        )
        docs = list(docs_gen)
        return docs

    def get_mongo_documents(self, raw_docs):
        rdocs = self.get_docs(raw_docs)
        docs = self.spacy_docs(rdocs)

        doc_sents = []
        for idoc, text in zip(docs, rdocs):
            sent_dict = self.get_sents(idoc)
            item = {
                'docid': text["id"],
                'creation': pd.to_datetime(text["creation"]),
                'title': text["title"],
                'text': text["text"],
                'sents': sent_dict,
                'annotations': [],
                'userannotations': [],
                'status': 'loaded',
            }
            doc_sents.append(item)
        return doc_sents

    def get_tokens(self, spacy_doc) -> list:
        sentence_tokens = []
        for sent in spacy_doc.sents:
            words = self.nlp(sent.text)
            sentence = []
            for word in words:
                sentence.append(word)
            sentence_tokens.append(sentence)
        return sentence_tokens

    @staticmethod
    def get_sents(spacy_doc) -> list:
        """
        """
        sents = []
        for _, sent in enumerate(spacy_doc.sents):
            to_label = 1
            sents.append({
                'start': sent.start,
                'end': sent.end,
                'startchar': sent.start_char,
                'endchar': sent.end_char,
                'tolabel': to_label,
            })
        return sents
