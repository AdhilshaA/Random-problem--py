# Collection of random problems

## Sudoku Solver

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

## Translation assistant lite

### Problem:

- Given a poorly translated text file in English that contains repeated specific mistakes, correct the mistakes through substitution.
- Additionally, We add some formatting to the text file depending on the context.
- Here, the given context is a Chinese Novel translated using Google Translate. The highly domain-specific mistakes are repeated throughout the text, which includes the names of the characters, places, specific emotions etc.

### Motivation:
- Guess what? I liked reading that novel. But, the official translations stopped at some point. So, I used Google Translate to read the rest of the novel from raw sources.
- The translation was bad. But, I was able to understand the context. So, I thought, why not correct the mistakes?
- Why use programming to correct the mistakes?
  - Because the mistakes are repeated throughout the text.
  - Because I can and it's fun.
- 