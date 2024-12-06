import requests

def send_discord_notification(message, webhook_url):
    """
    Discordに通知を送信する関数。

    Parameters:
        message (str): 通知するメッセージ。
        webhook_url (str): DiscordのWebhook URL。
    """
    data = {
        "content": message  # Discordのメッセージ内容
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("通知を送信しました。")
        else:
            print(f"通知の送信に失敗しました: {response.status_code}")
    except Exception as e:
        print(f"通知の送信中にエラーが発生しました: {e}")
