Battleships:
Battleships is a 2-player strategic game in which each player has a grid of ships, with the objective of sinking the opponent's ships as they take turns guessing coordinates.

Features completed:
- initialise the playing board as a grid of coordinates
- read in battleships from a text file as a dictionary
- place the battleships on the board
- implements an option to choose from multiple algorithms for placement of the ships on the board
- processes attacks by the player using coordinates they input
- a simple game loop in the command-line interface
- generates an AI attack as a tuple of coordinates randomly
- implements an AI opponent command-line interface game loop
- adds a graphical user interface with Flask, including a placement page for the battleships and a gameplay page for attacks

Additional features:
- redirects the player to the placement page automatically using the URL
- removes the ability to guess the same coordinates twice (ship does not return to blue after being hit twice)

Execution instructions:
Simple game loop in CLI: Run 'game_engine.py'
AI in CLI: Run 'mp_game_engine.py'
AI in GUI: Run 'main.py' and load the url 'http://127.0.0.1:5000'

Licenses:
The Unlicense
This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.
In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.