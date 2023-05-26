import schedule
import time
import pywhatkit

def send_message():
    # The hour and minute are based on a 24-hour time clock
    pywhatkit.sendwhatmsg("<phone number>", "Message Here!", 7, 15)

schedule.every().day.at("07:15").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
