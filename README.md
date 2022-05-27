# Dnstap Protocol Buffers implementation in Python

Dnstap Protocol Buffers implementation in Python, more informations on dnstap http://dnstap.info/.
This library is based on the following [protocol buffers schema](https://raw.githubusercontent.com/dnstap/dnstap.pb/master/dnstap.proto).

## Installation

This module can be installed from [pypi](https://pypi.org/project/dnstap_pb) website

```python
pip install dnstap_pb
```

## Decoder

Example to use the Dnstap decoder

```python
import dnstap_pb

# dnstap decoder
dnstap = dnstap_pb.Dnstap()

payload = b'\n\x08dnsdist1\x12\rdnsdist 1.5.0r[\x08\x05\x10\x01\x18\x01"\x04\n\x00'
payload += b'\x00\xd2*\x04\n\x00\x00\xd20\xe6\xae\x0385@\x8e\x8f\xc6\xff\x05M\x1cf,'
payload += b'\x15R6\xda\xba\x01 \x00\x01\x00\x00\x00\x00\x00\x01\x03www\x06google\x02'
payload += b'fr\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x0c\x00\n\x00'
payload += b'\x08\xe68\xe3\x8e\x7f\x01\xdexx\x01'

dnstap.ParseFromString(payload)

dm = dnstap.message
print(dm)
type: CLIENT_QUERY
socket_family: INET
socket_protocol: UDP
query_address: "\n\000\000\322"
response_address: "\n\000\000\322"
query_port: 60218
response_port: 53
query_time_sec: 1609664434
query_time_nsec: 533617553
query_message: "\221W\001 \000\001\000\000\000\000\000\001\003www\006google\002fr\000\000\001
\000\001\000\000)\020\000\000\000\000\000\000\014\000\n\000\010\273\257\370\014_\001\341-"
```

## Encoder

Example to use the Dnstap encoder

```python
import dnstap_pb

# dnstap encoder
dnstap = dnstap_pb.Dnstap()

# clear all fields
dnstap.Clear()

# constructs the message
dnstap.type = 1
dnstap.version = b"0.1.0"
dnstap.identity = b"dnstap_python"

dnstap.message.type = dnstap_pb.dnstap_pb2._MESSAGE_TYPE.values_by_name["CLIENT_QUERY"].number
dnstap.message.socket_protocol = dnstap_pb.dnstap_pb2._SOCKETPROTOCOL.values_by_name["UDP"].number
dnstap.message.socket_family = dnstap_pb.dnstap_pb2._SOCKETFAMILY.values_by_name["INET"].number

# serialize the dnstap message to binary
payload = dnstap.SerializeToString()
```

# Development

dnstap_pb2 file generation guideline
 
Download dnstap.proto from https://github.com/dnstap/dnstap.pb

```
wget https://raw.githubusercontent.com/dnstap/dnstap.pb/master/dnstap.proto
```

Download protoc

```
export VER=21.0
wget https://github.com/protocolbuffers/protobuf/releases/download/v$VER/protoc-$VER-linux-x86_64.zip
unzip protoc-$VER-linux-x86_64.zip
```

Generate proto

```
python3 -m pip install protobuf
bin/protoc --python_out=. dnstap.proto
```
