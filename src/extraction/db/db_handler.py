import os
from pymongo import MongoClient


class MongoHandler:
    DB_NAME = 'InfoExtraction'
    DOCUMENTS = 'documents'

    def __init__(self):

        conn_str = os.getenv("MONGO_CONNECTION_STRING")
        # This, for development purpose
        if conn_str is None:
            conn_str = "mongodb://root:example@mongo:27017"

        self.client = MongoClient(conn_str)
        self.db = self.client[self.DB_NAME]

    def insert_documents(self, docs):
        coll = self.db[self.DOCUMENTS]
        coll.insert_many(docs)

    def delete_db(self):
        self.client.drop_database(self.DB_NAME)

    def get_doc_list(self):
        """Returns the list of documents ids and title
        """
        coll = self.db[self.DOCUMENTS]
        projection = {
            '_id': 0,
            'docid': 1,
            'creation': 1,
            'title': 1,
            'text': 1,
            'status': 1,
        }
        docs = coll.find({}, projection)
        return list(docs)

    def read_doc(self, docid: int):
        "Returns the document matching the given docid"
        coll = self.db[self.DOCUMENTS]
        doc = coll.find_one(
            {'docid': docid},
            {'_id': 0}
        )
        return doc

    def update_status(
        self,
        docid: int,
        status: str = None,
    ):
        if status is None:
            status = 'manual_processed'

        coll = self.db[self.DOCUMENTS]
        coll.update_one(
            {'docid': docid},
            {'$set': {
                'status': status
            }},
        )
        return status

    def get_all_annotations(self) -> list:
        """Return the text and annotations"""
        coll = self.db[self.DOCUMENTS]
        proj = {
            '_id': 0,
            'docid': 1,
            'text': 1,
            'annotations': 1,
            'userannotations': 1
        }
        docs = coll.find({}, proj)
        return list(docs)

    def update_annotations(
        self,
        docid: int,
        annots: list,
        modfrom: str
    ):
        """The annotation field is updated for the given docid"""
        if modfrom == 'model':
            field = 'annotations'
            status = 'processed'
        elif modfrom == 'user':
            field = 'userannotations'
            status = 'manual_processed'
        else:
            raise ValueError(f'Invalid argument {modfrom}')

        coll = self.db[self.DOCUMENTS]
        coll.update_one(
            {'docid': docid},
            {'$set': {
                field: annots,
                'status': status
            }}
        )

    def delete_interactions(self, docid):
        """Delete interactions (userannotations) and the status
        returns to 'processed'
        """
        coll = self.db[self.DOCUMENTS]
        coll.update_one(
            {'docid': docid},
            {'$set': {
                'userannotations': [],
                'status': 'processed',
            }},
        )

    def close_conn(self):
        self.client.close()

    def read_all_documents(self):
        coll = self.db[self.DOCUMENTS]
        cursor = coll.find({})
        return list(cursor)
