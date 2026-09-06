import random


# =========================
# クイズ開始
# =========================

print("ようこそ都道府県クイズへ！")
print("このアプリでは、日本の都道府県に関するクイズを出題します。")
print("それでは、クイズを始めましょう！")

score = 0


# =========================
# 奈良県の問題データ
# =========================

from questions.nara import nara_questions

# =========================
# 大阪府の問題データ
# =========================

from questions.osaka import osaka_questions

# =========================
# 兵庫県の問題データ
# =========================

from questions.hyogo import hyogo_questions

# =========================
# 都道府県を選択
# =========================

while True:
    print("\n都道府県を選んでください")
    print("1. 奈良県")
    print("2. 大阪府")
    print("3. 兵庫県")

    prefecture_choice = input("番号を入力してください: ")

    if prefecture_choice == "1":
        questions = nara_questions
        break
    elif prefecture_choice == "2":
        questions = osaka_questions
        break
    elif prefecture_choice == "3":
        questions = hyogo_questions
        break
    else:
        print("1から3を入力してください。")
# =========================
# 難易度を選択
# =========================

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

# =========================
# 難易度で問題を絞り込む
# =========================

if selected_difficulty == 0:
    filtered_questions = questions
else:
    filtered_questions = [
        question for question in questions
        if question["difficulty"] == selected_difficulty
    ]

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
        print("1から3を入力してください。")

# =========================
# 問題をランダムに選択
# =========================

if quiz_count > len(filtered_questions):
    print(f"\n選択した難易度には{len(filtered_questions)}問しかないため、")
    print(f"{len(filtered_questions)}問出題します。")
    quiz_count = len(filtered_questions)

selected_questions = random.sample(filtered_questions, quiz_count)


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

percentage = score / (quiz_count * 10) * 100

print(f"\nクイズ終了！あなたのスコアは{score}点です。")
print(f"正答率は{percentage:.0f}%です。")

if percentage >= 80:
    print("合格です！次の都道府県に進みましょう！")
else:
    print("残念！もう一度挑戦してみてください！")