import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "food_reviews.db")


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            confidence REAL NOT NULL,
            aspects TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.commit()
    connection.close()


def save_review(review_text, result):
    connection = get_connection()
    cursor = connection.execute(
        """
        INSERT INTO reviews (text, sentiment, confidence, aspects)
        VALUES (?, ?, ?, ?)
        """,
        (
            review_text,
            result["sentiment"],
            result["confidence"],
            result.get("aspects_json", "[]"),
        ),
    )
    connection.commit()
    review_id = cursor.lastrowid
    connection.close()
    return int(review_id)


def get_reviews():
    connection = get_connection()
    rows = connection.execute(
        """
        SELECT id, text, sentiment, confidence, aspects, created_at
        FROM reviews
        ORDER BY id DESC
        """
    ).fetchall()
    connection.close()

    return [dict(row) for row in rows]


def get_analytics():
    connection = get_connection()

    total_reviews = connection.execute(
        "SELECT COUNT(*) AS count FROM reviews"
    ).fetchone()["count"]

    rows = connection.execute(
        "SELECT sentiment, COUNT(*) AS count FROM reviews GROUP BY sentiment"
    ).fetchall()

    connection.close()

    counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for row in rows:
        if row["sentiment"] in counts:
            counts[row["sentiment"]] = row["count"]

    return {
        "total_reviews": total_reviews,
        "positive": counts["Positive"],
        "negative": counts["Negative"],
        "neutral": counts["Neutral"],
    }
