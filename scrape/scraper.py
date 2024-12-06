import requests
from bs4 import BeautifulSoup

def fetch_schedule(url):
    """
    指定されたURLから予定データを取得する関数。

    Parameters:
        url (str): データを取得する対象のURL。

    Returns:
        list: 予定データのリスト。取得できない場合は空のリスト。
    """
    try:
        # ページを取得
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードが200以外の場合は例外を発生
        soup = BeautifulSoup(response.text, "html.parser")

        # テーブルを特定
        table = soup.find("table", class_="m_schenw")
        if not table:
            print("予定表が見つかりませんでした。")
            return []

        # テーブル内の行（<tr>）を抽出
        rows = table.find_all("tr")
        schedule = []

        # 各行のセル（<td>）からデータを取得
        for row in rows:
            cells = row.find_all("td")
            # セルが空の場合はスキップ
            if not cells or all(cell.get_text(strip=True) == "" for cell in cells):
                continue
            # データをリストとして追加
            schedule.append([cell.get_text(strip=True) for cell in cells])

        return schedule
    except Exception as e:
        print(f"データ取得中にエラーが発生しました: {e}")
        return []


