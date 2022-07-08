# fingerprint_pull

This script creates packets evenly for *nix platforms operating systems so that fingerprints can be generated from the receiving server.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/but-i-am-dominator/fingerprint_pull.git
   ```
2. From inside the directory; install the python prerequisites.
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure Firefox binary is present.
   ```sh
   sudo apt install firefox

   ```

### Usage

This script must be called with a required argument. You must add the desired URL/URI to the end of the command.

```sh
python crawl.py http://162.243.3.85:65000
```


### Requirements

For this script to run:
* Python 3
* Pip
* Python libraries listed in the requirements file.
* Firefox binary.


### Notes
Chrome does not have the acrhieved versions that Firefox has. Firefox was chosen as the browser platform. The firefox binary must be present for Selenium to work.

## Contact

David "Q" Quartarolo - [@d_quartarolo](https://twitter.com/d_quartarolo)

Project Link: [https://github.com/but-i-am-dominator/fingerprint_pull](https://github.com/but-i-am-dominator/fingerprint_pull)