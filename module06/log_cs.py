import logger_module as log
import socket, sys

print(dir(socket))

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((host, port))
        print(log.info(f"Port {port} is open"))
    except socket.timeout:
        print(log.warning(f"Port {port} is time out"))
    except ConnectionRefusedError:
        print(log.error(f"Port {port} is closed"))
    finally:
        sock.close


def scan_ports(host, ports):
    log.info(f"Scanning {host} on ports: {ports}")
    for port in ports:
        scan_port(host, port)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    ports = [22, 80, 443, 8080, 3306]
    scan_ports(target, ports)


# python log_cs.py google.com # for scan port in server
