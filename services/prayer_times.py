# services/prayer_times.py

import httpx

def get_prayer_times(city, country):
    # Aladhan API endpoint
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    
    try:
        # Make the initial request
        response = httpx.get(url)
        
        # If the response is a redirect, follow the new URL
        if response.status_code == 302:
            redirected_url = response.headers["Location"]
            response = httpx.get(redirected_url)
        
        # Raise error if response is not OK
        response.raise_for_status()
        
        # Parse the JSON data
        data = response.json()

        # Check if the data is valid
        if data["code"] == 200:
            return data["data"]["timings"]
        else:
            return None
    except httpx.RequestError as e:
        print(f"Error fetching prayer times: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code} - {e.response.text}")
        return None