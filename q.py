import requests

# API key provided
access_key = 'oGrDqzQFdMs7DXFmnRtNgEqy'

# Fetch exchange rates
url = f'https://fcsapi.com/api-v3/forex/latest?symbol=all_forex&access_key=oGrDqzQFdMs7DXFmnRtNgEqy'
response = requests.get(url)

if response.status_code == 200:
    exchange_rates_data = response.json()
    
    # Print the entire JSON response to diagnose the structure
    print("Full response from API:", exchange_rates_data)
    
    if 'response' in exchange_rates_data:
        exchange_rates = exchange_rates_data['response']
        
        # Get user input for currency
        user_currency = input("Enter the currency: ").strip().upper()
        
        # Create a file name based on user input
        filename = f"{user_currency.lower()}_exchange_rates.txt"
        
        # Open the file for writing
        with open(filename, 'w') as file:
            for rate in exchange_rates:
                if rate['s'].startswith(user_currency):
                    other_currency = rate['s'].split('/')[1]
                    rate_value = rate['c']
                    file.write(f"{other_currency} - {rate_value}\n")
        
        print(f"Exchange rates written to {filename}")
    else:
        print("The response key is not present in the API response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response content:", response.text)
