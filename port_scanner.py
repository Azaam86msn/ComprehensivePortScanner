import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    def is_valid_ip(ip):
        # Check if IP follows the IPv4 format and each segment is between 0 and 255
        segments = ip.split(".")
        if len(segments) != 4:
            return False
        for segment in segments:
            if not segment.isdigit() or not 0 <= int(segment) <= 255:
                return False
        return True

    # Resolve target to hostname and IP address
    if is_valid_ip(target):
        ip_address = target
        hostname = None
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            pass
    else:
        if any(char.isalpha() for char in target):  # Check if target might be a hostname
            try:
                ip_address = socket.gethostbyname(target)
                hostname = target
            except socket.gaierror:
                return "Error: Invalid hostname"
        else:
            return "Error: Invalid IP address"

    # Scan each port in the given range
    for port in range(port_range[0], port_range[1] + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # Increased timeout for reliability
                result = s.connect_ex((ip_address, port))
                if result == 0:
                    open_ports.append(port)
        except Exception:
            pass  # Ignore errors for individual ports

    # Prepare verbose output
    if verbose:
        result = []
        if hostname:
            result.append(f"Open ports for {hostname} ({ip_address})")
        else:
            result.append(f"Open ports for {ip_address}")
        result.append("PORT     SERVICE")
        for port in open_ports:
            service = ports_and_services.get(port, "unknown")
            result.append(f"{port:<9}{service}")
        return "\n".join(result)

    return open_ports
