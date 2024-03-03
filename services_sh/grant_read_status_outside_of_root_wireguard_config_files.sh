#!/bin/bash

grant_read_status_outside_of_root_wireguard_config_files() {
    # Grant read permissions to the /etc/wireguard directory and its contents
    # sudo chmod 644 /etc/wireguard/*.conf
    sudo chmod a+r /etc/wireguard/*.conf
    sudo chmod a+rx /etc/wireguard
    echo "Read permissions granted successfully to /etc/wireguard directory."
}

# Call the function to grant read permissions
grant_read_status_outside_of_root_wireguard_config_files
