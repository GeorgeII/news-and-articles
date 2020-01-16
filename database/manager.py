import psycopg2
import json

from model.article import Article


def save(model: Article):
    """
    First off, this function gets information from resources/database-config.json in order to connect to a database.
    Then the function save a model into the database.
    :param model: A model of type Article to store it into the database.
    """

    with open("resources/database-config.json") as f:
        db_info = json.load(f)

    try:
        connection = psycopg2.connect(user=db_info["user"],
                                      password=db_info["password"],
                                      host=db_info["host"],
                                      port=db_info["port"],
                                      database=db_info["database-name"])
        cursor = connection.cursor()

        query = """INSERT INTO article (headline, full_article, source, link, article_date)
                VALUES (%s, %s, %s, %s, %s)"""

        values_to_insert = (model.headline, model.full_article, model.source_name, model.link, model.article_date)
        cursor.execute(query, values_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into article table")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into article table", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
