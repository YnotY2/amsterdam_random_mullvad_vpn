from utils.colors import Colors
from utils.logger import setup_logger
import requests
from config.settings import mullvad_vpn_check_connection_domain

# Set up logger with service name
service_name = "verfify_mullvad_vpn_server_type"
logger = setup_logger(service_name)

def verfify_mullvad_vpn_server_type(fetched_ip_from_config_file):

    logger.info(f"{Colors.CYAN}Attempting to verify 'WireGuard' connection-type is currently being utilised by VPN-I.P{Colors.END}{Colors.BLUE}{fetched_ip_from_config_file} {Colors.END}")


    try:

        logger.info(f"{Colors.CYAN}Fetching JSON-object from mullvad-API domain: {Colors.END} {Colors.MAGENTA}'{mullvad_vpn_check_connection_domain}' {Colors.END}")
        print("")

        # Send GET request to fetch the JSON object
        response = requests.get(mullvad_vpn_check_connection_domain)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            # Extract the user-agent from the JSON object
            # print(json_data)

            fetched_mullvad_server_type = json_data.get('mullvad_server_type', '')
            initialized_mullvad_server_type = "WireGuard"

            # Cross reference both mullvad_exit_ip_hostname from config-file and server, (they have the same name, when you download a config file it has the exit_ip_hostname as the file name of the config.
            logger.info(f"{Colors.CYAN}Attempting to cross reference MullvadVPN connection-type's:{Colors.END}")
            logger.info(f"{Colors.BLUE}MullvadVPN server-type initialized:  {Colors.END} {Colors.BLUE} {initialized_mullvad_server_type} {Colors.END}")
            logger.info(f"{Colors.BLUE}MullvadVPN server-type fetched from website:  {Colors.END} {Colors.BLUE} {fetched_mullvad_server_type} {Colors.END}")

            if initialized_mullvad_server_type == fetched_mullvad_server_type:
                # Log successful verification
                logger.info(f'{Colors.GREEN}Successfully verified mullvad server-type from currently live config-file is currently being utilized. {Colors.END}')
                print("")
                return fetched_mullvad_server_type

            else:
                # Log mismatch between user-agents
                logger.error(f"{Colors.RED}Error: Mismatch between mullvad_server-type. mullvad-server type: {initialized_mullvad_server_type}, mullvad_server_type fetched from website: {fetched_mullvad_server_type} {Colors.END}")
                return False
        else:
            # Print error message for non-200 status codes
            logger.error(
                f"{Colors.RED}Error: Failed to fetch JSON object. Status code: {response.status_code} {Colors.END}")
            return False

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e} {Colors.END}")
        return False

if __name__ == "__main__":
    verfify_mullvad_vpn_server_type()