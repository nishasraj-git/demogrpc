# client.py
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        number = float(input("Enter a number: "))
        request = calculator_pb2.SquareRootRequest(number=number)
        response = stub.SquareRoot(request)
        print(f"Square root of {number} is: {response.result}")

if __name__ == '__main__':
    run()
