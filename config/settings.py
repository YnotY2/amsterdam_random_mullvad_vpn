import os

# MullVad API endpoint returning JSON-object
mullvad_vpn_check_connection_domain = os.getenv("mullvad_vpn_check_connection_domain", "https://am.i.mullvad.net/json")

# MullVadVPN WireGuard Config Files         //Code assumes your files are stored within dir '/etc/wireguard/'
wireguard_mullvadvpn_ip_nl_ams_wg_001 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-001", "nl-ams-wg-001.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_002 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-002", "nl-ams-wg-002.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_003 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-003", "nl-ams-wg-003.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_004 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-004", "nl-ams-wg-004.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_005 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-005", "nl-ams-wg-005.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_006 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-006", "nl-ams-wg-006.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_007 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-007", "nl-ams-wg-007.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_101 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-101", "nl-ams-wg-101.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_102 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-102", "nl-ams-wg-102.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_201 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-201", "nl-ams-wg-201.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_202 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-202", "nl-ams-wg-202.conf")
wireguard_mullvadvpn_ip_nl_ams_wg_203 = os.getenv("wireguard_mullvadvpn_ip_nl-ams-wg-203", "nl-ams-wg-203.conf")
