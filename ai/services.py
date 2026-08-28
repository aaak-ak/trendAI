import os
import openai

# API ключ беремо з .env
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_description(title: str) -> str:
    """Обгортка для generate_captions — повертає перший опис"""
    captions = generate_captions(title, count=1)
    return captions[0] if captions else ""


def generate_hook(title: str) -> str:
    """Обгортка для generate_hooks — повертає перший хук"""
    hooks = generate_hooks(title, count=1)
    return hooks[0] if hooks else ""


def generate_hashtags(title: str) -> list[str]:
    """Генерація хештегів"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Зроби список хештегів для: {title}"}]
        )
        text = response.choices[0].message["content"]
        return [tag.strip() for tag in text.split() if tag.startswith("#")]
    except Exception as e:
        return [f"#error: {e}"]


def generate_captions(title: str, count: int = 5) -> list[str]:
    """Генерація описів продукту"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Зроби {count} варіантів описів для: {title}. Дай список по одному рядку"}]
        )
        text = response.choices[0].message["content"]
        return [line.strip("-• ") for line in text.split("\n") if line.strip()]
    except Exception as e:
        return [f"Помилка генерації описів: {e}"]


def generate_hooks(title: str, count: int = 10) -> list[str]:
    """Генерація рекламних хуків"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Зроби {count} рекламних хук для: {title}. Дай список по одному рядку"}]
        )
        text = response.choices[0].message["content"]
        return [line.strip("-• ") for line in text.split("\n") if line.strip()]
    except Exception as e:
        return [f"Помилка генерації хуків: {e}"]


def generate_scripts(title: str, count: int = 3) -> list[str]:
    """Генерація коротких рекламних сценаріїв"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Напиши {count} коротких рекламних сценаріїв для: {title}. Дай список по одному рядку"}]
        )
        text = response.choices[0].message["content"]
        return [line.strip("-• ") for line in text.split("\n") if line.strip()]
    except Exception as e:
        return [f"Помилка генерації сценаріїв: {e}"]



