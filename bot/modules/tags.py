from sqlalchemy import select
from database.models import Tag
from database.session import Session

DEFAULT_TAGS = [
    {"name": "Геймер",      "name_uz": "Geymer",      "name_en": "Gamer",      "emoji": "🎮", "category": "Хобби"},
    {"name": "Аниме",       "name_uz": "Anime",        "name_en": "Anime",      "emoji": "🎌", "category": "Хобби"},
    {"name": "Спорт",       "name_uz": "Sport",        "name_en": "Sports",     "emoji": "⚽", "category": "Хобби"},
    {"name": "Музыка",      "name_uz": "Musiqa",       "name_en": "Music",      "emoji": "🎵", "category": "Хобби"},
    {"name": "Кино",        "name_uz": "Kino",         "name_en": "Movies",     "emoji": "🎬", "category": "Хобби"},
    {"name": "Книги",       "name_uz": "Kitoblar",     "name_en": "Books",      "emoji": "📚", "category": "Хобби"},
    {"name": "Путешествия", "name_uz": "Sayohat",      "name_en": "Travel",     "emoji": "✈️", "category": "Хобби"},
    {"name": "Фото",        "name_uz": "Foto",         "name_en": "Photo",      "emoji": "📸", "category": "Хобби"},
    {"name": "Рэп",         "name_uz": "Rep",          "name_en": "Rap",        "emoji": "🎤", "category": "Музыка"},
    {"name": "Рок",         "name_uz": "Rok",          "name_en": "Rock",       "emoji": "🤘", "category": "Музыка"},
    {"name": "Электронная", "name_uz": "Elektronika",  "name_en": "Electronic", "emoji": "🎧", "category": "Музыка"},
    {"name": "Художник",    "name_uz": "Rassom",       "name_en": "Artist",     "emoji": "🎨", "category": "Творчество"},
    {"name": "Программист", "name_uz": "Dasturchi",    "name_en": "Developer",  "emoji": "💻", "category": "Технологии"},
    {"name": "Косплей",     "name_uz": "Kosplay",      "name_en": "Cosplay",    "emoji": "🦸", "category": "Хобби"},
]


class TagModule:
    @staticmethod
    async def seed_tags():
        async with Session() as s:
            for tag_data in DEFAULT_TAGS:
                existing = await s.execute(
                    select(Tag).where(Tag.name == tag_data["name"])
                )
                tag = existing.scalar_one_or_none()
                if tag:
                    # обновляем переводы если уже есть
                    tag.name_uz = tag_data.get("name_uz")
                    tag.name_en = tag_data.get("name_en")
                else:
                    s.add(Tag(**tag_data))
            await s.commit()

    @staticmethod
    async def get_all_tags() -> list[Tag]:
        async with Session() as s:
            result = await s.execute(
                select(Tag).order_by(Tag.category, Tag.name)
            )
            return result.scalars().all()

    @staticmethod
    async def get_tags_by_ids(ids: list[int]) -> list[Tag]:
        async with Session() as s:
            result = await s.execute(
                select(Tag).where(Tag.id.in_(ids))
            )
            return result.scalars().all()

    @staticmethod
    def get_tag_name(tag: Tag, lang: str) -> str:
        """Вернуть имя тега на нужном языке."""
        if lang == "uz" and tag.name_uz:
            return tag.name_uz
        if lang == "en" and tag.name_en:
            return tag.name_en
        return tag.name
