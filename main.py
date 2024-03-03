import time

from utils.colors import Colors
from utils.logger import setup_logger

from services_python.start_connection_wireguard_mullvadvpn import start_connection_wireguard_mullvadvpn
from services_python.grant_read_status_outside_of_root_wireguard_config_files import grant_read_status_outside_of_root_wireguard_config_files
from services_python.fetch_ip_from_wireguard_mullvad_config_file import fetch_ip_from_wireguard_mullvad_config_file
from services_python.verify_connection_and_ip_wireguard_mullvadvpn import verify_connection_and_ip_wireguard_mullvadvpn
from services_python.verify_mullvad_exit_ip_hostname_currently_utilised import verify_mullvad_exit_ip_hostname_currently_utilised
from services_python.quit_connection_wireguard_mullvadvpn import quit_connection_wireguard_mullvadvpn
from services_python.verfify_mullvad_vpn_server_type import verfify_mullvad_vpn_server_type
from services_python.print_recap_live_connection_details_to_terminal import print_recap_live_connection_details_to_terminal


# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

def main():
    try:

        # Start and verify VPN connection to Amsterdam Exit I.P
        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} grant_read_status_outside_of_root_wireguard_config_files.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        grant_read_status_outside_of_root_wireguard_config_files()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} start_connection_wireguard_mullvadvpn.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        utilised_wireguard_mullvadvpn_config_file = start_connection_wireguard_mullvadvpn()     # starts connection from a random config-file.

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} fetch_ip_from_wireguard_mullvad_config_file.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        fetched_ip_from_config_file = fetch_ip_from_wireguard_mullvad_config_file(utilised_wireguard_mullvadvpn_config_file)        # Fetches IP we are currently using from config file

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} verify_connection_and_ip_wireguard_mullvadvpn.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        mullvad_exit_ip = verify_connection_and_ip_wireguard_mullvadvpn(utilised_wireguard_mullvadvpn_config_file, fetched_ip_from_config_file)       # This returns 'True' if I.P fetched is the same as I.P initialized from config-file

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} verify_mullvad_exit_ip_hostname_currently_utilised.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        mullvad_exit_ip_hostname = verify_mullvad_exit_ip_hostname_currently_utilised(utilised_wireguard_mullvadvpn_config_file)        # They have the same name, when you download a config file it has the exit_ip_hostname as the file name of the config.

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} verfify_mullvad_vpn_server_type.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        fetched_mullvad_server_type = verfify_mullvad_vpn_server_type(fetched_ip_from_config_file)           # This returns 'WireGuard' server type if sever-type is WireGuard

        ## Currently we have successfully verified these 4 variables parmaters for in db object; user-agent, mullvad-exit-ip, mullvad-exit-ip-hostname, WireGuard-server-type


        # Finally we will verify all needed parameters for connecting to Google Account login
        logger.info(f"{Colors.BLUE}Checking if all returns needed for confirming successfull connection from random specified mullvad-vpn config-file True... {Colors.END}")
        try:
            if verify_connection_and_ip_wireguard_mullvadvpn:
                try:
                    if mullvad_exit_ip_hostname:
                        try:
                            if fetched_mullvad_server_type:

                                logger.info(f"{Colors.GREEN}Sucessfully verified we are connected to WireGuard MullVad-VPN exit-I.P. {Colors.END}")
                                print("")
                                try:
                                    print_recap_live_connection_details_to_terminal(utilised_wireguard_mullvadvpn_config_file, mullvad_exit_ip_hostname, fetched_mullvad_server_type, mullvad_exit_ip)
                                    print("")


                                except Exception as e:
                                    logger.error(f"{Colors.RED}Error: While logging current MullVadVPN connection to terminal: {e} {Colors.END}")

                                try:
                                    stop_code = False
                                    while not stop_code:
                                        quit_connection_awnser = input(f"{Colors.YELLOW} type either q/Q to quit current VPN connection:  {Colors.END}")

                                        if quit_connection_awnser.upper() == "Q":
                                            logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} verify_mullvad_exit_ip_hostname_currently_utilised.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
                                            quit_connection_wireguard_mullvadvpn(fetched_ip_from_config_file, utilised_wireguard_mullvadvpn_config_file)
                                            stop_code = True

                                        else:
                                            logger.error(f"{Colors.RED}Key code is neither q/Q please type a valid key.{Colors.END}")
                                            stop_code = False


                                except Exception as e:
                                    logger.error(f"{Colors.RED}Error: While attepmting or already quiting MullVadVPN connection: {e} {Colors.END}")

                            else:
                                logger.error(
                                    f"{Colors.RED}Error: While attempting to confirm successful return of fetched_mullvad_server_type {Colors.END}")
                        except Exception as e:
                            logger.error(
                                f"{Colors.RED}Error: While attempting to confirm successful return of fetched_mullvad_server_type: {e} {Colors.END}")

                    else:
                        logger.error(f"{Colors.RED}Error: While attempting to confirm mullvad_exit_ip_hostname returned successfully {Colors.END}")
                except Exception as e:
                    logger.error(f"{Colors.RED}Error: While attempting to confirm mullvad_exit_ip_hostname returned successfully: {e} {Colors.END}")

            else:
                logger.error(f"{Colors.RED}Error: While attempting to confirm connection to wireguard I.P returned True successfully{Colors.END}")
        except Exception as e:
            logger.error(f"{Colors.RED}Error: While attempting to confirm connection to wireguard I.P returned True successfully :  {e} {Colors.END}")


    except Exception as e:
            logger.error(f"{Colors.RED}Error: while starting 'main.py' and returning 'cursor' for postgreSQL future actions.{e}{Colors.END}")

if __name__ == "__main__":
    main()
