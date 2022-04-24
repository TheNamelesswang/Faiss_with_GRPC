# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_pb2 as data__pb2


class FaissServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/faissrpc_service.FaissService/add',
                request_serializer=data__pb2.Message_add.SerializeToString,
                response_deserializer=data__pb2.Message_tag.FromString,
                )
        self.remove_index = channel.unary_unary(
                '/faissrpc_service.FaissService/remove_index',
                request_serializer=data__pb2.Message_int.SerializeToString,
                response_deserializer=data__pb2.Message_tag.FromString,
                )
        self.remove_memory = channel.unary_unary(
                '/faissrpc_service.FaissService/remove_memory',
                request_serializer=data__pb2.Message_int.SerializeToString,
                response_deserializer=data__pb2.Message_tag.FromString,
                )
        self.get_size = channel.unary_unary(
                '/faissrpc_service.FaissService/get_size',
                request_serializer=data__pb2.Message_None.SerializeToString,
                response_deserializer=data__pb2.Message_int.FromString,
                )
        self.recall_by_ids = channel.unary_unary(
                '/faissrpc_service.FaissService/recall_by_ids',
                request_serializer=data__pb2.Message_recall.SerializeToString,
                response_deserializer=data__pb2.Message_json.FromString,
                )
        self.cal_by_ids = channel.unary_unary(
                '/faissrpc_service.FaissService/cal_by_ids',
                request_serializer=data__pb2.Message_cal.SerializeToString,
                response_deserializer=data__pb2.Message_json.FromString,
                )
        self.write = channel.unary_unary(
                '/faissrpc_service.FaissService/write',
                request_serializer=data__pb2.Message_None.SerializeToString,
                response_deserializer=data__pb2.Message_tag.FromString,
                )


class FaissServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_memory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_size(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recall_by_ids(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cal_by_ids(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaissServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=data__pb2.Message_add.FromString,
                    response_serializer=data__pb2.Message_tag.SerializeToString,
            ),
            'remove_index': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_index,
                    request_deserializer=data__pb2.Message_int.FromString,
                    response_serializer=data__pb2.Message_tag.SerializeToString,
            ),
            'remove_memory': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_memory,
                    request_deserializer=data__pb2.Message_int.FromString,
                    response_serializer=data__pb2.Message_tag.SerializeToString,
            ),
            'get_size': grpc.unary_unary_rpc_method_handler(
                    servicer.get_size,
                    request_deserializer=data__pb2.Message_None.FromString,
                    response_serializer=data__pb2.Message_int.SerializeToString,
            ),
            'recall_by_ids': grpc.unary_unary_rpc_method_handler(
                    servicer.recall_by_ids,
                    request_deserializer=data__pb2.Message_recall.FromString,
                    response_serializer=data__pb2.Message_json.SerializeToString,
            ),
            'cal_by_ids': grpc.unary_unary_rpc_method_handler(
                    servicer.cal_by_ids,
                    request_deserializer=data__pb2.Message_cal.FromString,
                    response_serializer=data__pb2.Message_json.SerializeToString,
            ),
            'write': grpc.unary_unary_rpc_method_handler(
                    servicer.write,
                    request_deserializer=data__pb2.Message_None.FromString,
                    response_serializer=data__pb2.Message_tag.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'faissrpc_service.FaissService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FaissService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/add',
            data__pb2.Message_add.SerializeToString,
            data__pb2.Message_tag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/remove_index',
            data__pb2.Message_int.SerializeToString,
            data__pb2.Message_tag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_memory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/remove_memory',
            data__pb2.Message_int.SerializeToString,
            data__pb2.Message_tag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_size(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/get_size',
            data__pb2.Message_None.SerializeToString,
            data__pb2.Message_int.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recall_by_ids(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/recall_by_ids',
            data__pb2.Message_recall.SerializeToString,
            data__pb2.Message_json.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cal_by_ids(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/cal_by_ids',
            data__pb2.Message_cal.SerializeToString,
            data__pb2.Message_json.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/faissrpc_service.FaissService/write',
            data__pb2.Message_None.SerializeToString,
            data__pb2.Message_tag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
