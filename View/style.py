style_sheet = """
    /* Dark Mode Style */

    /* Application background */
    QMainWindow {
        background-color: #222222;
        color: #ffffff;
    }

    /* QPushButton */
    QPushButton {
        background-color: #444444;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 8px;
    }
    QPushButton:hover {
        background-color: #666666;
    }
    QPushButton:pressed {
        background-color: #888888;
    }

    /* QLabel */
    QLabel {
        color: #ffffff;
    }

    /* QListView */
    QListView {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid black;
        border-radius: 5px;
    }
    QListView:item {
        padding: 5px;
    }
    QListView:item:selected {
        background-color: #666666;
    }

    /* QLineEdit */
    QLineEdit {
        background-color: #444444;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 5px;
    }

    /* QProgressBar */
    QProgressBar {
        background-color: #333333;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        height: 10px;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #888888;
    }

    /* QFrame (Separator) */
    QFrame {
        background-color: #222222;
        height: 1px;
    }
"""
