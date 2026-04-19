# ====== CHATBOT DINH DƯỠNG GIẢ LẬP (KHÔNG API) ======

def calculate_tdee(w, h, a, g):
    if g.lower() == "nam":
        return (10 * w) + (6.25 * h) - (5 * a) + 5
    else:
        return (10 * w) + (6.25 * h) - (5 * a) - 161


# ====== TRI THỨC GIẢ LẬP ======
knowledge = {
    "ức gà": "100g ức gà luộc chứa khoảng 31g protein.",
    "giảm cân": "Để giảm cân, bạn nên ăn ít calo hơn TDEE, tăng protein và tập luyện đều đặn.",
    "tăng cân": "Để tăng cân, bạn cần ăn nhiều hơn TDEE, ưu tiên thực phẩm giàu dinh dưỡng.",
    "protein": "Protein giúp xây dựng cơ bắp và rất quan trọng trong chế độ ăn."
}


# ====== CHATBOT ======
def chatbot_answer(question, tdee):
    question = question.lower()

    for key in knowledge:
        if key in question:
            return f"{knowledge[key]}\n👉 Dựa trên TDEE của bạn ({tdee:.0f}), hãy điều chỉnh khẩu phần phù hợp."

    return f"👉 Với TDEE {tdee:.0f} calo, bạn nên cân đối ăn uống hợp lý (carb, protein, fat) và duy trì lối sống lành mạnh."


# ====== MAIN ======
if __name__ == "__main__":
    print("=== CHATBOT DINH DƯỠNG (DEMO OFFLINE) ===")

    w = float(input("Nhập cân nặng (kg): "))
    h = float(input("Nhập chiều cao (cm): "))
    a = int(input("Nhập tuổi: "))
    g = input("Giới tính (nam/nu): ")

    tdee = calculate_tdee(w, h, a, g)

    print(f"\n👉 TDEE của bạn: {tdee:.2f} calo/ngày")

    while True:
        question = input("\nBạn hỏi gì? (thoát để dừng): ")

        if question.lower() == "thoát":
            print("Tạm biệt!")
            break

        answer = chatbot_answer(question, tdee)
        print("\n🤖 Chatbot:", answer)
