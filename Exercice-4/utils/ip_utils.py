import ipaddress

class IPValidator:
    """
    Classe pour la validation et l'identification des adresses IP (IPv4 et IPv6).
    """

    @staticmethod
    def is_valid_ipv4(ip: str) -> bool:
        """Vérifie si une adresse est un IPv4 valide."""
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def is_valid_ipv6(ip: str) -> bool:
        """Vérifie si une adresse est un IPv6 valide."""
        try:
            ipaddress.IPv6Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def identify_ip_version(ip: str) -> str:
        """
        Identifie si une adresse est une IPv4 ou une IPv6 valide.
        """
        if IPValidator.is_valid_ipv4(ip):
            return "IPv4 valide"
        elif IPValidator.is_valid_ipv6(ip):
            return "IPv6 valide"
        else:
            return "Adresse IP non valide"

    @staticmethod
    def validate_ip_list(ip_list: list) -> dict:
        """
        Valide une liste d'adresses IP et retourne un dictionnaire avec leur type.
        """
        return {ip: IPValidator.identify_ip_version(ip) for ip in ip_list}

    @staticmethod
    def validate_ip_dict(ip_dict: dict) -> dict:
        """
        Valide un dictionnaire contenant des hôtes et leurs adresses IP.
        """
        return {host: IPValidator.identify_ip_version(ip) for host, ip in ip_dict.items()}
