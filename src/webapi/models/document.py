import graphene


class Sentence(graphene.ObjectType):
    start = graphene.Int()
    end = graphene.Int()
    startchar = graphene.Int()
    endchar = graphene.Int()


class Annot(graphene.ObjectType):
    tagid = graphene.Int()
    label = graphene.String()
    label_id = graphene.Int()
    start = graphene.Int()
    end = graphene.Int()
    confidence = graphene.Float()
    annotatedby = graphene.String()


class InputAnnot(graphene.InputObjectType):
    tagid = graphene.Int()
    label = graphene.String()
    label_id = graphene.Int()
    start = graphene.Int()
    end = graphene.Int()
    confidence = graphene.Float()
    annotatedby = graphene.String()
