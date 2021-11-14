# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nuser.proto\"\x18\n\x06UserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\"9\n\x04user\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0blast_active\x18\x03 \x01(\t\"?\n\x0f\x42ookingUserData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0e\n\x06movies\x18\x03 \x01(\t2_\n\x04User\x12\x1f\n\x0bGetUserByID\x12\x07.UserId\x1a\x05.user\"\x00\x12\x36\n\x15GetBookedMoviesOfUser\x12\x07.UserId\x1a\x10.BookingUserData\"\x00\x30\x01\x62\x06proto3'
)




_USERID = _descriptor.Descriptor(
  name='UserId',
  full_name='UserId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='UserId.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=38,
)


_USER = _descriptor.Descriptor(
  name='user',
  full_name='user',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='user.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='user.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_active', full_name='user.last_active', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=97,
)


_BOOKINGUSERDATA = _descriptor.Descriptor(
  name='BookingUserData',
  full_name='BookingUserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='BookingUserData.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='BookingUserData.date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='BookingUserData.movies', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['UserId'] = _USERID
DESCRIPTOR.message_types_by_name['user'] = _USER
DESCRIPTOR.message_types_by_name['BookingUserData'] = _BOOKINGUSERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  })
_sym_db.RegisterMessage(UserId)

user = _reflection.GeneratedProtocolMessageType('user', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user)
  })
_sym_db.RegisterMessage(user)

BookingUserData = _reflection.GeneratedProtocolMessageType('BookingUserData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGUSERDATA,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:BookingUserData)
  })
_sym_db.RegisterMessage(BookingUserData)



_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=164,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserByID',
    full_name='User.GetUserByID',
    index=0,
    containing_service=None,
    input_type=_USERID,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookedMoviesOfUser',
    full_name='User.GetBookedMoviesOfUser',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_BOOKINGUSERDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
