from easydict import EasyDict
from graphql_server.flask import GraphQLView as GraphQLView

from socialNet_backend.api.graphql.schema import schema
from socialNet_backend.lib.web.user import get_current_user


def get_context():
    user = get_current_user()
    return EasyDict(
        user=user
    )


def create_graphql_view():
    view = GraphQLView.as_view(
        'graphql',
        schema=schema.graphql_schema,
        graphiql=True,
        get_context=get_context,
    )
    return view
