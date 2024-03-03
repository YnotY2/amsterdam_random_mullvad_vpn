from utils.colors import Colors
from utils.logger import setup_logger
import subprocess

# Set up logger with service name
service_name = "quit_connection_wireguard_mullvadvpn"
logger = setup_logger(service_name)

def quit_connection_wireguard_mullvadvpn(fetched_ip_from_config_file, utilised_wireguard_mullvadvpn_config_file):

    logger.info(f"{Colors.CYAN}Attempting to quit connection to live MullVadVPN exit-I.P:{Colors.END}  {Colors.BLUE} {fetched_ip_from_config_file} {Colors.END}")
    logger.info(f"{Colors.BLUE}MullvadVPN exit-ip-hostname's config-file:  {Colors.END} {Colors.BLUE} {utilised_wireguard_mullvadvpn_config_file} {Colors.END}")

    try:
        # Quit connection
        subprocess.run(['sudo', 'wg-quick', 'down', f'/etc/wireguard/{utilised_wireguard_mullvadvpn_config_file}'])
        logger.info(f"{Colors.GREEN}Successfully quit connection to MullvadVPN config-file:{Colors.END}{Colors.BLUE} {utilised_wireguard_mullvadvpn_config_file}{Colors.END}{Colors.END}")
        logger.info(f"{Colors.GREEN}Successfully quit connection to MullvadVPN I.P:{Colors.END}{Colors.BLUE} {fetched_ip_from_config_file}{Colors.END}{Colors.END}")

        print("")
        return True


    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e} {Colors.END}")
        return False

if __name__ == "__main__":
    quit_connection_wireguard_mullvadvpn()