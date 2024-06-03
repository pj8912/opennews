import sqlite3

conn = sqlite3.connect('myn.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()



cursor.execute("""
CREATE TABLE rss_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    rss_link VARCHAR(255) NOT NULL,
    category_id INT,
    language_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (language_id) REFERENCES languages(id)
);
""")


cursor.execute("""
CREATE TABLE categories (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")


cursor.execute("""
CREATE TABLE languages (
    id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    language_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")


cursor.execute("""
CREATE TABLE saved_news (
    id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    news_title VARCHAR(255) NOT NULL,
    news_short TEXT,
    source_name VARCHAR(255),
    source_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")


cursor.execute("""
CREATE TABLE your_feed (
    id SERIAL PRIMARY KEY,
    rss_link_id INT,
    category_id INT,
    language_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rss_link_id) REFERENCES rss_links(id),
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (language_id) REFERENCES languages(id)
);
""")

cursor.close()
conn.close()
