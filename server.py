import argparse
import time
import socket


def tcp(addr, port):
    print("Starting TCP server...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((addr, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            init_time = time.time()
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print(
                        f"Connection closed after {time.time() - init_time} seconds")
                    break
                print(f"Received {data}")


def udp(addr, port):
    print("Starting UDP server...")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server = (addr, port)
        s.bind(server)
        print(f"Listening on {server}")
        while True:
            payload, client_address = s.recvfrom(4096)
            print(f"Received {payload} from {client_address}")


def main():
    parser = argparse.ArgumentParser(
        description="Run TCP or UDP server (receive data)")
    parser.add_argument('protocol', type=str, nargs=1,
                        choices=['UDP', 'TCP'], help="The protocol to send packets over (UDP or TCP)")
    parser.add_argument('--address', '--addr', '-a',
                        type=str, default='127.0.0.1', help="The IP address to receive packets from (defaults to 127.0.0.1, localhost)")
    parser.add_argument('--port', '-p', type=int, default=54321,
                        help="The port to receive packets from (defaults to 54321). Ports below 1000 may require special permissions or be reserved")

    args = parser.parse_args()

    if args.protocol[0] == 'UDP':
        udp(args.address, args.port)
    else:
        tcp(args.address, args.port)


if __name__ == '__main__':
    main()
