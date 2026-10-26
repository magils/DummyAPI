import random

from django.utils import timezone
from django.utils.text import slugify

from dummy_data_app.generators.utils import random_date

NEWS_CATEGORIES = [
    "politics",
    "business",
    "technology",
    "sports",
    "health",
    "science",
    "entertainment",
    "world",
]
NEWS_COUNTRIES = ["US", "ES", "MX", "GB", "DE", "FR", "BR", "JP", "DO", "AR"]
NEWS_AUTHORS = [
    "Jane Smith",
    "Carlos Perez",
    "Amara Okafor",
    "Liam Chen",
    "Sofia Rossi",
    "Noah Muller",
]
NEWS_SOURCES = [
    "Daily Herald",
    "Global Times",
    "The Observer",
    "Tech Pulse",
    "Sports Wire",
    "Health Today",
]

HEADLINE_SUBJECTS = [
    "Government",
    "Local startup",
    "Scientists",
    "National team",
    "Central bank",
    "Researchers",
    "City council",
]
HEADLINE_VERBS = [
    "announces",
    "unveils",
    "reports",
    "rejects",
    "launches",
    "delays",
    "confirms",
]
HEADLINE_OBJECTS = [
    "new policy",
    "record growth",
    "major breakthrough",
    "budget plan",
    "surprise victory",
    "AI initiative",
    "climate agreement",
]

LOREM_SENTENCES = [
    "Officials said the decision followed months of review.",
    "Analysts expect the impact to be felt over the coming quarters.",
    "Critics questioned the timing of the announcement.",
    "The move comes amid growing public pressure.",
    "Further details are expected later this week.",
    "Experts described the outcome as largely unexpected.",
]


def _paragraph(sentences=4):
    return " ".join(random.choices(LOREM_SENTENCES, k=sentences))


def generate_news_item():
    title = f"{random.choice(HEADLINE_SUBJECTS)} {random.choice(HEADLINE_VERBS)} {random.choice(HEADLINE_OBJECTS)}"
    slug = f"{slugify(title)}-{random.randint(1000, 9999)}"
    source = random.choice(NEWS_SOURCES)

    return {
        "title": title,
        "slug": slug,
        "summary": _paragraph(2),
        "content": "\n\n".join(_paragraph(5) for _ in range(random.randint(3, 6))),
        "category": random.choice(NEWS_CATEGORIES),
        "author": random.choice(NEWS_AUTHORS),
        "source": source,
        "url": f"https://{slugify(source)}.example.com/{slug}",
        "country": random.choice(NEWS_COUNTRIES),
        "is_featured": random.random() < 0.15,
        "is_breaking": random.random() < 0.05,
        "published_at": timezone.make_aware(random_date(days_back=90)),
    }
