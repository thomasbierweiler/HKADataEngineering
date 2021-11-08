# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\024io.grpc.hka.studentsB\rStudentsProtoP\001\242\002\004HKAS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstudent.proto\"*\n\x04Name\x12\x0f\n\x07surname\x18\x01 \x01(\t\x12\x11\n\tgivenname\x18\x02 \x01(\t\"^\n\x07Student\x12\x13\n\x04name\x18\x01 \x01(\x0b\x32\x05.Name\x12\x19\n\x07\x66\x61\x63ulty\x18\x02 \x01(\x0b\x32\x08.Faculty\x12\x13\n\x0byearOfBirth\x18\x03 \x01(\x05\x12\x0e\n\x06\x65xists\x18\x04 \x01(\x08\"\x91\x02\n\x07\x46\x61\x63ulty\x12)\n\x0b\x66\x61\x63ultyname\x18\x01 \x01(\x0e\x32\x14.Faculty.FacultyName\"\xda\x01\n\x0b\x46\x61\x63ultyName\x12\x0f\n\x0bUnspecified\x10\x00\x12\x17\n\x13\x41rchitekturBauwesen\x10\x01\x12\x1e\n\x1a\x45lektroInformationstechnik\x10\x02\x12#\n\x1fInformatikWirtschaftsinformatik\x10\x03\x12 \n\x1cInformationsmanagementMedien\x10\x04\x12\x1b\n\x17MaschinenbauMechatronik\x10\x05\x12\x1d\n\x19Wirtschaftswissenschaften\x10\x06\x32T\n\x08Students\x12 \n\x0bListStudent\x12\x05.Name\x1a\x08.Student\"\x00\x12&\n\x0cListStudents\x12\x08.Faculty\x1a\x08.Student\"\x00\x30\x01\x42.\n\x14io.grpc.hka.studentsB\rStudentsProtoP\x01\xa2\x02\x04HKASb\x06proto3'
)



_FACULTY_FACULTYNAME = _descriptor.EnumDescriptor(
  name='FacultyName',
  full_name='Faculty.FacultyName',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unspecified', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ArchitekturBauwesen', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ElektroInformationstechnik', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InformatikWirtschaftsinformatik', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InformationsmanagementMedien', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MaschinenbauMechatronik', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Wirtschaftswissenschaften', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=431,
)
_sym_db.RegisterEnumDescriptor(_FACULTY_FACULTYNAME)


_NAME = _descriptor.Descriptor(
  name='Name',
  full_name='Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='surname', full_name='Name.surname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='givenname', full_name='Name.givenname', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=17,
  serialized_end=59,
)


_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Student.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='faculty', full_name='Student.faculty', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yearOfBirth', full_name='Student.yearOfBirth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exists', full_name='Student.exists', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=61,
  serialized_end=155,
)


_FACULTY = _descriptor.Descriptor(
  name='Faculty',
  full_name='Faculty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='facultyname', full_name='Faculty.facultyname', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FACULTY_FACULTYNAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=431,
)

_STUDENT.fields_by_name['name'].message_type = _NAME
_STUDENT.fields_by_name['faculty'].message_type = _FACULTY
_FACULTY.fields_by_name['facultyname'].enum_type = _FACULTY_FACULTYNAME
_FACULTY_FACULTYNAME.containing_type = _FACULTY
DESCRIPTOR.message_types_by_name['Name'] = _NAME
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['Faculty'] = _FACULTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), {
  'DESCRIPTOR' : _NAME,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:Name)
  })
_sym_db.RegisterMessage(Name)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  })
_sym_db.RegisterMessage(Student)

Faculty = _reflection.GeneratedProtocolMessageType('Faculty', (_message.Message,), {
  'DESCRIPTOR' : _FACULTY,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:Faculty)
  })
_sym_db.RegisterMessage(Faculty)


DESCRIPTOR._options = None

_STUDENTS = _descriptor.ServiceDescriptor(
  name='Students',
  full_name='Students',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=433,
  serialized_end=517,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListStudent',
    full_name='Students.ListStudent',
    index=0,
    containing_service=None,
    input_type=_NAME,
    output_type=_STUDENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListStudents',
    full_name='Students.ListStudents',
    index=1,
    containing_service=None,
    input_type=_FACULTY,
    output_type=_STUDENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDENTS)

DESCRIPTOR.services_by_name['Students'] = _STUDENTS

# @@protoc_insertion_point(module_scope)
