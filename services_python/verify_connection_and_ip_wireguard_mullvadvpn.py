from utils.colors import Colors
from utils.logger import setup_logger
import requests
from config.settings import mullvad_vpn_check_connection_domain
import re

# Set up logger with service name
service_name = "verify_connection_and_ip_wireguard_mullvadvpn"
logger = setup_logger(service_name)

# You are connected to Mullvad (server nl-ams-wg-007). Your IP address is 185.65.134.197        ## This is the returned string from request
# We should modify our code to instead of cross-referencing "config-names" we should cross reference "I.P-address"
# We can do this by reading out I.P address from the config-file we are currently connected to.
# Then fetching a JSON object from MullVadVPN API that contains that IP and more usefull info.

# When we are actually connecting to the accs, it might be usefull to have a function that read's
# IP from config file listed in object account_info "https://github.com/YnotY2/google_horeca_reviews/blob/main/databases.md"
# We will add the following;
# server-name
# config-name
# IP (already_existant)
def verify_connection_and_ip_wireguard_mullvadvpn(utilised_wireguard_mullvadvpn_config_file, fetched_ip_from_config_file):

    logger.info(f"{Colors.CYAN}Attempting to verify connection to correct MullVadVPN exit-I.P{Colors.END}")

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

            mullvad_exit_ip = json_data.get('ip', '')

            # Log the fetched MullvadVPN exit IP
            logger.info(f"{Colors.CYAN}MullvadVPN exit IP fetched from website: {mullvad_exit_ip}{Colors.END}")

            # Shorten the exit-ip to only the first 3-set's of numbers
            # Extract the first 3 sets of numbers from the IP address
            logger.info(f"{Colors.BLUE}Attempting to shorten to IP-address to only first 3-set's of identifiable numbers.{Colors.END}")
            try:
                ip_parts = mullvad_exit_ip.split(".")[:3]
                # Join the parts back together to form the IP string
                reformated_mullvad_exit_ip = ".".join(ip_parts)
                logger.info(f"{Colors.GREEN}Successfully shortend the I.P .")
                print("")
            except Exception as e:
                logger.error(f"{Colors.RED}Failed to shorten IP '{mullvad_exit_ip}': {e} ")

            # Cross reference both user_agents
            logger.info(f"{Colors.CYAN}Attempting to cross reference IP addresses:{Colors.END}")
            logger.info(f"{Colors.BLUE}IP address returned from config-file '{utilised_wireguard_mullvadvpn_config_file}':     {Colors.END} {Colors.BLUE} {fetched_ip_from_config_file} {Colors.END}")
            logger.info(f"{Colors.BLUE}IP address reflected from website:     {Colors.END} {Colors.BLUE} {reformated_mullvad_exit_ip} {Colors.END}")

            if fetched_ip_from_config_file == reformated_mullvad_exit_ip:
                # Log successful verification
                logger.info(f'{Colors.GREEN}Successfully verified random available IP returned by "start_connection_wireguard_mullvadvpn.py" is currently being utilized. {Colors.END}')
                print("")
                return mullvad_exit_ip

            else:
                # Log mismatch between user-agents
                logger.error(f"{Colors.RED}Error: Mismatch between IP addresses. address initialized: {fetched_ip_from_config_file}, address fetched from website: {reformated_mullvad_exit_ip} {Colors.END}")
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
    verify_connection_and_ip_wireguard_mullvadvpn()