from utils.colors import Colors

def print_recap_live_connection_details_to_terminal(utilised_wireguard_mullvadvpn_config_file, mullvad_exit_ip_hostname, fetched_mullvad_server_type, mullvad_exit_ip):
    try:
        print(f"{Colors.YELLOW}Currently live MullVadVPN connection:{Colors.END}")
        print("")
        print(f"{Colors.MAGENTA}Server-type:{Colors.END}  {Colors.YELLOW}{fetched_mullvad_server_type}{Colors.END}")
        print(f"{Colors.MAGENTA}Local config-file:{Colors.END}  {Colors.YELLOW}{utilised_wireguard_mullvadvpn_config_file}{Colors.END}")
        print(f"{Colors.MAGENTA}Exit-I.P hostname:{Colors.END}  {Colors.YELLOW}{mullvad_exit_ip_hostname}{Colors.END}")
        print(f"{Colors.MAGENTA}Exit-I.P :{Colors.END}  {Colors.YELLOW}{mullvad_exit_ip}{Colors.END}")



    except Exception as e:
        print(f"{Colors.RED}Error, while atempting to log live con details to terminal; {e}{Colors.END}")

if __name__ == "__main__":
    print_recap_live_connection_details_to_terminal()