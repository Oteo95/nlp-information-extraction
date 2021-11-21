import graphene

from webapi.mutations.delete_interactions import DeleteInteractions
from webapi.mutations.update_annotations import UpdateAnnotations


class Mutation(graphene.ObjectType):
    delete_interactions = DeleteInteractions.Field()
    update_annotations = UpdateAnnotations.Field()
