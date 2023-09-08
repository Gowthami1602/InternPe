import tkinter as tk
import random

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
SNAKE_SIZE = 20
DELAY = 100  # milliseconds

# Directions
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        self.root.bind("<Key>", self.on_key_press)

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.direction = RIGHT
        self.score = 0
        self.game_over = False

        self.update()
        self.root.mainloop()

    def create_food(self):
        while True:
            food = (random.randint(0, (WIDTH - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HEIGHT - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE)
            if food not in self.snake:
                return food

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == UP:
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == LEFT:
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == RIGHT:
            new_head = (head_x + GRID_SIZE, head_y)

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

        if self.check_collision():
            self.game_over = True

    def check_collision(self):
        head = self.snake[0]

        if (head in self.snake[1:] or
                head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT):
            return True

        return False

    def draw(self):
        self.canvas.delete("all")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR)

        x, y = self.food
        self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=FOOD_COLOR)

        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.draw()
            self.root.after(DELAY, self.update)
        else:
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2, text=f"Game Over\nScore: {self.score}", fill="white", font=("Helvetica", 20)
            )

    def on_key_press(self, event):
        if event.keysym == "Up" and self.direction != DOWN:
            self.direction = UP
        elif event.keysym == "Down" and self.direction != UP:
            self.direction = DOWN
        elif event.keysym == "Left" and self.direction != RIGHT:
            self.direction = LEFT
        elif event.keysym == "Right" and self.direction != LEFT:
            self.direction = RIGHT

if __name__ == "__main__":
    SnakeGame()
