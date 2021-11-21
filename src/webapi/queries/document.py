import graphene
import logging

from webapi.models import document

logger = logging.getLogger(__name__)


class Document(graphene.ObjectType):
    docid = graphene.Int(required=True)
    creation = graphene.DateTime()
    title = graphene.String()
    text = graphene.String()
    status = graphene.String()
    sents = graphene.List(document.Sentence)
    annotations = graphene.List(document.Annot)
    userannotations = graphene.List(document.Annot)
