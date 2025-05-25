import sqlite3

def connect_database():
    """Creates the database (if it doesn't exist) and returns the connection object."""
    conn = sqlite3.connect("collatz_conjecture.db")
    cursor = conn.cursor()

    # create the table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS collatz (
        number INTEGER PRIMARY KEY,
        steps TEXT,
        step_count INTEGER,
        max_value INTEGER
    )
    """)

    conn.commit()
    return conn

def clear_database():
    """Clears all records in the database for a fresh computation."""
    conn = sqlite3.connect('collatz_conjecture.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM collatz")
    conn.commit()

def format_large_number(n):
    """Formats large integers with commas or scientific notation if extremely large."""
    if n >= 10**9:
        return f"{n:.3e}" # scientific notation for very large numbers
    return f"{n:,}" # format with comma as thousands separator

def queries():
    """Performs key queries and prints summary statistics."""
    conn = sqlite3.connect("collatz_conjecture.db")
    cursor = conn.cursor()

    # get the minimum and maximum number in the database
    cursor.execute("SELECT MIN(number) FROM collatz")
    start = cursor.fetchone()[0]
    cursor.execute("SELECT MAX(number) FROM collatz")
    end = cursor.fetchone()[0]

    # find the max step_count
    cursor.execute("SELECT MAX(step_count) FROM collatz")
    max_step_count = cursor.fetchone()[0]

    # if there is more than one value that reaches the highest step count, fetch them all
    cursor.execute("""
        SELECT number, step_count, max_value FROM collatz
        WHERE step_count = ?
    """, (max_step_count,))

    results = cursor.fetchall()

    # print number(s) that reached the highest step count along with their details
    print(f"In the range {start} to {end}\n"
          f"Number(s) reaching the highest step count:")
    for number, step_count, max_value in results:
        print(f"Number: {number}\n"
              f"Step count: {step_count}\n"
              f"The highest value it has reached: {format_large_number(max_value)}\n")
    print("For detailed sequences, check the SQLite database file 'collatz_conjecture.db' using a DB viewer tool.")
