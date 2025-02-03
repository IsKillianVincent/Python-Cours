import ipaddress

def is_valid_ipv4(ip: str) -> bool:
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip: str) -> bool:
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def identify_ip_version(ip: str) -> str:
    if is_valid_ipv4(ip):
        return "IPv4 valide"
    elif is_valid_ipv6(ip):
        return "IPv6 valide"
    else:
        return "Adresse IP non valide"

def validate_ip_list(ip_list: list) -> dict:
    return {ip: identify_ip_version(ip) for ip in ip_list}

def validate_ip_dict(ip_dict: dict) -> dict:
    return {host: identify_ip_version(ip) for host, ip in ip_dict.items()}
