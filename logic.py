from PyQt6.QtWidgets import *
from gui import *
import data_manager

class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        """
        Function initialization, sets up main window and button clicks

        :return: None
        """
        super().__init__()
        self.setupUi(self)

        data_manager.init_csv()


        self.button_add.clicked.connect(self.add_button)
        self.button_remove.clicked.connect(self.remove_button)
        self.button_clear.clicked.connect(self.clear_button)
        self.button_search.clicked.connect(self.search_button)

    def condition_check(self, genre: str, title: str, watch: str, rating: int) -> bool:
        """
        Checks if the user's input is valid

        :param genre: Movie genre provided by the user
        :param title: Movie title provided by the user
        :param watch: Where to watch the movie
        :param rating: rating of movie must be a integer
        :return: Returns True if the condition is satisfied, false otherwise
        """
        try:

            if genre == "" or title == "" or watch == "" or rating == "":
                self.label_error.setText("All fields are required")
                return False

            if not rating.isdigit():
                raise ValueError

        except ValueError:
                self.label_error.setText("Rating needs to be a number")
                return False

        return True


    def add_button(self) -> None:
        """
        Adds a movie entry to the CSV file after validation

        :return: None, if the condition_check not satisfied, the function exits early
        """
        try:
            genre = self.text_genre.text()
            title = self.text_movietitle.text()
            watch = self.text_watch.text()
            rating = self.text_rating.text()

            if not self.condition_check(genre, title, watch, rating):
                return

            data_manager.add_csv(genre, title, watch, rating)

            self.label_error.setText("Successfully added Movie")

        except Exception as e:
            self.label_error.setText("Error adding Movie")

    def search_button(self) -> None:
        """
        Search the CSV file for entries matching the keyword provided by the user

        :return: None. Displays results or errors in label_error
        """
        keyword = self.text_keyword.text().strip()

        if keyword == "":
            self.label_error.setText("Please enter a keyword")
            return

        results = data_manager.search_csv(keyword)

        if not results:
            self.label_error.setText("No results found")
            return

        answer = ""
        for row, col in enumerate(results):
            answer += f"{row+1}. Genre: {col[0]}, Title: {col[1]}, Where to watch: {col[2]}, Rating: {col[3]}\n"

        self.label_error.setText(f'Search results:\n{answer}')

    def clear_button(self) -> None:
        """
        Clear all input fields and error messages from the interface.

        :return: None
        """
        self.text_genre.clear()
        self.text_movietitle.clear()
        self.text_watch.clear()
        self.text_rating.clear()
        self.label_error.setText("")
        self.text_keyword.clear()

    def remove_button(self) -> None:
        """
        Remove movie entries from the CSV file that match a keyword
        :return: None. Displays removed entries or an error message
        """
        keyword = self.text_keyword.text().strip()

        if keyword == "":
            self.label_error.setText("Please enter a keyword")
            return

        removed = data_manager.remove_csv(keyword)
        answer = ""
        for row, col in enumerate(removed):
            answer += f"{row+1}. Genre: {col[0]}, Title: {col[1]}, Where to watch: {col[2]}, Rating: {col[3]}\n"

        if not removed:
            self.label_error.setText("No results found")
        else:
            self.label_error.setText(f"Successfully removed Movie containing:\n {answer}")
