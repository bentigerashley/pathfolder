import requests


api_key = 'h523hDtETbkJ3nSJL323hjYLXbCyDaRZ'
base_url = 'https://api.recruitment.shq.nz'

def get_domains(client_id):
    url = f"{base_url}/domains/{client_id}?api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()


def get_dns_records(zone_id):
    url = f"{base_url}/zones/{zone_id}?api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()


def main():
    client_id = 100  
    try:
        domains_data = get_domains(client_id)
        
    
        print("Domains Data:", domains_data)
        
        
        for domain in domains_data:
            domain_name = domain['name']
            print(f"Domain: {domain_name}")
            if 'zones' in domain:
                for zone in domain['zones']:
                    zone_id = zone['uri'].split('/')[-1]  
                    dns_records = get_dns_records(zone_id)
                    print(f"  Zone ID: {zone_id}")
                    for record in dns_records['records']:
                        print(f"    Record: {record}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
