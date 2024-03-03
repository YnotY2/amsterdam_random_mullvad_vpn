# MullvadVPN Connection Tool

## Explained

This tool is designed to start and end connections when specified to random Amsterdam MullvadVPN servers using WireGuard. It provides functionality to automatically start, vertify, and quit connection, as well as view relevant connection details in the terminal. This is a very simple lil-code that I thought I would make public cuz why not 0-0 . You can quite easily modify the code for you're use case... 

- MullVad config-files download url; "https://mullvad.net/en/account/wireguard-config"

## Usage

+ Firt off make sure you WireGuard installed on youre system and have downloaded the WireGuard MullVad-VPN config files, and saved them within "/etc/wireguard" .

To use this tool, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

```bash
git clone git@github.com:YnotY2/amsterdam_random_mullvad_vpn.git
```


### Settings: 

After setting up the needed file's you can navigate over the the; "./config/settings.py" direcory. This "settings.py" file is where you *need* specifiy the following; 

- MullVadVPN WireGuard Config Files

Please replace these file's with the actually file names of you're config-files for wireguard and mullvad, downloaded from above url. If you simply want to connect to all available Amsterdam I.P's (like me) download all available config-files for amsterdam and save them in the "/etc/wireguard/" directory. Code should imidiatly work. 

"settings.py" file visualised; 
```python
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
```



2. **Install Dependencies**: Make sure you have all dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

3. **Grant file-permissions**:Make sure the files running code have correct permissions. You can grant perms using:

```bash
sudo python3 grant_permissions.py
```

3. **Run the Tool**: Execute the `main.py` file to start the MullvadVPN connection tool:

```bash
python3 main.py
```

## Ouput-code:

```python
2024-03-03 01:29:50,500 - INFO - main - Calling grant_read_status_outside_of_root_wireguard_config_files.py service -function
2024-03-03 01:29:50,500 - INFO - grant_read_status_outside_of_root_wireguard_config_files - Executing grant_read_status_outside_of_root_wireguard_config_files.sh script
2024-03-03 01:29:50,513 - INFO - grant_read_status_outside_of_root_wireguard_config_files - Read permissions granted successfully to /etc/wireguard directory.

2024-03-03 01:29:50,513 - INFO - main - Calling start_connection_wireguard_mullvadvpn.py service -function
2024-03-03 01:29:50,513 - INFO - start_connection_wireguard_mullvadvpn - Attempting to connect to a random MullVadVPN exit-I.P
Warning: `/etc/wireguard/nl-ams-wg-007.conf' is world accessible
[#] ip link add nl-ams-wg-007 type wireguard
[#] wg setconf nl-ams-wg-007 /dev/fd/63
[#] ip -4 address add 10.69.151.45/32 dev nl-ams-wg-007
[#] ip -6 address add fc00:bbbb:bbbb:bb01::6:972c/128 dev nl-ams-wg-007
[#] ip link set mtu 1420 up dev nl-ams-wg-007
[#] resolvconf -a tun.nl-ams-wg-007 -m 0 -x
[#] wg set nl-ams-wg-007 fwmark 51820
[#] ip -6 route add ::/0 dev nl-ams-wg-007 table 51820
[#] ip -6 rule add not fwmark 51820 table 51820
[#] ip -6 rule add table main suppress_prefixlength 0
[#] nft -f /dev/fd/63
[#] ip -4 route add 0.0.0.0/0 dev nl-ams-wg-007 table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63
2024-03-03 01:29:50,567 - INFO - start_connection_wireguard_mullvadvpn - Successfully connected to MullvadVPN config-file: nl-ams-wg-007.conf

2024-03-03 01:29:50,568 - INFO - main - Calling fetch_ip_from_wireguard_mullvad_config_file.py service -function
2024-03-03 01:29:50,568 - INFO - fetch_ip_from_wireguard_mullvad_config_file - Attempting to fetch MullVadVPN exit I.P found in wireguard config file
2024-03-03 01:29:50,568 - INFO - fetch_ip_from_wireguard_mullvad_config_file - Successfully found the I.P within the: 'nl-ams-wg-007.conf'
2024-03-03 01:29:50,568 - INFO - fetch_ip_from_wireguard_mullvad_config_file - I.P:  185.65.134
2024-03-03 01:29:50,568 - INFO - fetch_ip_from_wireguard_mullvad_config_file - !Important! : The I.P here is only the first 3 sets of numbers from the actual IP. We only fetch these as they are always the same when checking on an external website for I.P address. So we can always confirm correct IP matching the first 3 sets of numbers.

2024-03-03 01:29:50,568 - INFO - main - Calling verify_connection_and_ip_wireguard_mullvadvpn.py service -function
2024-03-03 01:29:50,568 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Attempting to verify connection to correct MullVadVPN exit-I.P
2024-03-03 01:29:50,568 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Fetching JSON-object from mullvad-API domain:  'https://am.i.mullvad.net/json' 

2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - MullvadVPN exit IP fetched from website: 185.65.134.197
2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Attempting to shorten to IP-address to only first 3-set's of identifiable numbers.
2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Successfully shortend the I.P .

2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Attempting to cross reference IP addresses:
2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - IP address returned from config-file 'nl-ams-wg-007.conf':       185.65.134 
2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - IP address reflected from website:       185.65.134 
2024-03-03 01:29:50,972 - INFO - verify_connection_and_ip_wireguard_mullvadvpn - Successfully verified random available IP returned by "start_connection_wireguard_mullvadvpn.py" is currently being utilized. 

2024-03-03 01:29:50,972 - INFO - main - Calling verify_mullvad_exit_ip_hostname_currently_utilised.py service -function
2024-03-03 01:29:50,972 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - Attempting to fetch MullVadVPN exit-I.P hostname currently being utilised by VPN-I.P
2024-03-03 01:29:50,972 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - Fetching JSON-object from mullvad-API domain:  'https://am.i.mullvad.net/json' 

2024-03-03 01:29:51,083 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - Attempting to cross reference MullvadVPN exit-ip-hostname's:
2024-03-03 01:29:51,083 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - MullvadVPN exit-ip-hostname's config-file:    nl-ams-wg-007 
2024-03-03 01:29:51,083 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - MullvadVPN exit-ip-hostname reflected from website:       nl-ams-wg-007 
2024-03-03 01:29:51,083 - INFO - verify_mullvad_exit_ip_hostname_currently_utilised - Successfully verified mullvad exit-ip-hostname from currently live config-file is currently being utilized. 

2024-03-03 01:29:51,083 - INFO - main - Calling verfify_mullvad_vpn_server_type.py service -function
2024-03-03 01:29:51,083 - INFO - verfify_mullvad_vpn_server_type - Attempting to verify 'WireGuard' connection-type is currently being utilised by VPN-I.P185.65.134 
2024-03-03 01:29:51,083 - INFO - verfify_mullvad_vpn_server_type - Fetching JSON-object from mullvad-API domain:  'https://am.i.mullvad.net/json' 

2024-03-03 01:29:51,193 - INFO - verfify_mullvad_vpn_server_type - Attempting to cross reference MullvadVPN connection-type's:
2024-03-03 01:29:51,194 - INFO - verfify_mullvad_vpn_server_type - MullvadVPN server-type initialized:    WireGuard 
2024-03-03 01:29:51,194 - INFO - verfify_mullvad_vpn_server_type - MullvadVPN server-type fetched from website:    WireGuard 
2024-03-03 01:29:51,194 - INFO - verfify_mullvad_vpn_server_type - Successfully verified mullvad server-type from currently live config-file is currently being utilized. 

2024-03-03 01:29:51,194 - INFO - main - Checking if all returns needed for confirming successfull connection from random specified mullvad-vpn config-file True... 
2024-03-03 01:29:51,194 - INFO - main - Sucessfully verified we are connected to WireGuard MullVad-VPN exit-I.P. 

Currently live MullVadVPN connection:

Server-type:  WireGuard
Local config-file:  nl-ams-wg-007.conf
Exit-I.P hostname:  nl-ams-wg-007
Exit-I.P :  185.65.134.197

 type either q/Q to quit current VPN connection:  q
2024-03-03 01:29:55,650 - INFO - main - Calling verify_mullvad_exit_ip_hostname_currently_utilised.py service -function
2024-03-03 01:29:55,651 - INFO - quit_connection_wireguard_mullvadvpn - Attempting to quit connection to live MullVadVPN exit-I.P:   185.65.134 
2024-03-03 01:29:55,654 - INFO - quit_connection_wireguard_mullvadvpn - MullvadVPN exit-ip-hostname's config-file:    nl-ams-wg-007.conf 
Warning: `/etc/wireguard/nl-ams-wg-007.conf' is world accessible
[#] ip -4 rule delete table 51820
[#] ip -4 rule delete table main suppress_prefixlength 0
[#] ip -6 rule delete table 51820
[#] ip -6 rule delete table main suppress_prefixlength 0
[#] ip link delete dev nl-ams-wg-007
[#] resolvconf -d tun.nl-ams-wg-007 -f
[#] nft -f /dev/fd/63
2024-03-03 01:29:55,895 - INFO - quit_connection_wireguard_mullvadvpn - Successfully quit connection to MullvadVPN config-file: nl-ams-wg-007.conf
2024-03-03 01:29:55,895 - INFO - quit_connection_wireguard_mullvadvpn - Successfully quit connection to MullvadVPN I.P: 185.65.134

```

