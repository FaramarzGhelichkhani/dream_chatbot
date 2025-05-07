def dream_interpretation_parser(data: dict) -> str:
    label_map = {
        "emam_sadegh": "🔹 امام صادق (ع)",
        "ebn_sirin": "🔹 ابن سیرین",
        "danial": "🔹 دانیال نبی (ع)",
        "others": "🔹 سایر معبران",
        "summary": "🧾 جمع‌بندی"
    }

    parts = []
    if 'error' in data.keys():
        return data['error']
    
    for key in ["emam_sadegh", "ebn_sirin", "danial", "others", "summary"]:
        value = data.get(key, "یافت نشد").strip()
        label = label_map[key]
        parts.append(f"{label}:\n{value}")

    return "\n\n".join(parts)


# response = {
#     "emam_sadegh": "نشانه ایمان و صداقت است.",
#     "ebn_sirin": "نشان از رسیدن به مال حلال دارد.",
#     "danial": "یافت نشد",
#     "others": "ممکن است نشانه سفر باشد.",
#     "summary": "این خواب نمادی از موفقیت و پیشرفت است.",
#     "error": "لطفاً خواب خود را به‌صورت دقیق‌تر و با جزئیات بیشتری بنویسید تا بتوان آن را بر اساس منابع سنتی تعبیر کرد."  

# }

# message = format_dream_interpretation_emoji(response)
# print(message)
