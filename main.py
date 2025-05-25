from setup_database import connect_database, clear_database, queries
import json
import argparse

def compute_collatz_sequences(start, end, conn, cursor):
    data_to_insert = []

    for i in range(start, end + 1):
        number = i
        steps = [number]

        while number != 1:
            if number % 2 == 0: # if number is even
                number = number // 2
            else: # if number is odd
                number = 3 * number + 1
            steps.append(number)

        steps_json = json.dumps(steps) # convert steps to JSON string for database insertion
        step_count = len(steps) - 1
        max_value = max(steps)

        # collect data in memory for batch insertion
        data_to_insert.append((i, steps_json, step_count, max_value))

    # insert all records into the database in a single batch
    cursor.executemany(
        "INSERT INTO collatz (number, steps, step_count, max_value) VALUES (?, ?, ?, ?)", data_to_insert
    )
    conn.commit()

def main():
    # parse args, setup database, compute sequences, and show summary
    parser = argparse.ArgumentParser(description="Compute Collatz conjecture sequences and store results in SQLite DB.")
    parser.add_argument("start", type=int, help="Start of the range (inclusive), positive integer > 0")
    parser.add_argument("end", type=int, help="End of the range (inclusive), positive integer ≥ start")

    args = parser.parse_args()

    if args.start < 1 or args.end < 1:
        print("Both start and end values must be positive integers greater than 0.")
        return

    if args.start > args.end:
        print("The start value must be less than or equal to end value.")
        return

    conn = connect_database()
    cursor = conn.cursor()
    clear_database() # automatically clear the database at the start of every run

    compute_collatz_sequences(args.start, args.end, conn, cursor)
    queries()

    conn.close()

if __name__ == "__main__":
    main()
