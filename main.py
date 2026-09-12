import random
# =========================
# 問題データ
# =========================
from questions.nara import nara_questions
from questions.osaka import osaka_questions
from questions.hyogo import hyogo_questions
from questions.kyoto import kyoto_questions
from questions.shiga import shiga_questions
from questions.wakayama import wakayama_questions
from questions.mie import mie_questions
# =========================
# 地方ごとの問題データ
# =========================

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

score = 0

# =========================
# ゲームモードを選択
# =========================

while True:
    print("\nゲームモードを選んでください")
    print("1. 都道府県選択")
    print("2. 地方制覇の旅")
    print("3. 日本一周制覇の旅")

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
    else:
        print("1から3の番号を入力してください。")

# =========================
# ゲームモードごとの処理
# =========================

if game_mode == "prefecture":

    # =========================
    # 都道府県を選択
    # =========================

    while True:
        print("\n都道府県を選んでください")
        print("1. 奈良県")
        print("2. 大阪府")
        print("3. 兵庫県")
        print("4. 京都府")
        print("5. 滋賀県")
        print("6. 和歌山県")
        print("7. 三重県")

        prefecture_choice = input("番号を入力してください: ")

        if prefecture_choice == "1":
            selected_prefecture = "奈良県"
            questions = nara_questions
            break
        elif prefecture_choice == "2":
            selected_prefecture = "大阪府"
            questions = osaka_questions
            break
        elif prefecture_choice == "3":
            selected_prefecture = "兵庫県"
            questions = hyogo_questions
            break
        elif prefecture_choice == "4":
            selected_prefecture = "京都府"
            questions = kyoto_questions
            break
        elif prefecture_choice == "5":
            selected_prefecture = "滋賀県"
            questions = shiga_questions
            break
        elif prefecture_choice == "6":
            selected_prefecture = "和歌山県"
            questions = wakayama_questions
            break
        elif prefecture_choice == "7":
            selected_prefecture = "三重県"
            questions = mie_questions
            break
        else:
            print("1から7を入力してください。")


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
            print("北海道地方は現在開発中です！")

        elif region_choice == "2":
            print("東北地方は現在開発中です！")

        elif region_choice == "3":
            print("関東地方は現在開発中です！")

        elif region_choice == "4":
            print("中部地方は現在開発中です！")

        elif region_choice == "5":
            selected_region = "近畿地方"
            questions = kinki_questions
            break

        elif region_choice == "6":
            print("中国地方は現在開発中です！")

        elif region_choice == "7":
            print("四国地方は現在開発中です！")

        elif region_choice == "8":
            print("九州・沖縄地方は現在開発中です！")

        else:
            print("1から8の番号を入力してください。")

    # =========================
    # 地方制覇の出題設定
    # =========================

    quiz_count = 30
    selected_questions = random.sample(questions, quiz_count)
     
elif game_mode == "japan":
    print("\n日本一周制覇の旅は現在開発中です！")
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


# =========================
# 結果発表
# =========================

correct_count = score // 10
percentage = correct_count / quiz_count * 100

print("\nクイズ終了！")
print(f"正解数は{correct_count} / {quiz_count}問です。")
print(f"正答率は{percentage:.0f}%です。")

if game_mode == "prefecture":

    if percentage >= 80:
        print(f"🎉 {selected_prefecture}合格です！")
    else:
        print(f"残念！{selected_prefecture}合格ならず！")
        print("もう一度挑戦してみてください！")

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