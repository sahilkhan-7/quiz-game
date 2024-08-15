# 🎓 MCQ Quiz Game

Welcome to the **MCQ Quiz Game**, a Python-based project designed to test your knowledge with multiple-choice questions. This project utilizes a MySQL database to securely store login credentials and quiz questions.

## 📜 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## 🚀 Features

- **User Authentication**: Secure login and registration system.
- **Dynamic Question Pool**: MCQ questions are fetched from a MySQL database.
- **Score Tracking**: Keep track of your quiz performance.
- **Responsive Design**: User-friendly interface that adapts to various screen sizes.

## 🛠️ Installation

### Prerequisites

- Python 3.x
- MySQL Server

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sahilkhan-7/quiz-game.git
   cd mcq-quiz-game
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MySQL database**

   - Create a new database and import the provided SQL schema.
   - Update the database configuration in `config.py`.

4. **Run the application**
   ```bash
   python main.py
   ```

## 💻 Usage

1. **Register** a new account or **log in** with existing credentials.
2. **Start a Quiz**: Select the quiz category and difficulty level.
3. **Answer Questions**: Choose the correct answer for each question.
4. **View Results**: After completing the quiz, view your score and correct answers.

## 🗄️ Database Schema

### Tables

1. **Users**
   - `id` (Primary Key)
   - `username`
   - `password` (hashed)

2. **Questions**
   - `id` (Primary Key)
   - `question_text`
   - `option_a`
   - `option_b`
   - `option_c`
   - `option_d`
   - `correct_answer`
   - `category`
   - `difficulty`

## 🤝 Contributing

We welcome contributions to improve this project! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)

---
