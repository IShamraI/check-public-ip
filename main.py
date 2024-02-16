#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import logging
import pickle
import urllib.request

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class PublicIpAddress:
    """
    Class to retrieve and manage public IP address.
    """

    def __init__(self, url: str = "https://ifconfig.me/ip", filename: str = ".ipaddress.pkl"):
        """
        Initialize PublicIpAddress object.

        :param url: URL to fetch public IP address.
        :param filename: File to store the IP address.
        """
        self.url = url
        self._value = ''
        self._filename = filename

    def _get_ipaddress(self) -> str:
        """
        Fetch the public IP address from the provided URL.

        :return: Public IP address as a string.
        """
        with urllib.request.urlopen(self.url) as response:
            return response.read().decode('utf-8').strip()

    @property
    def value(self) -> str:
        """
        Retrieve the public IP address.

        :return: Public IP address.
        """
        self._value = self._get_ipaddress()
        logging.debug(f"Received IP from {self.url}: {self._value}")
        self._save_ipaddress()
        return self._value

    def is_changed(self) -> bool:
        """
        Check if the public IP address has changed.

        :return: True if IP address has changed, False otherwise.
        """
        return self._read_ipaddress() != self.value

    def _save_ipaddress(self) -> None:
        """
        Save the current IP address to a file.
        """
        with open(self._filename, "wb") as pkl_file:
            pickle.dump(self._value, pkl_file)
        logging.debug(f"Saved IP address to {self._filename}")

    def _read_ipaddress(self) -> str:
        """
        Read the IP address from the file.

        :return: IP address stored in the file.
        """
        try:
            with open(self._filename, "rb") as pkl_file:
                return pickle.load(pkl_file)
        except FileNotFoundError:
            return ''


def main() -> None:
    """
    Main function to demonstrate the usage of PublicIpAddress class.
    """
    parser = argparse.ArgumentParser(description="Fetch public IP address.")
    parser.add_argument("--url", type=str, default="https://ifconfig.me/ip", help="URL to fetch public IP address")
    args = parser.parse_args()

    public_ip_address = PublicIpAddress(url=args.url)
    logging.info("Current IP address: %s", public_ip_address.value)
    logging.info("IP address changed: %s", public_ip_address.is_changed())


if __name__ == "__main__":
    main()
