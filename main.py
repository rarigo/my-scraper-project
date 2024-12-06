from scrape.detect_updates import detect_updates
from scrape.notifier import send_discord_notification
from scrape.config import DISCORD_WEBHOOK_URL, TARGET_URL
import schedule
import time
import datetime

def check_updates():
    """
    ページをチェックし、新しい予定があれば通知を送信する。
    """
    print("ページをチェックしています...")  # 動作確認用ログ
    new_schedules = detect_updates(TARGET_URL)

    if new_schedules:
        print("新しい予定が検出されました:")
        for schedule_item in new_schedules:
            print(schedule_item)
            message = f"新しい予定: {schedule_item}\n詳細はこちら: {TARGET_URL}"
            send_discord_notification(message, DISCORD_WEBHOOK_URL)
    else:
        print("新しい予定はありません。（チェック時刻: "
              f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")  # ログを追加


def send_no_update_notification():
    """
    更新がなくても通知を送信する。
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"現在新しい予定はありません。\n詳細はこちら: {TARGET_URL}\n時刻: {current_time}"
    print("指定時刻通知:", message)
    send_discord_notification(message, DISCORD_WEBHOOK_URL)

# スケジュール設定
schedule.every(15).minutes.do(check_updates)  # 2分ごとにページをチェック
schedule.every().day.at("10:00").do(send_no_update_notification)  # 12:00の通知
schedule.every().day.at("12:00").do(send_no_update_notification)  # 12:00の通知
schedule.every().day.at("12:30").do(send_no_update_notification)  # 12:30の通知
schedule.every().day.at("13:00").do(send_no_update_notification)  # 13:00の通知
schedule.every().day.at("15:50").do(send_no_update_notification)  # 15:50の通知

if __name__ == "__main__":
    print("スケジュール通知を開始します...")
    while True:
        schedule.run_pending()
        time.sleep(1)
