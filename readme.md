# Cloudflare DDNS Updater

This project is a simple Python script that automatically updates the DNS records for specified domains in your Cloudflare account with your current public IP address. This is particularly useful for maintaining updated DNS records in a dynamic IP environment.

## Prerequisites

- Python 3.x
- [requests](https://pypi.org/project/requests/) - For making HTTP requests to the Cloudflare API.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For loading environment variables from a `.env` file.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/cloudflare-ddns.git
   cd cloudflare-ddns
   ```

2. Install the required Python packages using a virtual environmen

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Create a .env file in the root directory of the project and add your Cloudflare API token and Zone ID:

    ```
    CLOUDFLARE_API_TOKEN=your_cloudflare_api_token
    CLOUDFLARE_ZONE_ID=your_cloudflare_zone_id
    ```

4. Edit the domains list in the script to include the domains you want to update

## Usage

To run the script manually, execute:
```
source .venv/bin/activate
python3 update_ddns.py
```

### Setting Up a Cron Job

To automate the script execution, you can set up a cron job to run the script at regular intervals. Below is an example of how to set up a cron job that runs every 5 minutes.

1. Open your crontab file for editing:
`crontab -e`

2. Add the following line to the crontab file


`*/5 * * * * /path/to/your/project/cloudflare-ddns/.venv/bin/python /path/to/your/project/cloudflare-ddns/update_ddns.py >> /path/to/your/project/cloudflare-ddns/cron.log 2>&1
`

## Tutorial
For a step-by-step tutorial on how to find your Cloudflare Zone ID and API Token, you can refer to this [YouTube video](https://www.youtube.com/watch?v=_bJUFYDR2X4). Please note that the video demonstrates the process using a Shell script, but this project uses a more flexible Python script.