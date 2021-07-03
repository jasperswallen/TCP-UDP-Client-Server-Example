import time
import socket
import argparse


def tcp(addr, port):
    print("Starting TCP client...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((addr, port))

        count = 0
        while True:
            data = bytes(f"Sending message {count}".encode('ascii'))
            print(f"Sending '{data}'")
            s.sendall(data)

            count += 1
            time.sleep(0.5)


def udp(addr, port):
    print("Starting UDP client...")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server = (addr, port)

        try:
            count = 0
            while True:
                data = bytes(f"Sending message {count}".encode('ascii'))
                print(f"Sending {data} to {server}")
                s.sendto(data, server)

                count += 1
                time.sleep(0.5)
        finally:
            print("Closing connection")


def main():
    parser = argparse.ArgumentParser(
        description="Run TCP or UDP client (send data)")
    parser.add_argument('protocol', type=str, nargs=1,
                        choices=['UDP', 'TCP'], help="The protocol to send packets over (UDP or TCP)")
    parser.add_argument('--address', '--addr', '-a',
                        type=str, default='127.0.0.1', help="The IP address to send packets to (defaults to 127.0.0.1, localhost)")
    parser.add_argument('--port', '-p', type=int, default=54321,
                        help="The port to send packets to (defaults to 54321). Ports below 1000 may require special permissions or be reserved")

    args = parser.parse_args()

    if args.protocol[0] == 'UDP':
        udp(args.address, args.port)
    else:
        tcp(args.address, args.port)


if __name__ == '__main__':
    main()
