# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dnstap.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dnstap.proto',
  package='dnstap',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x64nstap.proto\x12\x06\x64nstap\"\x94\x01\n\x06\x44nstap\x12\x10\n\x08identity\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12\r\n\x05\x65xtra\x18\x03 \x01(\x0c\x12!\n\x04type\x18\x0f \x02(\x0e\x32\x13.dnstap.Dnstap.Type\x12 \n\x07message\x18\x0e \x01(\x0b\x32\x0f.dnstap.Message\"\x13\n\x04Type\x12\x0b\n\x07MESSAGE\x10\x01\"\xa1\x02\n\x06Policy\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04rule\x18\x02 \x01(\x0c\x12%\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x15.dnstap.Policy.Action\x12#\n\x05match\x18\x04 \x01(\x0e\x32\x14.dnstap.Policy.Match\x12\r\n\x05value\x18\x05 \x01(\x0c\"J\n\x05Match\x12\t\n\x05QNAME\x10\x01\x12\r\n\tCLIENT_IP\x10\x02\x12\x0f\n\x0bRESPONSE_IP\x10\x03\x12\x0b\n\x07NS_NAME\x10\x04\x12\t\n\x05NS_IP\x10\x05\"T\n\x06\x41\x63tion\x12\x0c\n\x08NXDOMAIN\x10\x01\x12\n\n\x06NODATA\x10\x02\x12\x08\n\x04PASS\x10\x03\x12\x08\n\x04\x44ROP\x10\x04\x12\x0c\n\x08TRUNCATE\x10\x05\x12\x0e\n\nLOCAL_DATA\x10\x06\"\xcc\x05\n\x07Message\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.dnstap.Message.Type\x12+\n\rsocket_family\x18\x02 \x01(\x0e\x32\x14.dnstap.SocketFamily\x12/\n\x0fsocket_protocol\x18\x03 \x01(\x0e\x32\x16.dnstap.SocketProtocol\x12\x15\n\rquery_address\x18\x04 \x01(\x0c\x12\x18\n\x10response_address\x18\x05 \x01(\x0c\x12\x12\n\nquery_port\x18\x06 \x01(\r\x12\x15\n\rresponse_port\x18\x07 \x01(\r\x12\x16\n\x0equery_time_sec\x18\x08 \x01(\x04\x12\x17\n\x0fquery_time_nsec\x18\t \x01(\x07\x12\x15\n\rquery_message\x18\n \x01(\x0c\x12\x12\n\nquery_zone\x18\x0b \x01(\x0c\x12\x19\n\x11response_time_sec\x18\x0c \x01(\x04\x12\x1a\n\x12response_time_nsec\x18\r \x01(\x07\x12\x18\n\x10response_message\x18\x0e \x01(\x0c\x12\x1e\n\x06policy\x18\x0f \x01(\x0b\x32\x0e.dnstap.Policy\"\x95\x02\n\x04Type\x12\x0e\n\nAUTH_QUERY\x10\x01\x12\x11\n\rAUTH_RESPONSE\x10\x02\x12\x12\n\x0eRESOLVER_QUERY\x10\x03\x12\x15\n\x11RESOLVER_RESPONSE\x10\x04\x12\x10\n\x0c\x43LIENT_QUERY\x10\x05\x12\x13\n\x0f\x43LIENT_RESPONSE\x10\x06\x12\x13\n\x0f\x46ORWARDER_QUERY\x10\x07\x12\x16\n\x12\x46ORWARDER_RESPONSE\x10\x08\x12\x0e\n\nSTUB_QUERY\x10\t\x12\x11\n\rSTUB_RESPONSE\x10\n\x12\x0e\n\nTOOL_QUERY\x10\x0b\x12\x11\n\rTOOL_RESPONSE\x10\x0c\x12\x10\n\x0cUPDATE_QUERY\x10\r\x12\x13\n\x0fUPDATE_RESPONSE\x10\x0e*#\n\x0cSocketFamily\x12\x08\n\x04INET\x10\x01\x12\t\n\x05INET6\x10\x02*4\n\x0eSocketProtocol\x12\x07\n\x03UDP\x10\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03\x44OT\x10\x03\x12\x07\n\x03\x44OH\x10\x04'
)

_SOCKETFAMILY = _descriptor.EnumDescriptor(
  name='SocketFamily',
  full_name='dnstap.SocketFamily',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INET', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INET6', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1186,
  serialized_end=1221,
)
_sym_db.RegisterEnumDescriptor(_SOCKETFAMILY)

SocketFamily = enum_type_wrapper.EnumTypeWrapper(_SOCKETFAMILY)
_SOCKETPROTOCOL = _descriptor.EnumDescriptor(
  name='SocketProtocol',
  full_name='dnstap.SocketProtocol',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UDP', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOT', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOH', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1223,
  serialized_end=1275,
)
_sym_db.RegisterEnumDescriptor(_SOCKETPROTOCOL)

SocketProtocol = enum_type_wrapper.EnumTypeWrapper(_SOCKETPROTOCOL)
INET = 1
INET6 = 2
UDP = 1
TCP = 2
DOT = 3
DOH = 4


_DNSTAP_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='dnstap.Dnstap.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=173,
)
_sym_db.RegisterEnumDescriptor(_DNSTAP_TYPE)

_POLICY_MATCH = _descriptor.EnumDescriptor(
  name='Match',
  full_name='dnstap.Policy.Match',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QNAME', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_IP', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_IP', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NS_NAME', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NS_IP', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=305,
  serialized_end=379,
)
_sym_db.RegisterEnumDescriptor(_POLICY_MATCH)

_POLICY_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='dnstap.Policy.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NXDOMAIN', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NODATA', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PASS', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DROP', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRUNCATE', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCAL_DATA', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=381,
  serialized_end=465,
)
_sym_db.RegisterEnumDescriptor(_POLICY_ACTION)

_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='dnstap.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTH_QUERY', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTH_RESPONSE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOLVER_QUERY', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOLVER_RESPONSE', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_QUERY', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_RESPONSE', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORWARDER_QUERY', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORWARDER_RESPONSE', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STUB_QUERY', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STUB_RESPONSE', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOOL_QUERY', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOOL_RESPONSE', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_QUERY', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_RESPONSE', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=907,
  serialized_end=1184,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)


_DNSTAP = _descriptor.Descriptor(
  name='Dnstap',
  full_name='dnstap.Dnstap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='dnstap.Dnstap.identity', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='dnstap.Dnstap.version', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra', full_name='dnstap.Dnstap.extra', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='dnstap.Dnstap.type', index=3,
      number=15, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='dnstap.Dnstap.message', index=4,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DNSTAP_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=173,
)


_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='dnstap.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dnstap.Policy.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule', full_name='dnstap.Policy.rule', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='dnstap.Policy.action', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='match', full_name='dnstap.Policy.match', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dnstap.Policy.value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICY_MATCH,
    _POLICY_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=465,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='dnstap.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dnstap.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='socket_family', full_name='dnstap.Message.socket_family', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='socket_protocol', full_name='dnstap.Message.socket_protocol', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_address', full_name='dnstap.Message.query_address', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_address', full_name='dnstap.Message.response_address', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_port', full_name='dnstap.Message.query_port', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_port', full_name='dnstap.Message.response_port', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_time_sec', full_name='dnstap.Message.query_time_sec', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_time_nsec', full_name='dnstap.Message.query_time_nsec', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_message', full_name='dnstap.Message.query_message', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_zone', full_name='dnstap.Message.query_zone', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_time_sec', full_name='dnstap.Message.response_time_sec', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_time_nsec', full_name='dnstap.Message.response_time_nsec', index=12,
      number=13, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_message', full_name='dnstap.Message.response_message', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy', full_name='dnstap.Message.policy', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=1184,
)

_DNSTAP.fields_by_name['type'].enum_type = _DNSTAP_TYPE
_DNSTAP.fields_by_name['message'].message_type = _MESSAGE
_DNSTAP_TYPE.containing_type = _DNSTAP
_POLICY.fields_by_name['action'].enum_type = _POLICY_ACTION
_POLICY.fields_by_name['match'].enum_type = _POLICY_MATCH
_POLICY_MATCH.containing_type = _POLICY
_POLICY_ACTION.containing_type = _POLICY
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['socket_family'].enum_type = _SOCKETFAMILY
_MESSAGE.fields_by_name['socket_protocol'].enum_type = _SOCKETPROTOCOL
_MESSAGE.fields_by_name['policy'].message_type = _POLICY
_MESSAGE_TYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Dnstap'] = _DNSTAP
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['SocketFamily'] = _SOCKETFAMILY
DESCRIPTOR.enum_types_by_name['SocketProtocol'] = _SOCKETPROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dnstap = _reflection.GeneratedProtocolMessageType('Dnstap', (_message.Message,), {
  'DESCRIPTOR' : _DNSTAP,
  '__module__' : 'dnstap_pb2'
  # @@protoc_insertion_point(class_scope:dnstap.Dnstap)
  })
_sym_db.RegisterMessage(Dnstap)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'dnstap_pb2'
  # @@protoc_insertion_point(class_scope:dnstap.Policy)
  })
_sym_db.RegisterMessage(Policy)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'dnstap_pb2'
  # @@protoc_insertion_point(class_scope:dnstap.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
