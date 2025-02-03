import ipaddress

def is_valid_ipv4(ip: str) -> bool:
    """
    Vérifie si une adresse IP est valide au format IPv4.

    :param ip: L'adresse IP à valider.
    :return: True si l'IP est valide en tant qu'IPv4, False sinon.
    """
    try:
        # Tentative de création d'une adresse IPv4
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        # Si une exception est levée, l'adresse n'est pas valide en tant qu'IPv4
        return False


def is_valid_ipv6(ip: str) -> bool:
    """
    Vérifie si une adresse IP est valide au format IPv6.

    :param ip: L'adresse IP à valider.
    :return: True si l'IP est valide en tant qu'IPv6, False sinon.
    """
    try:
        # Tentative de création d'une adresse IPv6
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        # Si une exception est levée, l'adresse n'est pas valide en tant qu'IPv6
        return False


def identify_ip_version(ip: str) -> str:
    """
    Identifie la version d'une adresse IP (IPv4 ou IPv6).

    :param ip: L'adresse IP à identifier.
    :return: Un message indiquant si l'IP est IPv4, IPv6 ou non valide.
    """
    # Vérification du type d'adresse IP
    if is_valid_ipv4(ip):
        return "IPv4 valide"
    elif is_valid_ipv6(ip):
        return "IPv6 valide"
    else:
        return "Adresse IP non valide"


def validate_ip_list(ip_list: list) -> dict:
    """
    Valide une liste d'adresses IP et retourne un dictionnaire avec leur statut.

    :param ip_list: Liste des adresses IP à valider.
    :return: Un dictionnaire avec chaque adresse IP et son statut.
    """
    return {ip: identify_ip_version(ip) for ip in ip_list}


def validate_ip_dict(ip_dict: dict) -> dict:
    """
    Valide un dictionnaire d'adresses IP et retourne un dictionnaire avec leur statut.

    :param ip_dict: Dictionnaire où les clés sont des hôtes et les valeurs des adresses IP.
    :return: Un dictionnaire avec chaque hôte et le statut de son adresse IP.
    """
    result = {}
    for host, ip in ip_dict.items():
        try:
            result[host] = identify_ip_version(ip)
        except Exception as e:
            # En cas d'erreur, associer l'erreur à l'hôte
            result[host] = f"Erreur : {str(e)}"
    return result
