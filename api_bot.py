# CYBERIX - API Automation Bot
import requests
from datetime import datetime

def get_live_data():
    # কলকাতার লাইভ আবহাওয়া ডেটা নেওয়ার জন্য ফ্রি API URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=22.57&longitude=88.36&current_weather=true"
    
    print("[*] CYBERIX: Fetching live data from API...")
    
    try:
        # requests লাইব্রেরি দিয়ে API-তে রিকোয়েস্ট পাঠানো
        response = requests.get(url)
        
        # যদি সার্ভার থেকে সফল রেসপন্স (Status Code 200) আসে
        if response.status_code == 200:
            data = response.json() # ডেটাকে JSON ফরম্যাটে কনভার্ট করা
            current = data['current_weather']
            
            temp = current['temperature']
            wind_speed = current['windspeed']
            
            # একটি প্রফেশনাল রিপোর্ট ফরম্যাট তৈরি করা
            report = f"\n========== CYBERIX API REPORT ==========\n"
            report += f"Timestamp  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            report += f"Location   : Kolkata Region, India\n"
            report += f"Temperature: {temp}°C\n"
            report += f"Wind Speed : {wind_speed} km/h\n"
            report += f"========================================\n"
            
            # স্ক্রিনে রিপোর্ট প্রিন্ট করা
            print(report)
            
            # অটোমেশনের আসল কাজ: রিপোর্টটি একটি টেক্সট ফাইলে অটোমেটিক সেভ (Append) করে রাখা
            with open("weather_log.txt", "a") as file:
                file.write(report + "\n")
                
            print("[+] Success: Live data recorded in 'weather_log.txt'")
            
        else:
            print(f"[-] Error: Server responded with code {response.status_code}")
            
    except Exception as e:
        print(f"[-] Connection Failed: {e}")

if __name__ == "__main__":
    get_live_data()
