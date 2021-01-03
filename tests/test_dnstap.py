import dnstap_pb
import unittest

class TestDnstap(unittest.TestCase):
    def test_decoder(self):
        """dnstap decoder"""
        payload = b'\n\rdnstap_python\x12\x050.1.0r\x06\x08\x05\x10\x01\x18\x01x\x01'
        
        dnstap = dnstap_pb.Dnstap()
        dnstap.ParseFromString(payload)
        
        self.assertEqual( dnstap.identity, b"dnstap_python" )

    def test_encoder(self):
        """dnstap encoder"""   
        dnstap = dnstap_pb.Dnstap()

        dnstap.type = 1
        dnstap.version = b"0.1.0"
        dnstap.identity = b"dnstap_python"
        dnstap.message.type = dnstap_pb.dnstap_pb2._MESSAGE_TYPE.values_by_name["CLIENT_QUERY"].number
        dnstap.message.socket_protocol = dnstap_pb.dnstap_pb2._SOCKETPROTOCOL.values_by_name["UDP"].number
        dnstap.message.socket_family = dnstap_pb.dnstap_pb2._SOCKETFAMILY.values_by_name["INET"].number

        payload = dnstap.SerializeToString()
        self.assertEqual( len(payload), 32 )