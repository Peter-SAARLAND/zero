#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess

try:
    import json
except ImportError:
    import simplejson as json


class ZeroInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.zero_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.zero_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(self.inventory)

    # Example inventory for testing.
    def zero_inventory(self):
        inventory = {
            "all": {
                "hosts": []
            },
            "_meta": {
                "hostvars": {}
            }  
        }

        if0_environment = os.getenv('IF0_ENVIRONMENT', 'zero')

        # Check if ZERO_NODES is set
        if if0_environment:
            zero_nodes_manager = os.getenv('ZERO_NODES_MANAGER', "")
            zero_nodes_worker = os.getenv('ZERO_NODES_WORKER', "")

            if zero_nodes_manager and zero_nodes_manager != "":
                inventory["manager"] = []
                i = 1
                #node_count = zero_nodes.split(",").length
                for node in zero_nodes_manager.split(","):
                    hostname = "{}-manager-{}".format(if0_environment,i)
                    inventory['all']['hosts'].append(hostname)
                    inventory["manager"].append(hostname)
                    inventory['_meta']['hostvars'][hostname] = {
                        "ansible_host": node
                    }
                    i += 1

            if zero_nodes_worker and zero_nodes_worker != "":
                inventory["worker"] = []
                i = 1
                #node_count = zero_nodes.split(",").length
                for node in zero_nodes_worker.split(","):
                    hostname = "{}-worker-{}".format(if0_environment,i)
                    inventory['all']['hosts'].append(hostname)
                    inventory["worker"].append(hostname)
                    inventory['_meta']['hostvars'][hostname] = {
                        "ansible_host": node
                    }
                    i += 1
            inventory = json.dumps(inventory)
        else:
            return False
    
        return inventory

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ZeroInventory()