# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressValidation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61\x64\x64ressValidation.proto\"U\n\x17ValidateAddress_Request\x12\x12\n\npostalCode\x18\x01 \x01(\t\x12\x10\n\x08locality\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x64\x64ressLines\x18\x03 \x01(\t\"*\n\x18ValidateAddress_Response\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32`\n\x16ValidateAddressService\x12\x46\n\x0fValidateAddress\x12\x18.ValidateAddress_Request\x1a\x19.ValidateAddress_Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'addressValidation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VALIDATEADDRESS_REQUEST']._serialized_start=27
  _globals['_VALIDATEADDRESS_REQUEST']._serialized_end=112
  _globals['_VALIDATEADDRESS_RESPONSE']._serialized_start=114
  _globals['_VALIDATEADDRESS_RESPONSE']._serialized_end=156
  _globals['_VALIDATEADDRESSSERVICE']._serialized_start=158
  _globals['_VALIDATEADDRESSSERVICE']._serialized_end=254
# @@protoc_insertion_point(module_scope)
