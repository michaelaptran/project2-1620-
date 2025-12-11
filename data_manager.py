import csv
import os

CSV_FILE = "data.csv"
header = ["Genre","Movie Title", "Where to watch", "Rating"]

def init_csv() -> None:
    """
    Initialize the csv file and establish the header

    """
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0: #Used tutorial to know how to use os module
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

def add_csv(genre:str, title:str, watch:str, rating: int) -> None:
    """
    Append a movie entry to the CSV file
    :param genre: A string representing the genre of the movie
    :param title: A string representing the title of the movie
    :param watch: A string representing the watch of the movie
    :param rating: A integer representing the rating of the movie

    """
    with open(CSV_FILE, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([genre, title, watch, rating])

def load_csv() -> list:
    """
    Loads all rows from the CSV file, excluding the header
    :return: A list of rows, each row is a list of strings
    """
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        return list(reader)

def save_csv(rows: list) -> None:
    """
    Saves rows to the CSV file, rewriting the entire file with the header
    :param rows: A list of rows from the csv file

    """
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

def search_csv(keyword:str) -> list:
    """
    Search the CSV file for rows containing the keyword
    :param keyword: A string representing the keyword of the movie
    :return: a list that contains the keyword
    """
    keyword = keyword.lower()
    rows = load_csv()
    result = []

    for row in rows:
        if any(keyword in col.lower() for col in row):
            result.append(row)

    return result

def remove_csv(keyword:str) -> list:
    """
    Remove rows from the CSV file that match a keyword
    :param keyword: A string representing the keyword of the movie
    :return: a list that contains the keyword, the removed movie
    """
    keyword = keyword.lower()
    rows = load_csv()
    result = []
    removed = []

    for row in rows:
        if any(keyword in col.lower() for col in row): #Use AI for how to implement any() for keyword
            removed.append(row)
        else:
            result.append(row)
    save_csv(result)
    return removed
