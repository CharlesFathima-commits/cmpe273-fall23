import grpc
from concurrent import futures
import addressValidation_pb2
import addressValidation_pb2_grpc
import logging
import requests
class ValidateAddressService(addressValidation_pb2_grpc.ValidateAddressServiceServicer):
    def ValidateAddress(self, request, context):
        result = self.isValidAddress(request)
        return addressValidation_pb2_grpc.ValidateAddress_Response(result=result)
        
    def isValidAddress(self,request):
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        api_key= "AIzaSyBea0uH4QRAVkMDZUW8pwq21S02dhW-uAE"
        params = {
            'locality': request.locality,
            'postalCode': request.postalCode,
            'address': request.addressLines,
            'key': api_key
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            if data.get("status") == "OK":
                return True
            else:
                return False
        else:
            return False
        return True

    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressValidation_pb2_grpc.add_ValidateAddressServiceServicer_to_server(
        ValidateAddressService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()