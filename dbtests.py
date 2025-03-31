import pytest
import mysql.connector

def test_subscription_date():
    conn = mysql.connector.connect(
        host='localhost',
        user='flyway_user',
        password='flyway_pass',
        database='subscribers_db'
    )
    cursor = conn.cursor()

    cursor.execute("INSERT INTO subscribers (name, email) VALUES ('Vikas Rathore', 'vrathore@example.com')")
    conn.commit()

    cursor.execute("SELECT subscription_date FROM subscribers WHERE email = 'vrathore@example.com'")
    subscription_date = cursor.fetchone()

    assert subscription_date is not None  # The subscription_date should not be None

    cursor.close()
    conn.close()
