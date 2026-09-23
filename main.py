import random
import json
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent / "progress.json"

# =========================
# 地方ごとの都道府県
# =========================

regions = {
    "北海道地方": [
        "北海道"
    ],
    "東北地方": [
        "青森県",
        "岩手県",
        "宮城県",
        "秋田県",
        "山形県",
        "福島県"
    ],
    "関東地方": [
        "茨城県",
        "栃木県",
        "群馬県",
        "埼玉県",
        "千葉県",
        "東京都",
        "神奈川県"
    ],
    "中部地方": [
        "新潟県",
        "富山県",
        "石川県",
        "福井県",
        "山梨県",
        "長野県",
        "岐阜県",
        "静岡県",
        "愛知県"
    ],
    "近畿地方": [
        "三重県",
        "滋賀県",
        "京都府",
        "大阪府",
        "兵庫県",
        "奈良県",
        "和歌山県"
    ],
    "中国地方": [
        "鳥取県",
        "島根県",
        "岡山県",
        "広島県",
        "山口県"
    ],
    "四国地方": [
        "徳島県",
        "香川県",
        "愛媛県",
        "高知県"
    ],
    "九州・沖縄地方": [
        "福岡県",
        "佐賀県",
        "長崎県",
        "熊本県",
        "大分県",
        "宮崎県",
        "鹿児島県",
        "沖縄県"
    ]
}


# =========================
# 問題データ
# =========================
from questions.hokkaido import hokkaido_questions
from questions.aomori import aomori_questions
from questions.iwate import iwate_questions
from questions.miyagi import miyagi_questions
from questions.akita import akita_questions
from questions.yamagata import yamagata_questions
from questions.fukushima import fukushima_questions
from questions.ibaraki import ibaraki_questions
from questions.tochigi import tochigi_questions
from questions.gunma import gunma_questions
from questions.saitama import saitama_questions
from questions.nara import nara_questions
from questions.osaka import osaka_questions
from questions.hyogo import hyogo_questions
from questions.kyoto import kyoto_questions
from questions.shiga import shiga_questions
from questions.wakayama import wakayama_questions
from questions.mie import mie_questions

# =========================
# 都道府県ごとの問題データ
# =========================
prefecture_questions = {
    "北海道": hokkaido_questions,
    "青森県": aomori_questions,
    "岩手県": iwate_questions,
    "宮城県": miyagi_questions,
    "秋田県": akita_questions,
    "山形県": yamagata_questions,
    "福島県": fukushima_questions,
    "茨城県": ibaraki_questions,
    "栃木県": tochigi_questions,
    "群馬県": gunma_questions,
    "埼玉県": saitama_questions,
    "三重県": mie_questions,
    "滋賀県": shiga_questions,
    "京都府": kyoto_questions,
    "大阪府": osaka_questions,
    "兵庫県": hyogo_questions,
    "奈良県": nara_questions,
    "和歌山県": wakayama_questions,
}

# =========================
# 地方ごとの問題データ
# =========================
tohoku_questions = (
    aomori_questions
    + iwate_questions
    + miyagi_questions
    + akita_questions
    + yamagata_questions
    + fukushima_questions
)

kinki_questions = (
    nara_questions
    + osaka_questions
    + hyogo_questions
    + kyoto_questions
    + shiga_questions
    + wakayama_questions
    + mie_questions
)
# =========================
# クイズ開始
# =========================

print("ようこそ都道府県クイズへ！")
print("このアプリでは、日本の都道府県に関するクイズを出題します。")
print("それでは、クイズを始めましょう！")

# =========================
# プレイ記録を読み込む
# =========================

try:
    with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
        progress = json.load(file)

except FileNotFoundError:
    progress = {}

score = 0

# =========================
# ゲームモードを選択
# =========================

while True:
    print("\nゲームモードを選んでください")
    print("1. 都道府県選択")
    print("2. 地方制覇の旅")
    print("3. 日本一周制覇の旅")
    print("4. 制覇状況を見る")

    mode_choice = input("番号を入力してください: ")

    if mode_choice == "1":
        game_mode = "prefecture"
        break
    elif mode_choice == "2":
        game_mode = "region"
        break
    elif mode_choice == "3":
        game_mode = "japan"
        break
    elif mode_choice == "4":
        game_mode = "view_progress"
        break
    else:
        print("1から4の番号を入力してください。")

# =========================
# ゲームモードごとの処理
# =========================

if game_mode == "prefecture":
    print("\n地方を選択してください！")

    region_list = list(regions.keys())

    for i, region in enumerate(region_list, 1):
        print(f"{i}. {region}")

    while True:
        region_choice = input("地方を番号で選択してください: ")

        if region_choice.isdigit():
            region_number = int(region_choice)

            if 1 <= region_number <= len(region_list):
                selected_region = region_list[region_number - 1]
                break

        print(f"1から{len(region_list)}の番号を入力してください。")

    print(f"\n{selected_region}を選択しました！")
    print(f"\n{selected_region}の都道府県を選択してください！")

    prefecture_list = regions[selected_region]

    for i, prefecture in enumerate(prefecture_list, 1):
        print(f"{i}. {prefecture}")

    while True:
        prefecture_choice = input("都道府県を番号で選択してください: ")

        if prefecture_choice.isdigit():
            prefecture_number = int(prefecture_choice)

            if 1 <= prefecture_number <= len(prefecture_list):
                selected_prefecture = prefecture_list[prefecture_number - 1]
                break

        print(f"1から{len(prefecture_list)}の番号を入力してください。")

    print(f"\n{selected_prefecture}を選択しました！")
    if selected_prefecture in prefecture_questions:
        questions = prefecture_questions[selected_prefecture]
    else:
        print("この都道府県の問題はまだ準備中です！")
        exit()


    # =========================
    # 難易度・カテゴリを選択
    # =========================

    while True:

        # 難易度
        while True:
            print("\n難易度を選んでください")
            print("1. ⭐ はじめて")
            print("2. ⭐⭐ ものしり")
            print("3. ⭐⭐⭐ ご当地博士")
            print("4. すべての難易度")

            difficulty_choice = input("番号を入力してください: ")

            if difficulty_choice == "1":
                selected_difficulty = 1
                break
            elif difficulty_choice == "2":
                selected_difficulty = 2
                break
            elif difficulty_choice == "3":
                selected_difficulty = 3
                break
            elif difficulty_choice == "4":
                selected_difficulty = 0
                break
            else:
                print("1から4の番号を入力してください。")


        # カテゴリ
        while True:
            print("\nカテゴリを選んでください")
            print("1. すべて")
            print("2. 地理・自然")
            print("3. 歴史")
            print("4. 観光・名所")
            print("5. 食・特産品")
            print("6. 文化・伝統")
            print("7. 産業・暮らし")

            category_choice = input("番号を入力してください: ")

            if category_choice == "1":
                selected_category = "すべて"
                break
            elif category_choice == "2":
                selected_category = "地理・自然"
                break
            elif category_choice == "3":
                selected_category = "歴史"
                break
            elif category_choice == "4":
                selected_category = "観光・名所"
                break
            elif category_choice == "5":
                selected_category = "食・特産品"
                break
            elif category_choice == "6":
                selected_category = "文化・伝統"
                break
            elif category_choice == "7":
                selected_category = "産業・暮らし"
                break
            else:
                print("1から7の番号を入力してください。")


        # 難易度で絞り込み
        if selected_difficulty == 0:
            filtered_questions = questions
        else:
            filtered_questions = [
                question for question in questions
                if question["difficulty"] == selected_difficulty
            ]


        # カテゴリで絞り込み
        if selected_category != "すべて":
            filtered_questions = [
                question for question in filtered_questions
                if question["category"] == selected_category
            ]


        if len(filtered_questions) == 0:
            print("\n選択した条件に当てはまる問題がありません。")
            print("難易度とカテゴリを選び直してください。")
        else:
            break


    # =========================
    # 出題数を選択
    # =========================

    print("\n何問挑戦しますか？")
    print("1. 5問")
    print("2. 10問")

    while True:
        quiz_choice = input("番号を入力してください: ")

        if quiz_choice == "1":
            quiz_count = 5
            break
        elif quiz_choice == "2":
            quiz_count = 10
            break
        else:
            print("1から2を入力してください。")


    if quiz_count > len(filtered_questions):
        print(f"\n選択した条件には{len(filtered_questions)}問しかないため、")
        print(f"{len(filtered_questions)}問出題します。")
        quiz_count = len(filtered_questions)

    selected_questions = random.sample(filtered_questions, quiz_count)
            
elif game_mode == "region":

    # =========================
    # 地方を選択
    # =========================

    while True:
        print("\n地方を選んでください")
        print("1. 北海道地方")
        print("2. 東北地方")
        print("3. 関東地方")
        print("4. 中部地方")
        print("5. 近畿地方")
        print("6. 中国地方")
        print("7. 四国地方")
        print("8. 九州・沖縄地方")

        region_choice = input("番号を入力してください: ")

        if region_choice == "1":
           selected_region = "北海道地方"
           break

        elif region_choice == "2":
            selected_region = "東北地方"
            break

        elif region_choice == "3":
            selected_region = "関東地方"
            break

        elif region_choice == "4":
            selected_region = "中部地方"
            break

        elif region_choice == "5":
            selected_region = "近畿地方"
            break

        elif region_choice == "6":
            selected_region = "中国地方"
            break

        elif region_choice == "7":
            selected_region = "四国地方"
            break

        elif region_choice == "8":
            selected_region = "九州・沖縄地方"
            break

        else:
            print("1から8の番号を入力してください。")

    # =========================
    # 地方制覇の出題設定
    # =========================

    quiz_count = 30
    selected_questions = []

    # 選択した地方の都道府県を取得
    region_prefectures = regions[selected_region]

    # 選択した地方の全問題を入れるリスト
    region_questions = []

    # 各都道府県から最低2問ずつ選ぶ
    for prefecture in region_prefectures:
        questions = prefecture_questions[prefecture]

        selected_questions += random.sample(questions, 2)
        region_questions += questions

    # 残りの問題数を計算
    remaining_count = quiz_count - len(selected_questions)

    # すでに選ばれた問題を除外
    remaining_questions = [
        question for question in region_questions
        if question not in selected_questions
]

    # 残りを地方全体からランダムに選択
    selected_questions += random.sample(
        remaining_questions,
        remaining_count
)

    # 出題順をランダムにする
    random.shuffle(selected_questions)
     
elif game_mode == "japan":
    print("\n日本一周制覇の旅は現在開発中です！")
    exit()

elif game_mode == "view_progress":
    print("\n===== 🗾 制覇状況 =====")

    total_cleared = 0
    total_available = 0

    for region, prefectures in regions.items():

        # 問題が完成している都道府県だけ取り出す
        available_prefectures = [
            prefecture for prefecture in prefectures
            if prefecture in prefecture_questions
        ]

        # まだ問題が1県もない地方は表示しない
        if len(available_prefectures) == 0:
            continue

        print(f"\n【{region}】")

        region_cleared = 0

        for prefecture in available_prefectures:
            data = progress.get(prefecture, {})

            if data.get("cleared"):
                best_score = data.get("best_score", 0)
                print(f"✅ {prefecture}：制覇　BEST {best_score:.0f}%")
                region_cleared += 1
            else:
                print(f"⬜ {prefecture}：未制覇")

        print(
            f"{region}制覇："
            f"{region_cleared} / {len(available_prefectures)}"
        )

        total_cleared += region_cleared
        total_available += len(available_prefectures)

    print(f"\n🗾 全国制覇：{total_cleared} / {total_available}")

    exit()


# =========================
# クイズを出題
# =========================

for i, question in enumerate(selected_questions, 1):

    print(f"\n問題{i}: {question['question']}")

    # 元の選択肢を変更しないようにコピーする
    shuffled_choices = question["choices"].copy()

    # 選択肢をランダムに並び替える
    random.shuffle(shuffled_choices)

    for number, choice in enumerate(shuffled_choices, 1):
        print(f"{number}. {choice}")

    while True:
        answer = input("答えを番号で入力してください（1-4）: ")

        if answer in ["1", "2", "3", "4"]:
            break
        else:
            print("1〜4の番号を入力してください。")

    # 正解が何番になったか調べる
    correct_number = shuffled_choices.index(question["answer"]) + 1

    if answer == str(correct_number):
        print("正解です！")
        score += 10
    else:
        print("不正解です。")
        print(f"正解は「{question['answer']}」です。")

    print(f"💡 解説：{question['explanation']}")

# =========================
# 結果発表
# =========================

correct_count = score // 10
percentage = correct_count / quiz_count * 100

print("\nクイズ終了！")
print(f"正解数は{correct_count} / {quiz_count}問です。")
print(f"正答率は{percentage:.0f}%です。")

if game_mode == "prefecture":
    old_best = progress.get(selected_prefecture, {}).get("best_score", 0)
    best_score = max(old_best, percentage)

    already_cleared = progress.get(selected_prefecture, {}).get("cleared", False)
    cleared = already_cleared or percentage >= 80
    if percentage >= 80:
        print(f"🎉 {selected_prefecture}合格です！")
    
    else:
        print(f"残念！{selected_prefecture}合格ならず！")
        print("もう一度挑戦してみてください！")
    progress[selected_prefecture] = {
        "cleared": cleared,
        "best_score": best_score
    }

    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(progress, file, ensure_ascii=False, indent=4)
    
elif game_mode == "region":

    if correct_count == quiz_count:
        print(f"🎉 {selected_region}制覇！おめでとうございます！")
    else:
        remaining = quiz_count - correct_count
        print(f"{selected_region}制覇ならず！")
        print(f"あと{remaining}問正解で制覇でした！")

elif game_mode == "japan":

    if correct_count == quiz_count:
        print("🎉 日本一周制覇！おめでとうございます！")
    else:
        remaining = quiz_count - correct_count
        print("日本一周制覇ならず！")
        print(f"あと{remaining}問正解で制覇でした！")