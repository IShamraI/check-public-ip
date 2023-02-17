# !/usr/bin/env python3
# coding: UTF-8
import logging
import pickle
import urllib.request


class PublicIpAddress(object):
    def __init__(self, url="https://ifconfig.me/ip", filename=".ipaddress.pkl"):
        self.url = url
        self._value = ''
        self._filename = filename

    def _get_ipaddress(self) -> str:
        return str(urllib.request.urlopen(self.url).read())

    @property
    def value(self) -> str:
        self._value = self._get_ipaddress()
        logging.debug(f"Received ip from {self.url}: {self._value}")
        self._save_ipaddress()
        return self._value

    def is_changed(self):
        return self._read_ipaddress() != self.value

    def _save_ipaddress(self):
        with open(self._filename, "wb") as pkl_file:
            pickle.dump(self._value, pkl_file)

    def _read_ipaddress(self) -> str:
        with open(self._filename, "rb") as pkl_file:
            return str(pickle.load(pkl_file))


def main():
    public_ip_address = PublicIpAddress()
    print(public_ip_address.value)
    print(public_ip_address.is_changed())


if __name__ == "__main__":
    main()
