from logic import *


def main() -> None:
    """
    App point of entry
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()