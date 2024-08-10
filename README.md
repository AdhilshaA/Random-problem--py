# Collection of random problems

---
## Sudoku Solver lite

### Problem:
- Given a 9x9 sudoku board of hard difficulty, solve the board.

### Motivation:
- Well, I like sudoku. 🤓 I also like solving problems. So why not solve a sudoku problem?
- Why hard difficulty? 
  - Because it's what I solved for a long time. 
  - The techniques I used to solve sudoku in hard difficulty are the same techniques I will use to solve this problem.
- Why not proper sudoku solver?
  - I don't want to solve sudoku problems efficiently. I want to solve sudoku problems using the techniques I used to solve sudoku problems.
  - The main goal is to program the ideas that we obtain visually from the board. This can improve programming skills (I hope :slightly_smiling_face:).
- Will it work for expert difficulty? 
  - It's possible, but not guaranteed.
  - By including more advanced techniques, it will work for expert difficulty.
- Will it work for easy and medium difficulty? 
  - Yes, it will work. But it's overkill.

### Techniques:
- *SuperPencil*:
  - From the entered board, find the possible numbers for each cell.
- *Naked Single*:
  - If a cell has only one possible number, then that number is the answer.
- *Hidden Single*:
  - For a certain number, if there is only one possible cell in a row, column, or box, then that cell is the answer.
- *PencilCorrector*:
  - If a number is found in a row, column, or box, then that number is not possible in other cells in the same row, column, or box.
- By using these techniques repeatedly, the board will be solved.
- If the board is not solved, then the board is unsolvable (for now).

### How to run:
- Run `sudoku solver lvl hard v1.py`.
- There sudoku board can be input into the program. The instructions are provided in the program.
- The program will solve the board and display the solved board.

---
## Translation assistant lite

### Problem:

In sophisticated terms:
- Given a poorly translated text file in English that contains repeated specific mistakes, correct the mistakes through substitution.
- Additionally, We add some formatting to the text file depending on the context.
- Here, the given context is a Chinese Novel translated using Google Translate. The highly domain-specific mistakes are repeated throughout the text, which includes the names of the characters, places, specific emotions etc.
In simple terms:
- Correct the mistakes in the novel I was reading. (it's as silly and simple as that 😝)

### Motivation:
- Guess what? I liked reading that novel. But, the official translations stopped at some point. So, I used Google Translate to read the rest of the novel from raw sources.
- The translation was bad. But, I was able to understand the context. So, I thought, why not correct the mistakes?
- Why use programming to correct the mistakes?
  - Because the mistakes are repeated throughout the text.
  - Because I can and it's fun. 😛
- Why not use a proper translation tool?
  - Well, the tool is not the problem. The problem is the specific mistakes that are repeated throughout the text due to the text provided by the raw sources and pieces perceived by Google Translate.

### Techniques:
  - A dictionary of mistakes and their corrections is maintained within the program.
  - The program reads the text file and replaces the mistakes with the correct words.
  - The program also adds formatting to the text file specifically for Chapter headings, character dialogues, and specific emotions.
  - It skips empty lines, extra spaces, and special characters found in the text file.

### How to run:
- Run `translation special.py`.
- The program will read the text file and correct the mistakes.

---
## Bacteria tracing lite

### Problem:
- Given images of a bacteria colony, trace the bacteria colony movement over time.
- The bacteria can move in and out of plane of focus too.
- The color of the bacteria is very distinct from the background.

### Motivation:
- One of my friend is working on a project where he needs to trace the bacteria colony movement over time. Wanted to try it out.

### Techniques:
- The program reads the images and finds the bacteria through color thresholding.
- Analyse the position of bacteria that extenfs over pixels.
- Repeat for all images to trace the bacteria movement over time.
- Connect the bacteria positions over time to trace the movement (multiple possibilies).
- ⚠️ The program was not completed due to time constraints. Abandoned for now.


