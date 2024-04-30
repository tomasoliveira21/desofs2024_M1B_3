from socialNet_backend_protobuf import socialNet_backend_pb2_grpc, common_pb2
from socialNet_backend.api.grpc import serializers
from socialNet_backend.api.grpc.request import handle_grpc_errors
from socialNet_backend.lib import get_logger


from socialnet.lib.dates import utcnow


logger = get_logger(__name__)


class Foo:
    pass


class socialnetServiceServicer(socialNet_backend_pb2_grpc.socialnetServiceServicer):

    @handle_grpc_errors()
    def GetFoo(self, request, context):
        foo = Foo()
        foo.id = request.id
        foo.created_at = utcnow()
        foo.name = 'Foo'

        return serializers.serialize_foo(foo)

    @handle_grpc_errors()
    def Ping(self, request, context):
        return common_pb2.SimpleResponse(success=True)
