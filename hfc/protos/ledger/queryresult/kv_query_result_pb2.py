# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/ledger/queryresult/kv_query_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/ledger/queryresult/kv_query_result.proto',
  package='queryresult',
  syntax='proto3',
  serialized_pb=_b('\n3hfc/protos/ledger/queryresult/kv_query_result.proto\x12\x0bqueryresult\x1a\x1fgoogle/protobuf/timestamp.proto\"3\n\x02KV\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x0c\"q\n\x0fKeyModification\x12\r\n\x05tx_id\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tis_delete\x18\x04 \x01(\x08\x42k\n0org.hyperledger.fabric.protos.ledger.queryresultZ7github.com/hyperledger/fabric/protos/ledger/queryresultb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_KV = _descriptor.Descriptor(
  name='KV',
  full_name='queryresult.KV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='queryresult.KV.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='queryresult.KV.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='queryresult.KV.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=152,
)


_KEYMODIFICATION = _descriptor.Descriptor(
  name='KeyModification',
  full_name='queryresult.KeyModification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='queryresult.KeyModification.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='queryresult.KeyModification.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='queryresult.KeyModification.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_delete', full_name='queryresult.KeyModification.is_delete', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=267,
)

_KEYMODIFICATION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['KV'] = _KV
DESCRIPTOR.message_types_by_name['KeyModification'] = _KEYMODIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KV = _reflection.GeneratedProtocolMessageType('KV', (_message.Message,), dict(
  DESCRIPTOR = _KV,
  __module__ = 'hfc.protos.ledger.queryresult.kv_query_result_pb2'
  # @@protoc_insertion_point(class_scope:queryresult.KV)
  ))
_sym_db.RegisterMessage(KV)

KeyModification = _reflection.GeneratedProtocolMessageType('KeyModification', (_message.Message,), dict(
  DESCRIPTOR = _KEYMODIFICATION,
  __module__ = 'hfc.protos.ledger.queryresult.kv_query_result_pb2'
  # @@protoc_insertion_point(class_scope:queryresult.KeyModification)
  ))
_sym_db.RegisterMessage(KeyModification)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n0org.hyperledger.fabric.protos.ledger.queryresultZ7github.com/hyperledger/fabric/protos/ledger/queryresult'))
# @@protoc_insertion_point(module_scope)
