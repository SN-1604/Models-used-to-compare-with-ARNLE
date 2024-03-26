# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parsimony.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='parsimony.proto',
  package='Parsimony',
  syntax='proto3',
  serialized_pb=_b('\n\x0fparsimony.proto\x12\tParsimony\"^\n\x03mut\x12\x10\n\x08position\x18\x01 \x01(\x05\x12\x0f\n\x07ref_nuc\x18\x02 \x01(\x05\x12\x0f\n\x07par_nuc\x18\x03 \x01(\x05\x12\x0f\n\x07mut_nuc\x18\x04 \x03(\x05\x12\x12\n\nchromosome\x18\x05 \x01(\t\"1\n\rmutation_list\x12 \n\x08mutation\x18\x01 \x03(\x0b\x32\x0e.Parsimony.mut\"=\n\x0e\x63ondensed_node\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x18\n\x10\x63ondensed_leaves\x18\x02 \x03(\t\"\x1e\n\rnode_metadata\x12\r\n\x05\x63lade\x18\x01 \x01(\t\"\xa8\x01\n\x04\x64\x61ta\x12\x0e\n\x06newick\x18\x01 \x01(\t\x12\x30\n\x0enode_mutations\x18\x02 \x03(\x0b\x32\x18.Parsimony.mutation_list\x12\x32\n\x0f\x63ondensed_nodes\x18\x03 \x03(\x0b\x32\x19.Parsimony.condensed_node\x12*\n\x08metadata\x18\x04 \x03(\x0b\x32\x18.Parsimony.node_metadatab\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MUT = _descriptor.Descriptor(
  name='mut',
  full_name='Parsimony.mut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='Parsimony.mut.position', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref_nuc', full_name='Parsimony.mut.ref_nuc', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='par_nuc', full_name='Parsimony.mut.par_nuc', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mut_nuc', full_name='Parsimony.mut.mut_nuc', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chromosome', full_name='Parsimony.mut.chromosome', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=30,
  serialized_end=124,
)


_MUTATION_LIST = _descriptor.Descriptor(
  name='mutation_list',
  full_name='Parsimony.mutation_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutation', full_name='Parsimony.mutation_list.mutation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=126,
  serialized_end=175,
)


_CONDENSED_NODE = _descriptor.Descriptor(
  name='condensed_node',
  full_name='Parsimony.condensed_node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='Parsimony.condensed_node.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condensed_leaves', full_name='Parsimony.condensed_node.condensed_leaves', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=177,
  serialized_end=238,
)


_NODE_METADATA = _descriptor.Descriptor(
  name='node_metadata',
  full_name='Parsimony.node_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clade', full_name='Parsimony.node_metadata.clade', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=240,
  serialized_end=270,
)


_DATA = _descriptor.Descriptor(
  name='data',
  full_name='Parsimony.data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newick', full_name='Parsimony.data.newick', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_mutations', full_name='Parsimony.data.node_mutations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condensed_nodes', full_name='Parsimony.data.condensed_nodes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Parsimony.data.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=273,
  serialized_end=441,
)

_MUTATION_LIST.fields_by_name['mutation'].message_type = _MUT
_DATA.fields_by_name['node_mutations'].message_type = _MUTATION_LIST
_DATA.fields_by_name['condensed_nodes'].message_type = _CONDENSED_NODE
_DATA.fields_by_name['metadata'].message_type = _NODE_METADATA
DESCRIPTOR.message_types_by_name['mut'] = _MUT
DESCRIPTOR.message_types_by_name['mutation_list'] = _MUTATION_LIST
DESCRIPTOR.message_types_by_name['condensed_node'] = _CONDENSED_NODE
DESCRIPTOR.message_types_by_name['node_metadata'] = _NODE_METADATA
DESCRIPTOR.message_types_by_name['data'] = _DATA

mut = _reflection.GeneratedProtocolMessageType('mut', (_message.Message,), dict(
  DESCRIPTOR = _MUT,
  __module__ = 'parsimony_pb2'
  # @@protoc_insertion_point(class_scope:Parsimony.mut)
  ))
_sym_db.RegisterMessage(mut)

mutation_list = _reflection.GeneratedProtocolMessageType('mutation_list', (_message.Message,), dict(
  DESCRIPTOR = _MUTATION_LIST,
  __module__ = 'parsimony_pb2'
  # @@protoc_insertion_point(class_scope:Parsimony.mutation_list)
  ))
_sym_db.RegisterMessage(mutation_list)

condensed_node = _reflection.GeneratedProtocolMessageType('condensed_node', (_message.Message,), dict(
  DESCRIPTOR = _CONDENSED_NODE,
  __module__ = 'parsimony_pb2'
  # @@protoc_insertion_point(class_scope:Parsimony.condensed_node)
  ))
_sym_db.RegisterMessage(condensed_node)

node_metadata = _reflection.GeneratedProtocolMessageType('node_metadata', (_message.Message,), dict(
  DESCRIPTOR = _NODE_METADATA,
  __module__ = 'parsimony_pb2'
  # @@protoc_insertion_point(class_scope:Parsimony.node_metadata)
  ))
_sym_db.RegisterMessage(node_metadata)

data = _reflection.GeneratedProtocolMessageType('data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'parsimony_pb2'
  # @@protoc_insertion_point(class_scope:Parsimony.data)
  ))
_sym_db.RegisterMessage(data)


# @@protoc_insertion_point(module_scope)