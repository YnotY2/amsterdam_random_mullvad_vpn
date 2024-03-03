from utils.colors import Colors
from utils.logger import setup_logger

# Set up logger with service name
service_name = "fetch_ip_from_wireguard_mullvad_config_file"
logger = setup_logger(service_name)

def fetch_ip_from_wireguard_mullvad_config_file(utilised_wireguard_mullvadvpn_config_file):
    logger.info(f"{Colors.CYAN}Attempting to fetch MullVadVPN exit I.P found in wireguard config file{Colors.END}")

    try:
        with open(f"/etc/wireguard/{utilised_wireguard_mullvadvpn_config_file}", "r") as file:
            # Read all lines from the config file
            config_lines = file.readlines()

            # Iterate through each line to find the Endpoint field
            for line in config_lines:
                if line.startswith("Endpoint"):
                    # Split the line by whitespace to extract the IP address
                    endpoint_parts = line.split("=")
                    if len(endpoint_parts) == 2:  # Ensure the line has format "Endpoint = IP:Port"
                        # Extract the IP address from the second part
                        ip_address_with_port = endpoint_parts[1].strip()
                        # Split the IP address and port by colon to get just the IP address
                        ip_address_parts = ip_address_with_port.split(":")[0]
                        # Extract the first 3 sets of numbers from the IP address
                        ip_parts = ip_address_parts.split(".")[:3]
                        # Join the parts back together to form the IP string
                        fetched_ip_from_config_file = ".".join(ip_parts)

                        logger.info(
                            f"{Colors.GREEN}Successfully found the I.P within the: '{utilised_wireguard_mullvadvpn_config_file}'{Colors.END}")
                        logger.info(f"{Colors.CYAN}I.P: {Colors.END} {Colors.BLUE}{fetched_ip_from_config_file}{Colors.END}")
                        logger.info(
                            f"{Colors.MAGENTA}!Important! : The I.P here is only the first 3 sets of numbers from the actual IP. We only fetch these as they are always the same when checking on an external website for I.P address. So we can always confirm correct IP matching the first 3 sets of numbers.{Colors.END}")

                        print("")
                        return fetched_ip_from_config_file

            logger.error(f"{Colors.RED}Endpoint field not found in the configuration file{Colors.END}")
            return None

    except Exception as e:
        logger.error(f"Error reading config file: {e}")
        return None


if __name__ == "__main__":
    fetch_ip_from_wireguard_mullvad_config_file()