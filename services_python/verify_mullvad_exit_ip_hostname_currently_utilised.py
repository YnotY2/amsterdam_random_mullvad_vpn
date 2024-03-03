from utils.colors import Colors
from utils.logger import setup_logger
import requests
from config.settings import mullvad_vpn_check_connection_domain

# Set up logger with service name
service_name = "verify_mullvad_exit_ip_hostname_currently_utilised"
logger = setup_logger(service_name)

def verify_mullvad_exit_ip_hostname_currently_utilised(utilised_wireguard_mullvadvpn_config_file):

    logger.info(f"{Colors.CYAN}Attempting to fetch MullVadVPN exit-I.P hostname currently being utilised by VPN-I.P{Colors.END}")

    # First strip the '.conf' from our current config-file name
    utilised_wireguard_mullvadvpn_config_file = utilised_wireguard_mullvadvpn_config_file[:-5]  # Remove the last 5 characters (.conf)

    try:
        # Verifying connection to MullVadVPN exit I.P

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

            mullvad_exit_ip_hostname = json_data.get('mullvad_exit_ip_hostname', '')

            # Log the fetched MullvadVPN exit IP
            # logger.info(f"{Colors.CYAN}MullvadVPN exit-ip-hostname fetched from website: {mullvad_exit_ip_hostname}{Colors.END}")


            # Cross reference both mullvad_exit_ip_hostname from config-file and server, (they have the same name, when you download a config file it has the exit_ip_hostname as the file name of the config.
            logger.info(f"{Colors.CYAN}Attempting to cross reference MullvadVPN exit-ip-hostname's:{Colors.END}")
            logger.info(f"{Colors.BLUE}MullvadVPN exit-ip-hostname's config-file:  {Colors.END} {Colors.BLUE} {utilised_wireguard_mullvadvpn_config_file} {Colors.END}")
            logger.info(f"{Colors.BLUE}MullvadVPN exit-ip-hostname reflected from website:     {Colors.END} {Colors.BLUE} {mullvad_exit_ip_hostname} {Colors.END}")

            if utilised_wireguard_mullvadvpn_config_file == mullvad_exit_ip_hostname:
                # Log successful verification
                logger.info(f'{Colors.GREEN}Successfully verified mullvad exit-ip-hostname from currently live config-file is currently being utilized. {Colors.END}')
                print("")
                return mullvad_exit_ip_hostname

            else:
                # Log mismatch between user-agents
                logger.error(f"{Colors.RED}Error: Mismatch between mullvad_exit_ip_hostname. mullvad_exit_ip_hostname: {utilised_wireguard_mullvadvpn_config_file}, mullvad_exit_ip_hostname fetched from website: {mullvad_exit_ip_hostname} {Colors.END}")
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
    verify_mullvad_exit_ip_hostname_currently_utilised()