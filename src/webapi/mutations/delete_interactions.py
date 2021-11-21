import graphene
from extraction.db.db_handler import MongoHandler


class DeleteInteractions(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        docid = graphene.Int(required=True)

    docid = graphene.Int()
    status = graphene.String()

    def mutate(root, info, **input):
        docid = input.get('docid')
        mh = MongoHandler()

        mh.delete_interactions(
            docid=docid
        )
        doc = mh.read_doc(docid=docid)
        status = doc.get('status')
        mh.close_conn()
        return DeleteInteractions(docid=docid, status=status)
