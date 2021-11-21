import graphene
from webapi.queries.query import Query
from webapi.mutations.mutation import Mutation


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
