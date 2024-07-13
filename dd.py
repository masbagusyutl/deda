import time
import requests
import datetime
from itertools import cycle

# Function to read cookies from data.txt
def read_cookies_from_file(file_path):
    with open(file_path, 'r') as file:
        cookies = [line.strip() for line in file if line.strip()]
    return cookies

# Function to send POST request with a given cookie
def send_post_request(cookie):
    url = "https://deda-airdrop-nu.vercel.app/"
    headers = {
        'Cookie': cookie
    }
    response = requests.post(url, headers=headers)
    return response

# Function to display countdown
def countdown_timer(duration):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    while datetime.datetime.now() < end_time:
        remaining_time = end_time - datetime.datetime.now()
        print(f"Time remaining: {str(remaining_time).split('.')[0]}", end='\r')
        time.sleep(1)

# Main function to process accounts and handle the countdown
def process_accounts(file_path):
    cookies = read_cookies_from_file(file_path)
    num_accounts = len(cookies)
    print(f"Total accounts: {num_accounts}")

    cookie_cycle = cycle(cookies)
    
    while True:
        for index, cookie in enumerate(cookie_cycle, start=1):
            print(f"Processing account {index}/{num_accounts}")
            response = send_post_request(cookie)
            print(f"Status Code: {response.status_code}")
            time.sleep(5)
        
        print("All accounts processed. Starting 1-day countdown.")
        countdown_timer(86400)  # 86400 seconds = 1 day
        print("Countdown finished. Restarting the process.")

if __name__ == "__main__":
    process_accounts("data.txt")
