import json
import os
from scrape.scraper import fetch_schedule  # スクレイピング関数をインポート

PREVIOUS_DATA_FILE = "data/previous_data.json"

def load_previous_data():
    """
    前回のデータをJSONファイルから読み込む。
    ファイルが存在しない、または空の場合は空のリストを返す。
    """
    if os.path.exists(PREVIOUS_DATA_FILE):
        try:
            with open(PREVIOUS_DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # JSONが空の場合は空のリストを返す
            return []
    return []

def save_current_data(data):
    """
    今回のデータをJSONファイルに保存する。
    """
    with open(PREVIOUS_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def detect_updates(url):
    """
    URLから新しいデータを取得し、更新があればそれを検知する。

    Parameters:
        url (str): 予定を取得する対象のURL。

    Returns:
        list: 新しく追加されたデータのリスト。
    """
    # 前回のデータをロード
    previous_data = load_previous_data()

    # 今回のデータを取得
    current_data = fetch_schedule(url)

    # 更新を検知
    new_data = [item for item in current_data if item not in previous_data]

    # データを保存
    save_current_data(current_data)

    return new_data
