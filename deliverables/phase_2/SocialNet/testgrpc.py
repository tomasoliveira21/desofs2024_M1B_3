#!/usr/bin/env python
import grpc

from socialNet_backend_protobuf import common_pb2, socialNet_backend_pb2_grpc


channel = grpc.insecure_channel('localhost:51051')
stub = socialNet_backend_pb2_grpc.socialnetServiceStub(channel)


request = common_pb2.IdRequest(id=1)

response = stub.GetFoo(request)

print(response)
