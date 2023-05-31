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
        border: 1px solid black;
    }

    QScrollBar:vertical {
        background-color: #F0F0F0;
        width: 16px;
        margin: 0px 0px 0px 0px;
    }
    
    QScrollBar::handle:vertical {
        background-color: #444444;
        min-height: 20px;
    }
    
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        background: none;
    }
    
    QScrollBar:horizontal {
        background-color: #333333;
        height: 16px;
        margin: 0px 0px 0px 0px;
    }
    
    QScrollBar::handle:horizontal {
        background-color: #444444;
        min-width: 20px;
    }
    
    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {
        background: none;
    }
    
    /* QLineEdit */
    QLineEdit {
        background-color: #444444;
        selection-background-color: #507187;
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
