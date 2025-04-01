import pytest
import mysql.connector

def test_subscription_date():
    """
    Test to ensure that when a new subscriber is added to the 'subscribers' table,
    the 'subscription_date' field is automatically set (i.e., not None).
    """
    # Establish a connection to the MySQL database using the specified credentials.
    conn = mysql.connector.connect(
        host='localhost',           # Database host
        user='flyway_user',         # Database username
        password='flyway_pass',     # Database password
        database='subscribers_db'   # Target database
    )
    
    # Create a cursor object to execute SQL queries.
    cursor = conn.cursor()
    
    try:
        # Insert a new record into the 'subscribers' table.
        # It is assumed that the table schema sets a default value or trigger for 'subscription_date'.
        insert_query = (
            "INSERT INTO subscribers (name, email) "
            "VALUES ('Vikas Rathore', 'vrathore@example.com')"
        )
        cursor.execute(insert_query)
        conn.commit()  # Commit the transaction to ensure the record is saved.
        
        # Retrieve the subscription_date for the inserted subscriber.
        select_query = (
            "SELECT subscription_date FROM subscribers "
            "WHERE email = 'vrathore@example.com'"
        )
        cursor.execute(select_query)
        subscription_date = cursor.fetchone()  # Fetch the first row from the result set.
        
        # Assert that the subscription_date is not None.
        # This ensures that the database automatically set a value for subscription_date.
        assert subscription_date is not None, "subscription_date should be set but was found to be None."
        
    finally:
        # Close the cursor and the connection to free up resources.
        cursor.close()
        conn.close()
