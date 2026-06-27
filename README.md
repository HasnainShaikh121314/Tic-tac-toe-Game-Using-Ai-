# 🎮 Tic Tac Toe AI using Pygame

A classic **Tic Tac Toe** game built with **Python** and **Pygame**, featuring an unbeatable AI opponent powered by the **Minimax Algorithm with Alpha-Beta Pruning**.

---

## 📌 Features

* 🎨 Graphical user interface using Pygame
* 🤖 AI opponent using Minimax with Alpha-Beta Pruning
* 👤 Human vs Computer gameplay
* 🏆 Automatic winner and draw detection
* 🔄 Restart the game by pressing **R**
* 🖼️ Custom game assets (background, X, and O images)

---

## 📂 Project Structure

```
tic-tac-toe/
│
├── images/
│   ├── bg.jpg
│   ├── x.png
│   └── o.png
│
├── tic_tac_toe.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
cd tic-tac-toe-ai
```

### 2. Install dependencies

```bash
pip install pygame
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Game

```bash
python tic_tac_toe.py
```

---

## 🎮 Controls

| Action       | Control          |
| ------------ | ---------------- |
| Place X      | Left Mouse Click |
| Restart Game | **R** Key        |
| Quit         | Close Window     |

---

## 🧠 AI Algorithm

The computer player uses:

* **Minimax Algorithm**
* **Alpha-Beta Pruning**

### Why Alpha-Beta Pruning?

Alpha-Beta Pruning reduces the number of game states that need to be evaluated while producing the same optimal move as the standard Minimax algorithm.

Benefits include:

* Faster decision making
* Reduced computation
* Unbeatable gameplay

---

## 🏆 Game Rules

* The human player always plays as **X**.
* The AI always plays as **O**.
* The first player to align three symbols horizontally, vertically, or diagonally wins.
* If all cells are filled without a winner, the game ends in a draw.

---

## 📸 Screenshots

Add screenshots of the game here.

Example:

```
screenshots/gameplay.png
```

Markdown:

```md
![Gameplay](screenshots/gameplay.png)
```

---

## 📦 Requirements

* Python 3.8+
* Pygame

Install using:

```bash
pip install pygame
```

---

## 🔍 Algorithm Complexity

### Minimax

* Time Complexity: **O(b^d)**
* Space Complexity: **O(d)**

where:

* **b** = branching factor
* **d** = search depth

Alpha-Beta Pruning significantly reduces the number of nodes explored in practice.

---

## 🛠️ Future Improvements

* Difficulty levels (Easy, Medium, Hard)
* Scoreboard
* Sound effects
* Animations
* Main menu
* Multiplayer mode
* Better UI and visual effects

---

## 👨‍💻 Author

Developed using **Python** and **Pygame** as an implementation of game AI with the Minimax Algorithm and Alpha-Beta Pruning.

---

