import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_gpt(prompt: str) -> str:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_description(title: str) -> str:

    try:

        prompt = f"""
        Create a short affiliate product description for:
        {title}
        """

        return ask_gpt(prompt)

    except Exception:

        if "Air Pump" in title:

            return (
                "Portable air compressor for cars, motorcycles "
                "and bicycles. A practical emergency tool that "
                "every driver should keep in the vehicle."
            )

        if "MagSafe" in title:

            return (
                "Strong magnetic phone holder for iPhone users. "
                "Perfect for work, travel and everyday use."
            )

        if "Fan" in title:

            return (
                "Portable cooling gadget designed for summer, "
                "travel and outdoor activities."
            )

        if "LED" in title:

            return (
                "Create a unique atmosphere with a stunning "
                "starry night projection effect."
            )

        return (
            f"{title} is a trending product with strong market "
            f"potential and social media appeal."
        )


def generate_hook(title: str) -> str:

    try:

        prompt = f"""
        Create a viral TikTok hook for:
        {title}
        """

        return ask_gpt(prompt)

    except Exception:

        if "Air Pump" in title:
            return "Every driver should keep this tool in the trunk."

        if "MagSafe" in title:
            return "This tiny gadget solves a problem every iPhone user has."

        if "Fan" in title:
            return "This gadget could become your summer essential."

        if "LED" in title:
            return "Your car interior will never look the same again."

        return f"You won't believe how useful this gadget is: {title}"


def generate_hashtags(title: str):

    try:

        prompt = f"""
        Generate 10 hashtags for:
        {title}

        Return only hashtags.
        """

        result = ask_gpt(prompt)

        return result.split()

    except Exception:

        if "Air Pump" in title:

            return [
                "#car",
                "#cars",
                "#driver",
                "#carlife",
                "#automotive",
                "#roadtrip",
                "#gadgets",
                "#musthave",
                "#viral",
                "#aliexpress"
            ]

        if "MagSafe" in title:

            return [
                "#iphone",
                "#magsafe",
                "#apple",
                "#tech",
                "#gadgets",
                "#viral",
                "#musthave",
                "#amazonfinds",
                "#shopping",
                "#aliexpress"
            ]

        if "Fan" in title:

            return [
                "#summer",
                "#fan",
                "#cooling",
                "#travel",
                "#gadgets",
                "#viral",
                "#shopping",
                "#musthave",
                "#tiktokmademebuyit",
                "#aliexpress"
            ]

        return [
            "#trend",
            "#viral",
            "#gadgets",
            "#shopping",
            "#aliexpress",
            "#amazonfinds",
            "#tiktokmademebuyit",
            "#deals",
            "#musthave",
            "#tech"
        ]


def generate_captions(title: str, count: int = 5):

    try:

        prompt = f"""
        Create {count} affiliate captions for:
        {title}
        """

        result = ask_gpt(prompt)

        return [
            line.strip()
            for line in result.split("\n")
            if line.strip()
        ]

    except Exception:

        return [
            f"Trending product: {title}",
            f"One of the most interesting gadgets this year.",
            f"Affordable and practical solution.",
            f"Perfect for everyday use.",
            f"Popular product with growing demand."
        ]


def generate_hooks(title: str, count: int = 10):

    try:

        prompt = f"""
        Create {count} viral marketing hooks for:
        {title}
        """

        result = ask_gpt(prompt)

        return [
            line.strip()
            for line in result.split("\n")
            if line.strip()
        ]

    except Exception:

        return [
            f"You won't believe this gadget: {title}",
            f"This product is going viral right now",
            f"One of the smartest purchases this year",
            f"Why is everyone buying this?",
            f"This could solve a daily problem"
        ]


def generate_scripts(title: str, count: int = 3):

    try:

        prompt = f"""
        Create {count} TikTok scripts for:
        {title}
        """

        result = ask_gpt(prompt)

        return [
            line.strip()
            for line in result.split("\n")
            if line.strip()
        ]

    except Exception:

        if "Air Pump" in title:

            return [
                "Low tire pressure? Plug in the air pump and inflate in minutes.",
                "Every driver should keep this emergency gadget in the trunk.",
                "A small tool that can save your entire road trip."
            ]

        if "MagSafe" in title:

            return [
                "Attach your iPhone instantly with MagSafe technology.",
                "No more unstable phone holders.",
                "Simple, strong and perfect for daily use."
            ]

        return [
            f"POV: You discovered {title} and wonder why you didn't buy it earlier.",
            f"This is how {title} makes life easier.",
            f"Here's why people are talking about {title}."
        ]