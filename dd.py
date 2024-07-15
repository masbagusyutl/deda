import time
import requests
import datetime

# Function to read cookies and baggage from data.txt
def read_cookies_and_baggage_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    cookies_and_baggage = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]
    return cookies_and_baggage

# Function to send POST request with a given cookie and baggage
def send_post_request(cookie, baggage):
    url = "https://deda-airdrop-nu.vercel.app/"
    headers = {
        'Cookie': cookie,
        'Baggage': baggage
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
    cookies_and_baggage = read_cookies_and_baggage_from_file(file_path)
    num_accounts = len(cookies_and_baggage)
    print(f"Total accounts: {num_accounts}")

    while True:
        for index, (cookie, baggage) in enumerate(cookies_and_baggage, start=1):
            print(f"Processing account {index}/{num_accounts}")
            response = send_post_request(cookie, baggage)
            print(f"Status Code: {response.status_code}")
            time.sleep(5)
        
        print("All accounts processed. Starting 1-day countdown.")
        countdown_timer(86400)  # 86400 seconds = 1 day
        print("Countdown finished. Restarting the process.")

if __name__ == "__main__":
    process_accounts("data.txt")
