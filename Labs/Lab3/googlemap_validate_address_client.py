from __future__ import print_function
import grpc
import addressValidation_pb2
import addressValidation_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = addressValidation_pb2_grpc.ValidateAddressServiceStub(channel)
    addressLines = "1334 The Alameda, #393"
    locality= "San Jose"
    postalCode= "95126"
    address = addressLines + locality + postalCode
    response = stub.ValidateAddress(addressValidation_pb2.ValidateAddress_Request(postalCode= postalCode, locality=locality, addressLines=addressLines))
    if response.is_valid:
        print(f"The address '{address}' is valid.")
    else:
        print(f"The address '{address}' is not valid.")

if __name__ == '__main__':
    run()