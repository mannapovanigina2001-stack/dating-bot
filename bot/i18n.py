"""
Все тексты бота на трёх языках: русский, узбекский, английский.
Использование:
    from bot.i18n import t
    text = t("welcome", lang)
    text = t("profile_caption", lang, name="Алишер", age=22, city="Ташкент")
"""

TEXTS = {

    # ── Общее ──────────────────────────────────────────────────────────────
    "choose_language": {
        "ru": "🌐 Выбери язык:",
        "uz": "🌐 Tilni tanlang:",
        "en": "🌐 Choose your language:",
    },
    "language_set_ru": {
        "ru": "✅ Язык изменён на Русский",
        "uz": "✅ Til ruscha qilib o'zgartirildi",
        "en": "✅ Language changed to Russian",
    },
    "language_set_uz": {
        "ru": "✅ Til o'zbekchaga o'zgartirildi",
        "uz": "✅ Til o'zbekchaga o'zgartirildi",
        "en": "✅ Language changed to Uzbek",
    },
    "language_set_en": {
        "ru": "✅ Язык изменён на Английский",
        "uz": "✅ Til inglizchaga o'zgartirildi",
        "en": "✅ Language changed to English",
    },

    # ── Регистрация ─────────────────────────────────────────────────────────
    "reg_welcome": {
        "ru": (
            "Привет! 👋\n\n"
            "Я помогу тебе найти собеседника или вторую половинку 💘\n\n"
            "Сначала выбери язык:"
        ),
        "uz": (
            "Salom! 👋\n\n"
            "Men senga do'st yoki sevgilini topishda yordam beraman 💘\n\n"
            "Avval tilni tanlang:"
        ),
        "en": (
            "Hello! 👋\n\n"
            "I'll help you find a friend or a special someone 💘\n\n"
            "First, choose your language:"
        ),
    },
    "reg_ask_name": {
        "ru": "Как тебя зовут? Введи имя:",
        "uz": "Ismingiz nima? Ismingizni kiriting:",
        "en": "What's your name? Enter your name:",
    },
    "reg_ask_gender": {
        "ru": "Отлично, {name}! Кто ты?",
        "uz": "Zo'r, {name}! Siz kimsiz?",
        "en": "Great, {name}! Who are you?",
    },
    "reg_ask_age": {
        "ru": "Сколько тебе лет?",
        "uz": "Yoshingiz nechida?",
        "en": "How old are you?",
    },
    "reg_age_error": {
        "ru": "Введи корректный возраст (14–100):",
        "uz": "To'g'ri yoshni kiriting (14–100):",
        "en": "Please enter a valid age (14–100):",
    },
    "reg_ask_city": {
        "ru": "Из какого ты города?",
        "uz": "Qaysi shahardasiz?",
        "en": "What city are you from?",
    },
    "reg_ask_photo": {
        "ru": "Загрузи своё фото 📸\n\nОно будет видно другим пользователям.",
        "uz": "Rasmingizni yuklang 📸\n\nBoshqa foydalanuvchilar uni ko'radi.",
        "en": "Upload your photo 📸\n\nOther users will be able to see it.",
    },
    "reg_photo_error": {
        "ru": "Пожалуйста, отправь фото, а не текст.",
        "uz": "Iltimos, matn emas, rasm yuboring.",
        "en": "Please send a photo, not text.",
    },
    "reg_ask_about": {
        "ru": "Расскажи немного о себе 📝\n\nИли напиши «-» чтобы пропустить:",
        "uz": "O'zingiz haqingizda qisqacha yozing 📝\n\nYoki o'tkazib yuborish uchun «-» yozing:",
        "en": "Tell us a bit about yourself 📝\n\nOr type «-» to skip:",
    },
    "reg_ask_looking": {
        "ru": "Кого ищешь?",
        "uz": "Kimni qidiryapsiz?",
        "en": "Who are you looking for?",
    },
    "reg_ask_tags": {
        "ru": "Выбери свои интересы 🎯\n\nМожно выбрать несколько. Нажми «Готово» когда закончишь:",
        "uz": "Qiziqishlaringizni tanlang 🎯\n\nBirnechtasini tanlash mumkin. Tugatgach «Tayyor» tugmasini bosing:",
        "en": "Choose your interests 🎯\n\nYou can select multiple. Press «Done» when finished:",
    },
    "reg_done": {
        "ru": (
            "🎉 Анкета создана, {name}!\n\n"
            "Теперь ты можешь смотреть анкеты других и знакомиться."
        ),
        "uz": (
            "🎉 Anketa yaratildi, {name}!\n\n"
            "Endi boshqalarning anketalarini ko'rib, tanishishingiz mumkin."
        ),
        "en": (
            "🎉 Profile created, {name}!\n\n"
            "Now you can browse other profiles and start meeting people."
        ),
    },
    "reg_already": {
        "ru": "Ты уже зарегистрирован! Используй меню ниже.",
        "uz": "Siz allaqachon ro'yxatdan o'tgansiz! Quyidagi menyudan foydalaning.",
        "en": "You're already registered! Use the menu below.",
    },
    "reg_cancelled": {
        "ru": "Регистрация отменена. Напиши /start чтобы начать заново.",
        "uz": "Ro'yxatdan o'tish bekor qilindi. Qaytadan boshlash uchun /start yozing.",
        "en": "Registration cancelled. Type /start to begin again.",
    },

    # ── Кнопки регистрации ──────────────────────────────────────────────────
    "btn_male": {
        "ru": "👨 Парень",
        "uz": "👨 Yigit",
        "en": "👨 Guy",
    },
    "btn_female": {
        "ru": "👩 Девушка",
        "uz": "👩 Qiz",
        "en": "👩 Girl",
    },
    "btn_looking_male": {
        "ru": "👨 Парней",
        "uz": "👨 Yigitlar",
        "en": "👨 Guys",
    },
    "btn_looking_female": {
        "ru": "👩 Девушек",
        "uz": "👩 Qizlar",
        "en": "👩 Girls",
    },
    "btn_looking_all": {
        "ru": "🌈 Всех",
        "uz": "🌈 Barchasi",
        "en": "🌈 Everyone",
    },
    "btn_done": {
        "ru": "✔️ Готово",
        "uz": "✔️ Tayyor",
        "en": "✔️ Done",
    },
    "btn_back": {
        "ru": "◀️ Назад",
        "uz": "◀️ Orqaga",
        "en": "◀️ Back",
    },
    "btn_cancel": {
        "ru": "❌ Отмена",
        "uz": "❌ Bekor qilish",
        "en": "❌ Cancel",
    },
    "btn_skip": {
        "ru": "➡️ Пропустить",
        "uz": "➡️ O'tkazib yuborish",
        "en": "➡️ Skip",
    },

    # ── Главное меню (Reply-кнопки) ─────────────────────────────────────────
    "menu_browse": {
        "ru": "👀 Смотреть анкеты",
        "uz": "👀 Anketalarni ko'rish",
        "en": "👀 Browse Profiles",
    },
    "menu_search": {
        "ru": "🔍 Поиск",
        "uz": "🔍 Qidiruv",
        "en": "🔍 Search",
    },
    "menu_favorites": {
        "ru": "⭐ Избранные",
        "uz": "⭐ Sevimlilar",
        "en": "⭐ Favorites",
    },
    "menu_referral": {
        "ru": "🔗 Реферал",
        "uz": "🔗 Referal",
        "en": "🔗 Referral",
    },
    "menu_profile": {
        "ru": "👤 Мой профиль",
        "uz": "👤 Mening anketam",
        "en": "👤 My Profile",
    },

    # ── Главный экран (inline) ──────────────────────────────────────────────
    "home_text": {
        "ru": (
            "<b>Главное меню</b>\n\n"
            "👀 <b>Смотреть анкеты</b> — найди нового человека\n\n"
            "👤 <b>Мой профиль</b> — посмотри и отредактируй\n\n"
            "🙈 <b>Скрыть анкету</b> — временно исчезнуть из поиска\n\n"
            "⭐ <b>Premium</b> — будь в топе и найди быстрее"
        ),
        "uz": (
            "<b>Asosiy menyu</b>\n\n"
            "👀 <b>Anketalarni ko'rish</b> — yangi odam topish\n\n"
            "👤 <b>Mening anketam</b> — ko'rish va tahrirlash\n\n"
            "🙈 <b>Anketani yashirish</b> — qidiruvdan vaqtincha chiqish\n\n"
            "⭐ <b>Premium</b> — tepada bo'l, tezroq top"
        ),
        "en": (
            "<b>Main Menu</b>\n\n"
            "👀 <b>Browse Profiles</b> — find someone new\n\n"
            "👤 <b>My Profile</b> — view and edit\n\n"
            "🙈 <b>Hide Profile</b> — temporarily disappear from search\n\n"
            "⭐ <b>Premium</b> — be on top and find faster"
        ),
    },
    "btn_home_browse": {
        "ru": "👀 Смотреть анкеты",
        "uz": "👀 Anketalarni ko'rish",
        "en": "👀 Browse Profiles",
    },
    "btn_home_profile": {
        "ru": "👤 Мой профиль",
        "uz": "👤 Mening anketam",
        "en": "👤 My Profile",
    },
    "btn_home_hide": {
        "ru": "🙈 Скрыть анкету",
        "uz": "🙈 Anketani yashirish",
        "en": "🙈 Hide Profile",
    },
    "btn_home_premium": {
        "ru": "⭐ Получить Premium",
        "uz": "⭐ Premium olish",
        "en": "⭐ Get Premium",
    },
    "home_hidden": {
        "ru": "😔 Анкета скрыта. Чтобы снова появиться в поиске — напиши /start",
        "uz": "😔 Anketa yashirildi. Qidiruvga qaytish uchun /start yozing.",
        "en": "😔 Profile hidden. To appear in search again — type /start",
    },

    # ── Просмотр анкет ──────────────────────────────────────────────────────
    "browse_empty": {
        "ru": "😢 Анкеты закончились. Загляни позже — появятся новые!",
        "uz": "😢 Anketalar tugadi. Keyinroq qarang — yangilari paydo bo'ladi!",
        "en": "😢 No more profiles for now. Check back later — new ones will appear!",
    },
    "browse_caption": {
        "ru": "{boost}<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}\n\n🎯 Интересы: {tags}",
        "uz": "{boost}<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}\n\n🎯 Qiziqishlar: {tags}",
        "en": "{boost}<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}\n\n🎯 Interests: {tags}",
    },
    "browse_no_tags": {
        "ru": "не указаны",
        "uz": "ko'rsatilmagan",
        "en": "not specified",
    },
    "browse_verified": {
        "ru": "✅ Верифицирован",
        "uz": "✅ Tasdiqlangan",
        "en": "✅ Verified",
    },
    "btn_like": {
        "ru": "❤️",
        "uz": "❤️",
        "en": "❤️",
    },
    "btn_fav": {
        "ru": "⭐",
        "uz": "⭐",
        "en": "⭐",
    },
    "btn_skip_profile": {
        "ru": "👎",
        "uz": "👎",
        "en": "👎",
    },
    "btn_report": {
        "ru": "🚨",
        "uz": "🚨",
        "en": "🚨",
    },
    "like_sent": {
        "ru": "Лайк отправлен ❤️",
        "uz": "Layk yuborildi ❤️",
        "en": "Like sent ❤️",
    },
    "skipped": {
        "ru": "Пропущено 👎",
        "uz": "O'tkazib yuborildi 👎",
        "en": "Skipped 👎",
    },
    "match_notify": {
        "ru": "💘 Мэтч с <b>{name}</b>! Пиши: @{username}{common}",
        "uz": "💘 <b>{name}</b> bilan match! Yozing: @{username}{common}",
        "en": "💘 It's a match with <b>{name}</b>! Write: @{username}{common}",
    },
    "match_username_none": {
        "ru": "напрямую",
        "uz": "to'g'ridan-to'g'ri",
        "en": "directly",
    },
    "match_common_tags": {
        "ru": "\n\n🎯 Общие интересы: {tags}",
        "uz": "\n\n🎯 Umumiy qiziqishlar: {tags}",
        "en": "\n\n🎯 Common interests: {tags}",
    },

    # ── Жалобы ──────────────────────────────────────────────────────────────
    "report_choose": {
        "ru": "Выбери причину жалобы:",
        "uz": "Shikoyat sababini tanlang:",
        "en": "Choose the reason for your report:",
    },
    "report_sent": {
        "ru": "✅ Жалоба отправлена. Модератор рассмотрит её в ближайшее время.",
        "uz": "✅ Shikoyat yuborildi. Moderator uni ko'rib chiqadi.",
        "en": "✅ Report sent. A moderator will review it shortly.",
    },
    "report_reasons": {
        "ru": ["Фейк/мошенник", "Оскорбления", "Спам", "Несовершеннолетний", "Другое"],
        "uz": ["Soxta/firibgar", "Haqorat", "Spam", "Voyaga etmagan", "Boshqa"],
        "en": ["Fake/scammer", "Insults", "Spam", "Minor", "Other"],
    },

    # ── Профиль ─────────────────────────────────────────────────────────────
    "profile_caption": {
        "ru": (
            "<b>Твой профиль</b>\n\n"
            "👤 {name}, {age} — {city}\n"
            "{verified}\n"
            "🏆 Активность: {score} очков\n\n"
            "📝 {about}\n\n"
            "🎯 Интересы: {tags}"
        ),
        "uz": (
            "<b>Mening anketam</b>\n\n"
            "👤 {name}, {age} — {city}\n"
            "{verified}\n"
            "🏆 Faollik: {score} ball\n\n"
            "📝 {about}\n\n"
            "🎯 Qiziqishlar: {tags}"
        ),
        "en": (
            "<b>Your Profile</b>\n\n"
            "👤 {name}, {age} — {city}\n"
            "{verified}\n"
            "🏆 Activity: {score} points\n\n"
            "📝 {about}\n\n"
            "🎯 Interests: {tags}"
        ),
    },
    "profile_no_about": {
        "ru": "Описание не указано",
        "uz": "Tavsif kiritilmagan",
        "en": "No description provided",
    },
    "profile_no_tags": {
        "ru": "не выбраны",
        "uz": "tanlanmagan",
        "en": "not selected",
    },
    "profile_not_found": {
        "ru": "Сначала зарегистрируйся через /start",
        "uz": "Avval /start orqali ro'yxatdan o'ting",
        "en": "Please register first via /start",
    },
    "profile_hidden_by_user": {
        "ru": "🙈 Анкета скрыта от других пользователей",
        "uz": "🙈 Anketa boshqa foydalanuvchilardan yashirilgan",
        "en": "🙈 Profile is hidden from other users",
    },
    "btn_profile_edit":    {"ru": "✏️ Редактировать", "uz": "✏️ Tahrirlash",            "en": "✏️ Edit"},
    "btn_profile_photo":   {"ru": "📸 Сменить фото",  "uz": "📸 Rasmni o'zgartirish",   "en": "📸 Change Photo"},
    "btn_profile_preview": {"ru": "👀 Предпросмотр",  "uz": "👀 Ko'rib chiqish",         "en": "👀 Preview"},
    "btn_profile_delete":  {"ru": "🗑 Удалить анкету", "uz": "🗑 Anketani o'chirish",    "en": "🗑 Delete Profile"},
    "btn_profile_show":    {"ru": "👁 Показать анкету", "uz": "👁 Anketani ko'rsatish",  "en": "👁 Show Profile"},
    "btn_profile_verify":  {"ru": "📸 Верифицировать", "uz": "📸 Tasdiqlash",            "en": "📸 Verify"},

    "profile_edit_choose": {
        "ru": "Что хочешь изменить?",
        "uz": "Nimani o'zgartirmoqchisiz?",
        "en": "What would you like to change?",
    },
    "btn_edit_name":    {"ru": "👤 Имя",       "uz": "👤 Ism",             "en": "👤 Name"},
    "btn_edit_age":     {"ru": "🎂 Возраст",   "uz": "🎂 Yosh",            "en": "🎂 Age"},
    "btn_edit_city":    {"ru": "🌆 Город",     "uz": "🌆 Shahar",          "en": "🌆 City"},
    "btn_edit_about":   {"ru": "📝 О себе",    "uz": "📝 O'zim haqimda",   "en": "📝 About Me"},
    "btn_edit_tags":    {"ru": "🎯 Интересы",  "uz": "🎯 Qiziqishlar",     "en": "🎯 Interests"},
    "btn_edit_looking": {"ru": "🔍 Ищу кого",  "uz": "🔍 Kimni qidiraman", "en": "🔍 Looking For"},

    "edit_ask_name":    {"ru": "Введи новое имя:",         "uz": "Yangi ismingizni kiriting:",    "en": "Enter your new name:"},
    "edit_ask_age":     {"ru": "Введи новый возраст:",     "uz": "Yangi yoshingizni kiriting:",   "en": "Enter your new age:"},
    "edit_ask_city":    {"ru": "Введи новый город:",       "uz": "Yangi shahringizni kiriting:",  "en": "Enter your new city:"},
    "edit_ask_about":   {"ru": "Напиши о себе (или «-» чтобы убрать):", "uz": "O'zingiz haqingizda yozing (yoki «-» o'chirish uchun):", "en": "Write about yourself (or «-» to remove):"},
    "edit_ask_photo":   {"ru": "Отправь новое фото 📸",    "uz": "Yangi rasmingizni yuboring 📸", "en": "Send your new photo 📸"},
    "edit_ask_looking": {"ru": "Кого ищешь?",              "uz": "Kimni qidiryapsiz?",            "en": "Who are you looking for?"},
    "edit_saved":       {"ru": "✅ Сохранено!",            "uz": "✅ Saqlandi!",                  "en": "✅ Saved!"},
    "edit_age_error":   {"ru": "Введи корректный возраст (14–100):", "uz": "To'g'ri yoshni kiriting (14–100):", "en": "Please enter a valid age (14–100):"},

    "profile_delete_confirm": {
        "ru": "⚠️ Удалить анкету? Это действие необратимо.",
        "uz": "⚠️ Anketani o'chirasizmi? Bu amalni qaytarib bo'lmaydi.",
        "en": "⚠️ Delete your profile? This action is irreversible.",
    },
    "btn_delete_yes": {"ru": "🗑 Да, удалить", "uz": "🗑 Ha, o'chirish", "en": "🗑 Yes, delete"},
    "btn_delete_no":  {"ru": "◀️ Отмена",      "uz": "◀️ Bekor qilish", "en": "◀️ Cancel"},
    "profile_deleted": {
        "ru": "Анкета удалена. Напиши /start чтобы создать новую.",
        "uz": "Anketa o'chirildi. Yangi yaratish uchun /start yozing.",
        "en": "Profile deleted. Type /start to create a new one.",
    },

    # ── Верификация ─────────────────────────────────────────────────────────
    "verify_already": {
        "ru": "⏳ Заявка на верификацию уже отправлена, ожидай.",
        "uz": "⏳ Tasdiqlash so'rovi allaqachon yuborilgan, kuting.",
        "en": "⏳ Verification request already sent, please wait.",
    },
    "verify_request": {
        "ru": (
            "📸 <b>Верификация фото</b>\n\n"
            "Отправь видео-кружок (🔵) с твоим лицом.\n"
            "Это докажет что ты реальный человек.\n\n"
            "После проверки ты получишь значок ✅ на анкете."
        ),
        "uz": (
            "📸 <b>Foto tasdiqlash</b>\n\n"
            "Yuzingiz ko'rinadigan video-doira (🔵) yuboring.\n"
            "Bu siz haqiqiy odam ekanligingizni isbotlaydi.\n\n"
            "Tekshiruvdan so'ng anketangizda ✅ belgisi paydo bo'ladi."
        ),
        "en": (
            "📸 <b>Photo Verification</b>\n\n"
            "Send a video circle (🔵) showing your face.\n"
            "This will prove that you are a real person.\n\n"
            "After review you will receive a ✅ badge on your profile."
        ),
    },
    "verify_approved": {
        "ru": "✅ Верификация прошла успешно! На анкете теперь есть значок ✅",
        "uz": "✅ Tasdiqlash muvaffaqiyatli o'tdi! Anketada endi ✅ belgisi bor.",
        "en": "✅ Verification successful! Your profile now has a ✅ badge.",
    },
    "verify_rejected": {
        "ru": "❌ Верификация отклонена. Попробуй снова — отправь чёткое видео-кружок с лицом.",
        "uz": "❌ Tasdiqlash rad etildi. Qaytadan urinib ko'ring — aniq yuz ko'rinadigan video-doira yuboring.",
        "en": "❌ Verification rejected. Try again — send a clear video circle showing your face.",
    },

    # ── Верификация — статусы ────────────────────────────────────────────────
    "ver_none":     {"ru": "",                  "uz": "",                    "en": ""},
    "ver_pending":  {"ru": "⏳ На проверке",    "uz": "⏳ Tekshirilmoqda",  "en": "⏳ Pending review"},
    "ver_verified": {"ru": "✅ Верифицирован",  "uz": "✅ Tasdiqlangan",    "en": "✅ Verified"},
    "ver_rejected": {"ru": "❌ Отклонено",      "uz": "❌ Rad etildi",      "en": "❌ Rejected"},

    # ── Поиск ───────────────────────────────────────────────────────────────
    "search_premium_only": {
        "ru": "🔒 <b>Поиск</b> доступен только Premium пользователям.\n\nАктивируй подписку — нажми «⭐ Получить Premium»",
        "uz": "🔒 <b>Qidiruv</b> faqat Premium foydalanuvchilar uchun mavjud.\n\nObunani faollashtiring — «⭐ Premium olish» tugmasini bosing",
        "en": "🔒 <b>Search</b> is available for Premium users only.\n\nActivate your subscription — tap «⭐ Get Premium»",
    },
    "search_choose_mode": {
        "ru": "🔍 <b>Поиск</b>\n\nКак будем искать?",
        "uz": "🔍 <b>Qidiruv</b>\n\nQanday qidiramiz?",
        "en": "🔍 <b>Search</b>\n\nHow would you like to search?",
    },
    "btn_search_tag":  {"ru": "🏷 По тегу",   "uz": "🏷 Teg bo'yicha",    "en": "🏷 By tag"},
    "btn_search_city": {"ru": "🌆 По городу", "uz": "🌆 Shahar bo'yicha", "en": "🌆 By city"},
    "search_by_tag": {
        "ru": "🏷 <b>Поиск по тегу</b>\n\nВыбери интерес:",
        "uz": "🏷 <b>Teg bo'yicha qidiruv</b>\n\nQiziqishni tanlang:",
        "en": "🏷 <b>Search by tag</b>\n\nChoose an interest:",
    },
    "search_by_city": {
        "ru": "🌆 <b>Поиск по городу</b>\n\nВведи название города:",
        "uz": "🌆 <b>Shahar bo'yicha qidiruv</b>\n\nShahar nomini kiriting:",
        "en": "🌆 <b>Search by city</b>\n\nEnter the city name:",
    },
    "search_empty_tag": {
        "ru": "По тегу «{tag}» никого не найдено 😔",
        "uz": "«{tag}» tegi bo'yicha hech kim topilmadi 😔",
        "en": "No one found with tag «{tag}» 😔",
    },
    "search_empty_city": {
        "ru": "В городе «{city}» никого не найдено 😔",
        "uz": "«{city}» shahrida hech kim topilmadi 😔",
        "en": "No one found in «{city}» 😔",
    },
    "search_found_tag": {
        "ru": "🔍 По тегу <b>{tag}</b> найдено {count} человек:",
        "uz": "🔍 <b>{tag}</b> tegi bo'yicha {count} kishi topildi:",
        "en": "🔍 Found {count} people with tag <b>{tag}</b>:",
    },
    "search_found_city": {
        "ru": "🌆 В городе <b>{city}</b> найдено {count} человек:",
        "uz": "🌆 <b>{city}</b> shahrida {count} kishi topildi:",
        "en": "🌆 Found {count} people in <b>{city}</b>:",
    },

    # ── Избранное ────────────────────────────────────────────────────────────
    "favorites_empty": {
        "ru": "⭐ У тебя пока нет избранных.\n\nНажми ⭐ под любой анкетой чтобы добавить.",
        "uz": "⭐ Hali sevimlilaring yo'q.\n\nQo'shish uchun istalgan anketa ostidagi ⭐ tugmasini bosing.",
        "en": "⭐ You have no favorites yet.\n\nTap ⭐ under any profile to add one.",
    },
    "favorites_caption": {
        "ru": "⭐ <b>Избранные {current}/{total}</b>\n\n<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}",
        "uz": "⭐ <b>Sevimlilar {current}/{total}</b>\n\n<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}",
        "en": "⭐ <b>Favorites {current}/{total}</b>\n\n<b>{name}, {age}</b> — {city}\n{verified}\n\n{about}",
    },
    "fav_added":   {"ru": "Добавлено в избранное ⭐",  "uz": "Sevimlilarga qo'shildi ⭐",  "en": "Added to favorites ⭐"},
    "fav_already": {"ru": "Уже в избранном ⭐",        "uz": "Allaqachon sevimlilarda ⭐",  "en": "Already in favorites ⭐"},
    "fav_limit": {
        "ru": "Лимит {limit} анкет. Активируй Premium для безлимита ⭐",
        "uz": "Chegara {limit} ta anketa. Chegarasiz uchun Premium faollashtiring ⭐",
        "en": "Limit of {limit} profiles. Activate Premium for unlimited ⭐",
    },
    "fav_removed":  {"ru": "Удалено из избранного 🗑", "uz": "Sevimlilardan o'chirildi 🗑", "en": "Removed from favorites 🗑"},
    "fav_list_empty": {
        "ru": "⭐ Избранных больше нет.",
        "uz": "⭐ Sevimlilar endi yo'q.",
        "en": "⭐ No more favorites.",
    },
    "btn_fav_write":  {"ru": "💬 Написать", "uz": "💬 Yozish",     "en": "💬 Write"},
    "btn_fav_remove": {"ru": "🗑 Удалить",  "uz": "🗑 O'chirish",  "en": "🗑 Remove"},

    # ── Реферал ─────────────────────────────────────────────────────────────
    "referral_text": {
        "ru": (
            "🔗 <b>Реферальная программа</b>\n\n"
            "Приглашено друзей: <b>{invited}</b>\n"
            "До следующего буста: <b>{next_boost}</b> чел.{boost_active}\n\n"
            "За каждые <b>3 приглашения</b> твоя анкета получает\n"
            "<b>+7 дней буста</b> — чаще показывается другим ❤️\n\n"
            "Твоя ссылка:"
        ),
        "uz": (
            "🔗 <b>Referal dasturi</b>\n\n"
            "Taklif qilingan do'stlar: <b>{invited}</b>\n"
            "Keyingi bustgacha: <b>{next_boost}</b> kishi{boost_active}\n\n"
            "Har <b>3 ta taklif</b> uchun anketangiz\n"
            "<b>+7 kun bust</b> oladi — boshqalarga ko'proq ko'rinadi ❤️\n\n"
            "Sizning havolangiz:"
        ),
        "en": (
            "🔗 <b>Referral Program</b>\n\n"
            "Friends invited: <b>{invited}</b>\n"
            "Until next boost: <b>{next_boost}</b> people{boost_active}\n\n"
            "For every <b>3 invitations</b> your profile gets\n"
            "<b>+7 days of boost</b> — shown to others more often ❤️\n\n"
            "Your referral link:"
        ),
    },
    "referral_boost_active": {
        "ru": "\n⚡ <b>Буст активен</b> до {date}",
        "uz": "\n⚡ <b>Bust faol</b> {date} gacha",
        "en": "\n⚡ <b>Boost active</b> until {date}",
    },
    "btn_referral_share": {
        "ru": "📤 Поделиться ссылкой",
        "uz": "📤 Havolani ulashish",
        "en": "📤 Share Link",
    },
    "referral_invited": {
        "ru": "🎉 По твоей ссылке зарегистрировался новый пользователь!\nВсего приглашено: <b>{count}</b>{boost}",
        "uz": "🎉 Havolangiz orqali yangi foydalanuvchi ro'yxatdan o'tdi!\nJami taklif qilingan: <b>{count}</b>{boost}",
        "en": "🎉 A new user registered via your link!\nTotal invited: <b>{count}</b>{boost}",
    },
    "referral_boost_earned": {
        "ru": "\n🚀 Ты получил +{days} дней буста!",
        "uz": "\n🚀 Siz +{days} kun bust oldingiz!",
        "en": "\n🚀 You earned +{days} days of boost!",
    },

    # ── Premium ──────────────────────────────────────────────────────────────
    "premium_text": {
        "ru": (
            "⭐ <b>Premium подписка</b>\n\n"
            "• Анкета показывается первой в поиске\n"
            "• Поиск людей по тегу и городу\n"
            "• Безлимитное избранное\n"
            "• Значок ⭐ на профиле\n"
            "• Видишь кто тебя лайкнул\n\n"
            "Выбери тариф:"
        ),
        "uz": (
            "⭐ <b>Premium obuna</b>\n\n"
            "• Anketa qidiruvda birinchi ko'rsatiladi\n"
            "• Teg va shahar bo'yicha qidiruv\n"
            "• Chegarasiz sevimlilar\n"
            "• Profilda ⭐ belgisi\n"
            "• Kim layk bosganini ko'rasan\n\n"
            "Tarifni tanlang:"
        ),
        "en": (
            "⭐ <b>Premium Subscription</b>\n\n"
            "• Your profile appears first in search\n"
            "• Search people by tag and city\n"
            "• Unlimited favorites\n"
            "• ⭐ badge on your profile\n"
            "• See who liked you\n\n"
            "Choose a plan:"
        ),
    },
    "btn_premium_1m": {"ru": "⭐ 1 месяц — 30 000 сум",      "uz": "⭐ 1 oy — 30 000 so'm",       "en": "⭐ 1 month — 30 000 UZS"},
    "btn_premium_3m": {"ru": "⭐⭐ 3 месяца — 70 000 сум",   "uz": "⭐⭐ 3 oy — 70 000 so'm",      "en": "⭐⭐ 3 months — 70 000 UZS"},
    "btn_premium_1y": {"ru": "⭐⭐⭐ 1 год — 250 000 сум",   "uz": "⭐⭐⭐ 1 yil — 250 000 so'm",   "en": "⭐⭐⭐ 1 year — 250 000 UZS"},
   "premium_payment": {
    "ru": (
        "💳 <b>Оплата Premium — {label}</b>\n\n"
        "Сумма: <b>{price}</b>\n\n"
        "📍 <b>Номер карты:</b>\n<code>{card}</code>\n\n"
        "⚠️ <b>Инструкция:</b>\n"
        "1️⃣ Скопируй номер карты\n"
        "2️⃣ Переведи <b>{price}</b> на карту\n"
        "3️⃣ Сделай скриншот чека\n"
        "4️⃣ Нажми кнопку ниже и отправь скриншот\n\n"
        "⏳ Активация в течение 15 минут"
    ),
    "uz": (
        "💳 <b>Premium to'lovi — {label}</b>\n\n"
        "Summa: <b>{price}</b>\n\n"
        "📍 <b>Karta raqami:</b>\n<code>{card}</code>\n\n"
        "⚠️ <b>Ko'rsatma:</b>\n"
        "1️⃣ Karta raqamini nusxa oling\n"
        "2️⃣ <b>{price}</b> kartaga o'tkaring\n"
        "3️⃣ Chek skrinshotini oling\n"
        "4️⃣ Quyidagi tugmani bosib skrinshotni yuboring\n\n"
        "⏳ 15 daqiqa ichida faollashtirish"
    ),
    "en": (
        "💳 <b>Premium Payment — {label}</b>\n\n"
        "Amount: <b>{price}</b>\n\n"
        "Choose your payment method:\n\n"
        "💳 <b>Card (Uzbekistan):</b>\n<code>{card}</code>\n\n"
        "₿ <b>Bitcoin (BTC):</b>\n<code>bc1q43zu07n7mxzfv9235l0k2a39hnktgd8xt85gu5</code>\n\n"
        "⧫ <b>Ethereum (ETH):</b>\n<code>0xd4520a3a3290ebbdf608f4400a414e1117d4dbf7</code>\n\n"
        "⚠️ <b>Instructions:</b>\n"
        "1️⃣ Copy the address you want to pay to\n"
        "2️⃣ Send exactly <b>{price}</b>\n"
        "3️⃣ Take a screenshot of the transaction\n"
        "4️⃣ Press the button below and send the screenshot\n\n"
        "⏳ Activation within 15 minutes"
    ),
},
    "btn_pay_confirm": {
        "ru": "✅ Я оплатил — отправить чек",
        "uz": "✅ To'ladim — chekni yuborish",
        "en": "✅ I've paid — send receipt",
    },
    "premium_awaiting_receipt": {
        "ru": "📸 Отправьте скриншот чека об оплате.\n\nПосле проверки Premium будет активирован.",
        "uz": "📸 To'lov chekining skrinshotini yuboring.\n\nTekshiruvdan so'ng Premium faollashtiriladi.",
        "en": "📸 Send a screenshot of your payment receipt.\n\nPremium will be activated after verification.",
    },
    "premium_receipt_received": {
        "ru": "✅ Чек получен! Ожидайте активации в течение 15 минут.\n\nВопросы: @admin",
        "uz": "✅ Chek qabul qilindi! 15 daqiqa ichida faollashtirishni kuting.\n\nSavollar: @admin",
        "en": "✅ Receipt received! Please wait up to 15 minutes for activation.\n\nQuestions: @admin",
    },
    "premium_given": {
        "ru": "🎉 Вам выдан <b>Premium на {days} дней</b>! ⭐",
        "uz": "🎉 Sizga <b>{days} kunlik Premium</b> berildi! ⭐",
        "en": "🎉 You have been granted <b>Premium for {days} days</b>! ⭐",
    },

    # ── Онбординг ───────────────────────────────────────────────────────────
    "onboarding_1": {
        "ru": (
            "👀 <b>Как смотреть анкеты?</b>\n\n"
            "Нажми <b>«👀 Смотреть анкеты»</b> в меню.\n"
            "❤️ — лайк, 👎 — пропустить, ⭐ — в избранное, 🚨 — пожаловаться.\n\n"
            "Если оба поставят лайк — это мэтч! Вы сможете написать друг другу."
        ),
        "uz": (
            "👀 <b>Anketalarni qanday ko'rish?</b>\n\n"
            "Menyudagi <b>«👀 Anketalarni ko'rish»</b> tugmasini bosing.\n"
            "❤️ — layk, 👎 — o'tkazib yuborish, ⭐ — sevimlilarga, 🚨 — shikoyat.\n\n"
            "Ikkalangiz ham layk qo'ysangiz — bu match! Bir-biringizga yoza olasizlar."
        ),
        "en": (
            "👀 <b>How to browse profiles?</b>\n\n"
            "Tap <b>«👀 Browse Profiles»</b> in the menu.\n"
            "❤️ — like, 👎 — skip, ⭐ — add to favorites, 🚨 — report.\n\n"
            "If both of you like each other — it's a match! You'll be able to write to each other."
        ),
    },
    "onboarding_2": {
        "ru": (
            "⭐ <b>Premium — больше возможностей</b>\n\n"
            "С Premium твоя анкета показывается первой, "
            "можешь искать по городу и тегам, "
            "и видеть кто тебя лайкнул.\n\n"
            "Нажми «⭐ Получить Premium» в главном меню чтобы узнать подробнее."
        ),
        "uz": (
            "⭐ <b>Premium — ko'proq imkoniyatlar</b>\n\n"
            "Premium bilan anketangiz birinchi ko'rsatiladi, "
            "shahar va teg bo'yicha qidirish mumkin, "
            "va kim layk bosganini ko'rish mumkin.\n\n"
            "Batafsil ma'lumot uchun asosiy menyudagi «⭐ Premium olish» tugmasini bosing."
        ),
        "en": (
            "⭐ <b>Premium — more features</b>\n\n"
            "With Premium your profile is shown first, "
            "you can search by city and tags, "
            "and see who liked you.\n\n"
            "Tap «⭐ Get Premium» in the main menu to learn more."
        ),
    },

    # ── Блокировка ──────────────────────────────────────────────────────────
    "banned_message": {
        "ru": "⛔ Твой аккаунт заблокирован. Обратись к @admin если считаешь это ошибкой.",
        "uz": "⛔ Hisobingiz bloklangan. Xato deb hisoblasangiz @admin ga murojaat qiling.",
        "en": "⛔ Your account has been banned. Contact @admin if you think this is a mistake.",
    },

    # ── Обращение в поддержку ───────────────────────────────────────────────
    "complaint_start": {
        "ru": "🛡 <b>Обращение в поддержку</b>\n\nНапишите сообщение или отправьте скриншот.",
        "uz": "🛡 <b>Yordam markazi</b>\n\nXabaringizni yoki screenshot yuboring.",
        "en": "🛡 <b>Support</b>\n\nWrite a message or send a screenshot.",
    },
    "complaint_sent": {
        "ru": "✅ <b>Отправлено!</b>\n\nМы скоро рассмотрим 🙏",
        "uz": "✅ <b>Yuborildi!</b>\n\nTez orada ko'rib chiqamiz 🙏",
        "en": "✅ <b>Sent!</b>\n\nWe'll review it soon 🙏",
    },
    "cancel": {
        "ru": "❌ Отмена",
        "uz": "❌ Bekor qilish",
        "en": "❌ Cancel",
    },

    # ── Мэтчи ───────────────────────────────────────────────────────────────
    "no_matches": {
        "ru": "😔 У тебя пока нет мэтчей\n\nСмотри анкеты и ставь лайки!",
        "uz": "😔 Hali mos kelganlar yo'q\n\nProfil ko'rib layk bos!",
        "en": "😔 You have no matches yet\n\nBrowse profiles and start liking!",
    },
    "matches_title": {
        "ru": "💌 <b>Твои мэтчи:</b>",
        "uz": "💌 <b>Sizning mos kelganlaringiz:</b>",
        "en": "💌 <b>Your matches:</b>",
    },
    "match_item": {
        "ru": "• {name}, {age} — {city}",
        "uz": "• {name}, {age} — {city}",
        "en": "• {name}, {age} — {city}",
    },
    "write_to": {
        "ru": "✉️ Написать {name}",
        "uz": "✉️ Yozish {name}",
        "en": "✉️ Write to {name}",
    },
    "no_username": {
        "ru": "❌ Нет username",
        "uz": "❌ Username yo'q",
        "en": "❌ No username",
    },
}


def t(key: str, lang: str = "ru", **kwargs) -> str:
    """
    Получить текст по ключу и языку.
    Поддерживает форматирование: t("reg_done", lang, name="Алишер")
    """
    entry = TEXTS.get(key)
    if entry is None:
        return f"[MISSING: {key}]"

    # Если значение — список (например report_reasons) — вернуть список
    if isinstance(entry.get("ru"), list):
        return entry.get(lang, entry.get("ru"))

    text = entry.get(lang) or entry.get("ru") or f"[MISSING: {key}]"
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    return text
