import graphene
from webapi.queries.document import Document
from extraction.db.db_handler import MongoHandler


class Query(graphene.ObjectType):
    document = graphene.Field(Document,  docid=graphene.Int(required=True))

    def resolve_document(parent, info, docid):
        mh = MongoHandler()
        raw_doc = mh.read_doc(docid)
        doc = Document(**raw_doc)
        # TODO: avoid this step when button confirmed implemented
        # Currently just checking if the documen has been opened.
        # Can be opened but not modified so is just processed.
        # If a model is involver the the document is processed too.
        if raw_doc.get('status') == 'loaded':
            mh.update_status(docid, status='processed')
        mh.close_conn()
        return doc

    documents = graphene.List(Document)

    def resolve_documents(parent, info):
        mh = MongoHandler()
        doclist = mh.get_doc_list()
        documents = [Document(**vals) for vals in doclist]
        mh.close_conn()
        return documents
