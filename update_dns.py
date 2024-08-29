import requests
from dotenv import load_dotenv
import os
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

load_dotenv()

# Cloudflare API Token
api_token = os.getenv('CLOUDFLARE_API_TOKEN')
zone_id = os.getenv('CLOUDFLARE_ZONE_ID')

# 獲取當前公網 IP
public_ip = requests.get('https://api.ipify.org').text

# 要更新的域名列表
domains = ['www.junting.info', 'junting.info']

# 獲取所有 DNS 記錄
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    dns_records = response.json()['result']
    for domain in domains:
        record = next((rec for rec in dns_records if rec['name'] == domain), None)
        if record:
            record_id = record['id']
            update_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
            data = {
                "type": "A",
                "name": domain,
                "content": public_ip,
                "ttl": 1,  # 使用自動 TTL
                "proxied": True
            }
            update_response = requests.put(update_url, headers=headers, json=data)
            if update_response.status_code == 200:
                log_message(f"DNS record for {domain} updated to {public_ip}")
            else:
                log_message(f"Failed to update DNS record for {domain}: {update_response.json()}")
        else:
            log_message(f"Record ID for {domain} not found")
else:
    log_message(f"Failed to fetch DNS records: {response.status_code} - {response.text}")
