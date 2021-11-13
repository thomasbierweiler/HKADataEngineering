# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mathfunc_pb2 as mathfunc__pb2


class MathFuncStub(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.hka.students";
    option java_outer_classname = "StudentsProto";
    option objc_class_prefix = "HKAS";

    Interface exported by the server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GuessFunction = channel.unary_unary(
                '/MathFunc/GuessFunction',
                request_serializer=mathfunc__pb2.FunctionDescription.SerializeToString,
                response_deserializer=mathfunc__pb2.State.FromString,
                )
        self.Delete = channel.unary_unary(
                '/MathFunc/Delete',
                request_serializer=mathfunc__pb2.DelMsg.SerializeToString,
                response_deserializer=mathfunc__pb2.DelState.FromString,
                )


class MathFuncServicer(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.hka.students";
    option java_outer_classname = "StudentsProto";
    option objc_class_prefix = "HKAS";

    Interface exported by the server
    """

    def GuessFunction(self, request, context):
        """method accepts the name of a student and returns an instance of Student (including full information)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathFuncServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GuessFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.GuessFunction,
                    request_deserializer=mathfunc__pb2.FunctionDescription.FromString,
                    response_serializer=mathfunc__pb2.State.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=mathfunc__pb2.DelMsg.FromString,
                    response_serializer=mathfunc__pb2.DelState.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MathFunc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MathFunc(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.hka.students";
    option java_outer_classname = "StudentsProto";
    option objc_class_prefix = "HKAS";

    Interface exported by the server
    """

    @staticmethod
    def GuessFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MathFunc/GuessFunction',
            mathfunc__pb2.FunctionDescription.SerializeToString,
            mathfunc__pb2.State.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MathFunc/Delete',
            mathfunc__pb2.DelMsg.SerializeToString,
            mathfunc__pb2.DelState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)