import graphene
import users.schema

class Query(
        users.schema.Query,
        graphene.ObjectType
):
    pass

'''
users.schema.UserMutation,
users.schema.CreateProfileMutation,
users.schema.CreateUserMutation,
'''
class Mutation(
        graphene.ObjectType
        ):
    pass

schema = graphene.Schema(query=Query)
