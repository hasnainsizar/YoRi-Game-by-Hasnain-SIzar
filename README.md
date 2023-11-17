[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10529017&assignment_repo_type=AssignmentRepo)
# PROJECT TITLE

• YORi Board

CIT 128 Student Directed Project

## Student Info

• Hasnain Sizar

• 37902 

• 2023

## Program Description

The project intends to create a board game with some modifications to Ludo's rules. There will be four players, each with two pieces in the game. Getting both of the pieces to the home area will be necessary to win the game. Players will take turns rolling the dice and adjusting their piece placement on a virtual gaming board with background music and effects. The program will display the game's winner. The Python library Pygame will be used to create the game.

## Goals and timeline:

Two weeks: research and plan

*	Research and review some board games and their rules.
*	Create a plan for developing the project with all the tasks listed, including the game's objectives, rules, and mechanics. 
*	Design the board using Pygame during this time by trying new stuff from the Python library. 

Four weeks: game development

*	Use the fundamental game mechanics: Move the pieces, roll the dice, and show the board as part of the fundamental game mechanics.
*	Create the user interface using the design board that was previously prepared.
*	Establishing Logic and Game Rules.
*	The inclusion of the main menu.
*	Add sound effects and music.

One week: Testing

*	To ensure the program is functioning and error-free, extensively test it.

One week: Finalizing

*	Ensure the code is clean and maintainable.
*	Ensure the README.md file has instructions for running the program.
*	Ensure Python unit tests are complete.
*	Start making the video showing the program working.


### Video Demonstration

https://youtu.be/6UpAhhUeFcg

### Install Instructions

Add any install instructions if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.

* Install pygame library by typing 'pip install pygame' in the terminal.
* Install the given Python, music, and image files from the repository to the same directory in your IDE.
* To avoid errors, copy the code from the repository and paste it into your Python files.
* Ensure all the files are in the same directory.


## Software Engineering

Describe the software engineering techniques used to design and develop this program.

* The programs use Object-oriented programming specifically for the game pieces.
* Git is used to track the changes made in the program over time.

## Testing Script

Describe the testing process using paragraphs and numbered bullet lists on how to manually test the software here. 

* Verify the pygame library is installed.
* Start the YoRi program.
* The following options should be displayed on the main menu screen:
  * Start YoRi - Press 1 to select this option.
  * YoRi Instructions - Press 2 to select this option.
  * Quit YoRi - Press 3 to select this option.
* When '2' is pressed, the game instructions should be visible on the screen.
* Press the 'ESC' key to return to the main menu.
* When '1' is pressed, the YoRi board should be displayed on the game interface.
* The middle top of the board should display the player turn that needs to be played.
* Click on the player piece to roll the dice and move the piece accordingly.
* When the dice are rolled, a number between 1 and 6 should appear randomly.
* The rolled dice would determine how and where the current piece moves.
* If a piece is still in the base, try moving it by clicking on it.
* The piece should stay in the base, if the dice is not a 6.
* Roll the dice until you get a 6.
* The base should be moved onto the start box.
* Keep rolling the dice by clicking on the piece you want to move.
* Based on the outcome of the dice, the piece would then move forward.
* A piece should return to its base area if another piece of a different color collides with it.
* You can test this by moving a piece to a spot where a piece of a different color is already present.
* The collided piece should be sent back to its base area.
* If two pieces of the same color collide, nothing happens as they make a pair.
* A piece that has just left the base area cannot collide with a piece of a different color at the start spot.
* However, a piece can collide with a piece of different color that has just left the base area and is at the start spot before the collision happened.
* Continue playing and rolling the dice one by one.
* A piece of another color cannot enter another piece's home area.
* When a player gets both their pieces to the home area, that player wins the game.
* The winning player should be displayed on the screen.
* After a 7-second delay, the game should quit without errors or bugs.

## Test Inputs

* Keyboard input: To navigate through the menu and make selections, press keys "1," "2," "3," and "Esc."
* Mouse input: Clicking the pieces with the mouse will roll and move the dice.

## Expected Errors:

* Invalid Key input: Pressing a key other than "1", "2", "3", or "Esc" should not cause anything to happen on the main menu.
* Invalid piece movement: Attempting to move a piece that is not permitted by the game's rules or moving a piece to an incorrect location should have no consequences.

## Directions and Grading Rubric

To review the project directions or update the grading rubric, review the [DIRECTIONS.md](DIRECTIONS.md) file.
