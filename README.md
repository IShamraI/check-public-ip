# Public IP Address Fetcher

This Python script fetches the public IP address from a given URL and stores it in a file. It checks if the IP address has changed since the last retrieval.

## Installation

1. Clone this repository or download the `public_ip_address.py` file.

2. Ensure you have Python 3 installed on your system.

## Usage

Run the script from the command line:

```shell
python public_ip_address.py [--url URL]

```


Optional arguments:

- `--url URL`: Specify the URL to fetch the public IP address. Default is `https://ifconfig.me/ip`.

## Output

- The script will print the current public IP address.
- It will also print whether the IP address has changed since the last retrieval.

## Logging

The script uses logging for debug information and status messages. By default, it logs messages with the level `DEBUG` and above.

## File Storage

The script stores the fetched IP address in a pickle file named `.ipaddress.pkl` in the current directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

