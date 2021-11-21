import graphene
from extraction.db.db_handler import MongoHandler
from webapi.models import document


class UpdateAnnotations(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        docid = graphene.Int(required=True)
        userannotations = graphene.List(document.InputAnnot)
    docid = graphene.String()

    def mutate(root, info, **input):
        doc_id = input.get('docid')
        new_anot = input.get('userannotations')
        mh = MongoHandler()
        mh.update_annotations(docid=doc_id, annots=new_anot, modfrom="user")
        mh.close_conn()
        return UpdateAnnotations(docid=doc_id)
