# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meterusage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="meterusage.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x10meterusage.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\'\n\x11MeterUsageRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t"\x98\x01\n\x0fMeterUsageReply\x12\x34\n\nmeterusage\x18\x01 \x03(\x0b\x32 .MeterUsageReply.MeterUsageEntry\x1aO\n\x0fMeterUsageEntry\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nmeterusage\x18\x02 \x01(\x02\x32K\n\rGetMeterUsage\x12:\n\x10ReturnMeterUsage\x12\x12.MeterUsageRequest\x1a\x10.MeterUsageReply"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_METERUSAGEREQUEST = _descriptor.Descriptor(
    name="MeterUsageRequest",
    full_name="MeterUsageRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="identifier",
            full_name="MeterUsageRequest.identifier",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=53,
    serialized_end=92,
)


_METERUSAGEREPLY_METERUSAGEENTRY = _descriptor.Descriptor(
    name="MeterUsageEntry",
    full_name="MeterUsageReply.MeterUsageEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time",
            full_name="MeterUsageReply.MeterUsageEntry.time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="meterusage",
            full_name="MeterUsageReply.MeterUsageEntry.meterusage",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=168,
    serialized_end=247,
)

_METERUSAGEREPLY = _descriptor.Descriptor(
    name="MeterUsageReply",
    full_name="MeterUsageReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="meterusage",
            full_name="MeterUsageReply.meterusage",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _METERUSAGEREPLY_METERUSAGEENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=95,
    serialized_end=247,
)

_METERUSAGEREPLY_METERUSAGEENTRY.fields_by_name[
    "time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METERUSAGEREPLY_METERUSAGEENTRY.containing_type = _METERUSAGEREPLY
_METERUSAGEREPLY.fields_by_name[
    "meterusage"
].message_type = _METERUSAGEREPLY_METERUSAGEENTRY
DESCRIPTOR.message_types_by_name["MeterUsageRequest"] = _METERUSAGEREQUEST
DESCRIPTOR.message_types_by_name["MeterUsageReply"] = _METERUSAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeterUsageRequest = _reflection.GeneratedProtocolMessageType(
    "MeterUsageRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _METERUSAGEREQUEST,
        "__module__": "meterusage_pb2"
        # @@protoc_insertion_point(class_scope:MeterUsageRequest)
    },
)
_sym_db.RegisterMessage(MeterUsageRequest)

MeterUsageReply = _reflection.GeneratedProtocolMessageType(
    "MeterUsageReply",
    (_message.Message,),
    {
        "MeterUsageEntry": _reflection.GeneratedProtocolMessageType(
            "MeterUsageEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _METERUSAGEREPLY_METERUSAGEENTRY,
                "__module__": "meterusage_pb2"
                # @@protoc_insertion_point(class_scope:MeterUsageReply.MeterUsageEntry)
            },
        ),
        "DESCRIPTOR": _METERUSAGEREPLY,
        "__module__": "meterusage_pb2"
        # @@protoc_insertion_point(class_scope:MeterUsageReply)
    },
)
_sym_db.RegisterMessage(MeterUsageReply)
_sym_db.RegisterMessage(MeterUsageReply.MeterUsageEntry)


_GETMETERUSAGE = _descriptor.ServiceDescriptor(
    name="GetMeterUsage",
    full_name="GetMeterUsage",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=249,
    serialized_end=324,
    methods=[
        _descriptor.MethodDescriptor(
            name="ReturnMeterUsage",
            full_name="GetMeterUsage.ReturnMeterUsage",
            index=0,
            containing_service=None,
            input_type=_METERUSAGEREQUEST,
            output_type=_METERUSAGEREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_GETMETERUSAGE)

DESCRIPTOR.services_by_name["GetMeterUsage"] = _GETMETERUSAGE

# @@protoc_insertion_point(module_scope)
