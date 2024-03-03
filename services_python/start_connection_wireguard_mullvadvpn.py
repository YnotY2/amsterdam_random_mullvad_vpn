from utils.colors import Colors
from utils.logger import setup_logger
from config.settings import wireguard_mullvadvpn_ip_nl_ams_wg_001, wireguard_mullvadvpn_ip_nl_ams_wg_002, wireguard_mullvadvpn_ip_nl_ams_wg_003, wireguard_mullvadvpn_ip_nl_ams_wg_004, wireguard_mullvadvpn_ip_nl_ams_wg_005, wireguard_mullvadvpn_ip_nl_ams_wg_006, wireguard_mullvadvpn_ip_nl_ams_wg_007, wireguard_mullvadvpn_ip_nl_ams_wg_101, wireguard_mullvadvpn_ip_nl_ams_wg_102, wireguard_mullvadvpn_ip_nl_ams_wg_201, wireguard_mullvadvpn_ip_nl_ams_wg_202, wireguard_mullvadvpn_ip_nl_ams_wg_203
import random
import subprocess

# Set up logger with service name
service_name = "start_connection_wireguard_mullvadvpn"
logger = setup_logger(service_name)

def start_connection_wireguard_mullvadvpn():

    logger.info(f"{Colors.CYAN}Attempting to connect to a random MullVadVPN exit-I.P{Colors.END}")

    # List of available WireGuard configurations
    wireguard_configs = [
        wireguard_mullvadvpn_ip_nl_ams_wg_001,
        wireguard_mullvadvpn_ip_nl_ams_wg_002,
        wireguard_mullvadvpn_ip_nl_ams_wg_003,
        wireguard_mullvadvpn_ip_nl_ams_wg_004,
        wireguard_mullvadvpn_ip_nl_ams_wg_005,
        wireguard_mullvadvpn_ip_nl_ams_wg_006,
        wireguard_mullvadvpn_ip_nl_ams_wg_007,
        wireguard_mullvadvpn_ip_nl_ams_wg_101,
        wireguard_mullvadvpn_ip_nl_ams_wg_102,
        wireguard_mullvadvpn_ip_nl_ams_wg_201,
        wireguard_mullvadvpn_ip_nl_ams_wg_202,
        wireguard_mullvadvpn_ip_nl_ams_wg_203
    ]

    try:
        # Choose a random WireGuard configuration
        selected_config = random.choice(wireguard_configs)

        if selected_config:
            # Start VPN connection
            try:
                subprocess.run(['sudo', 'wg-quick', 'up', f'/etc/wireguard/{selected_config}'])
                logger.info(f"{Colors.GREEN}Successfully connected to MullvadVPN config-file:{Colors.END}{Colors.BLUE} {selected_config}{Colors.END}{Colors.END}")
                print("")
                return selected_config

            except Exception as e:
                logger.error(f"{Colors.RED}Error: while connecting to mullvadVPN via wireguard{e} {Colors.END}")
                return False
        else:
            logger.error(f"{Colors.RED}No WireGuard configuration available.{Colors.END}")
            return False

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e} {Colors.END}")
        return False

if __name__ == "__main__":
    start_connection_wireguard_mullvadvpn()