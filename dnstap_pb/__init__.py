__version__ = "0.1.0"

# dnstap_pb2 generation guideline
# 
# wget https://raw.githubusercontent.com/dnstap/dnstap.pb/master/dnstap.proto
# wget https://github.com/protocolbuffers/protobuf/releases/download/v3.13.0/protoc-3.13.0-linux-x86_64.zip
# python3 -m pip install protobuf
# bin/protoc --python_out=. dnstap.proto

from dnstap_pb.dnstap_pb2 import *