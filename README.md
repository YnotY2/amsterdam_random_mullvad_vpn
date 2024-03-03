# MullvadVPN Connection Tool

This tool is designed to manage connections to MullvadVPN servers using WireGuard. It provides functionality to start, verify, and quit connections, as well as view relevant connection details in the terminal. This is a very simply lil-code that I thought I would make public cuz why not 0-0 . You can quite easily modify the code for you're use case... 

- MullVad config-files download url; "https://mullvad.net/en/account/wireguard-config"

## Usage

+ Firt off make sure you WireGuard installed on youre system and have downloaded the WireGuard MullVad-VPN config files, and saved them within "/etc/wireguard" .

To use this tool, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

```bash
git clone git@github.com:YnotY2/amsterdam_random_mullvad_vpn.git
```


2. **Install Dependencies**: Make sure you have all dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

3. **Grant file-permissions**:Make sure the files running code have correct permissions. You can grant perms using:

```bash
sudo python3 grant_permissions.py
```

