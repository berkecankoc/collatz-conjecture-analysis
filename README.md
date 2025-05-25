# Collatz Conjecture Analysis

## About Collatz Conjecture

The Collatz Conjecture is a famous unsolved problem in mathematics. It involves taking any positive integer and repeatedly applying the following rules:

* If the number is even, divide it by 2.
* If the number is odd, multiply it by 3 and add 1.

This process is repeated for each new result.

The conjecture asserts that, no matter which positive integer you start with, the sequence will always eventually reach 1.

**Example:**

Starting with `6`, the sequence is: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

For more details: [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture), [MathWorld](https://mathworld.wolfram.com/CollatzProblem.html)

## Project Description

This project analyzes the **Collatz Conjecture** by computing sequences for numbers within a specified range and storing the results in a SQLite database.

## Features

- Processes numbers in a given range and calculates their Collatz sequences.
- Stores the sequence steps, step count, and maximum value reached for each number.
- Uses SQLite for lightweight, file-based data storage.
- Automatically clears existing data before every new computation.

## Database Schema

The SQLite database contains a single table named `collatz` with the following columns:

| Column      | Type    | Description                              |
|-------------|---------|------------------------------------------|
| `number`    | INTEGER | The original number (Primary Key)        |
| `steps`     | TEXT    | JSON-encoded list of sequence steps      |
| `step_count`| INTEGER | Number of steps taken to reach 1         |
| `max_value` | INTEGER | Maximum value reached during the sequence|

## Requirements

- Python 3.6 or higher
- Uses built-in modules: `sqlite3`, `json`, `argparse`

## Usage

Run the script with the start and end of the range as positional arguments:

```
python main.py <start> <end>
````

* `<start>`: Start of the range (inclusive), positive integer > 0 
* `<end>`: End of the range (inclusive), positive integer ≥ start

### Example
Compute sequences for numbers from 110 to 42,000 (database is cleared automatically at the start):

```
python main.py 110 42000
```

## Project Structure

```
.
├── main.py               # Main script to run computations
├── setup_database.py     # Database setup and utility functions
└── README.md             # Project documentation
```

## How It Works

1. The database is created (if it doesn’t exist) with the proper table.
2. Existing data is automatically cleared before each new computation.
3. For each number in the specified range:
   * The Collatz sequence is computed.
   * The number, steps, step count, and max value are stored.
4. After the computation, a summary query prints number(s) that reached the highest step count along with their details.

## Exploring the Database

The resulting `collatz_conjecture.db` file is a standard SQLite database and can be easily explored using tools like [DB Browser for SQLite](https://sqlitebrowser.org/dl/) or any other SQLite viewer.

---

Feel free to open issues or submit pull requests for improvements!

---

## License

This project is released under the MIT License.
