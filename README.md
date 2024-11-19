# ComprehensivePortScanner

ComprehensivePortScanner is a Python-based tool for scanning open ports on a target IP address or hostname. The tool allows users to scan a specified range of ports and retrieve detailed information about open ports and associated services. It supports both simple and verbose output modes, making it ideal for network diagnostics, security assessments, and troubleshooting.

## Features

- **Port Scanning**: Scan a given range of ports for open connections on a target IP address or hostname.
- **Verbose Output**: Provides detailed output with service names for open ports, in addition to the port numbers.
- **Error Handling**: Handles invalid IP addresses and hostnames gracefully, providing appropriate error messages.
- **Host to IP Resolution**: Resolves hostnames to IP addresses before scanning.

## Prerequisites

- Python 3.x
- Required Python Modules:
  - `socket` (included by default in Python)
  - `unittest` (included by default in Python for testing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azaam86msn/ComprehensivePortScanner.git
   cd ComprehensivePortScanner
   ```

2. Ensure the `common_ports.py` file contains the `ports_and_services` dictionary for mapping port numbers to service names. You may need to update or modify this dictionary based on the ports you are interested in scanning.

## Usage

### 1. Running the Scanner

To run the scanner and test it with example data, execute the following in the terminal:

```bash
python main.py
```

This will run predefined tests and provide sample outputs for open ports on various hosts.

### 2. Scan Example

#### Scanning a Website by Hostname
You can scan ports on a target website by providing its hostname:
```python
import port_scanner

ports = port_scanner.get_open_ports("www.example.com", [70, 90])
print("Open ports:", ports)
```
**Output Example**:
```
Open ports: [80]
```

#### Scanning an IP Address with Verbose Mode
You can also scan an IP address with verbose output, which provides additional information about the open ports:
```python
ports = port_scanner.get_open_ports("192.168.1.1", [20, 100], True)
print(ports)
```
**Output Example**:
```
Open ports for 192.168.1.1
PORT     SERVICE
22       ssh
80       http
```

### 3. Running Unit Tests

The repository comes with built-in unit tests to verify the functionality of the port scanner. To run the tests, use the following command:
```bash
python main.py
```
This will execute the test cases and confirm that the port scanner behaves as expected.

### 4. Function Usage

#### `get_open_ports(target, port_range, verbose=False)`

- **Parameters**:
  - `target`: The IP address or hostname you want to scan.
  - `port_range`: A list containing the start and end of the port range (e.g., `[20, 80]`).
  - `verbose`: A boolean flag (`True` or `False`). If `True`, the function returns a detailed output with service names for each open port.

- **Returns**:
  - A list of open ports in non-verbose mode.
  - A detailed string with the open ports and their associated services in verbose mode.

#### Example

```python
open_ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print(open_ports)
```

**Output Example**:
```
Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http
```

## Error Handling

- **Invalid IP Address**: If an invalid IP address is provided (e.g., `266.255.9.10`), the function returns an error message:
  ```
  Error: Invalid IP address
  ```
  
- **Invalid Hostname**: If an unreachable or malformed hostname is provided (e.g., `scanme.nmap`), the function returns:
  ```
  Error: Invalid hostname
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

### Contributions

Feel free to fork the repository, create a branch, and submit pull requests for improvements, bug fixes, or new features. Make sure to write appropriate unit tests for new features or bug fixes.

---

### Contact

For any questions or issues, feel free to open an issue on GitHub or contact the repository maintainer.
```
