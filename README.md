# Tucker’s Tic-Tac-Toe
![Click here to view the project!](/documentation/other/project-collage.png)

## Introduction
Tucker’s Tic-Tac-Toe is a command-line program developed in Python that provides users with a simple yet fun game of Tic-Tac-Toe. Tucker (the cowboy) will greet users and briefly explain all they need to know about the game. To play Tic-Tac-Toe users take turns filling in cells on a grid of nine squares. The first player to fill in three cells in a row WINS!<br>
[Click here to view the project!](https://tuckers-tic-tac-toe-5f932c36e599.herokuapp.com/)

## User Experience Design
UXD was heavily considered when developing this terminal based project due to the limited visual features on offer. Below, you'll find the planning and development of the project across each plane.
- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

## Strategy Plane
Because this program would be run in the terminal, I immediately understood the challenges I faced when trying to create a game, as the way it would be presented to the user would be unfamiliar to most people and therefore offer some confusion. Taking this into account, I identified the following criteria that needed to be met for the project to deliver a positive user experience: Below, you'll find the objectives I decided upon. 
- Keep the user informed but not overwhelmed with text.
- Provide the user with a snappy, interactive gaming experience.

## Scope Plane
Using the strategy plane to guide me in breaking the game down into different sections, I ultimately settled on the following three stages:
- A stage that provides the user with information about the game. 
- A stage where users can play the game.
- A stage that concludes the game.

## Structure Plane
As Tic-Tac-Toe can be played by people of all ages, I felt it was important to make the game as unambiguous as possible, especially considering the way it would be presented to the user. Players move through the game by entering the number of an empty cell and hitting the ‘Enter’ key to lock in their choice. Each valid input will draw the game closer to its end.
Users will be guided through the game with the help of instruction messages that request their next move and error messages that indicate why their input might not have been valid.
The game is intended to be a relatively fast-paced game with short rounds, and so after a brief game conclusion, players can choose to either replay or end the game, with the focus being on getting back to the FUN!

## Skeleton Plane
When planning for this project, I created a flowchart to help me visualise the necessary functions needed to create a basic game of Tic-Tac-Toe. The flowchart depicts the journey taken through the program when completing the game. The final deployed project includes the change_player function, which isn't shown on the flowchart. This function changes the player's input marker between `”X”` and `”O”`. Below, you’ll find the flowchart and a brief description of each step.

1. When the game starts, the instructions are displayed, followed by the game board legend and the game board.

2. Next, the user will be prompted to provide an input of an empty cell number.

3. The program will check to see if the input provided is valid before moving on to one of two outcomes. If the input is valid, a marker will be placed in the cell number provided. If the input is invalid, an error message will be shown, and the player will be guided to input a valid input.

4. Following this, the program will check to see if the latest game board update has produced a winning result. If the game has been won, players will be presented with a message that shows the result of the game. If the game hasn't been won, then the program will check to see if the game has resulted in a tie. If the game does end in a tie, then players will be presented with a message that shows the result of the game. If the game hasn't been won and doesn’t result in a tie, then the programme will request that the other player provide a valid input.

5. When the game has concluded, players are asked to provide a valid input to determine whether or not they would like to play another round of the game or exit the program.

6. Once again, the program will check to see if the input provided is valid before providing an outcome. If the input is invalid, an error message will be shown, and the player will be guided to enter a valid input.

![Project flowchart](/documentation/flowcharts/flowchart.png)<br>
*This image shows the flowchart used to help create this program*

## Surface Plane
### Project Features
**Game instructions**<br>
Only when the program is first run will users be presented with instructions that explain how to play Tic-Tac-Toe. Upon users choosing to play another round, the program skips past the instructions, and gets right back to the game.<br> 
![Game instruction 1](/documentation/features/intro-instruction-1.png)
![Game instruction 2](/documentation/features/intro-instruction-2.png)
![Game instruction 3](/documentation/features/intro-instruction-3.png)
![Game instruction 4](/documentation/features/intro-instruction-4.png)
![Game instruction 5](/documentation/features/intro-instruction-5.png)<br>
*These images show the instructional messages displayed opon running the program.*

**Game-board legend**<br>
Following the game instructions, a small legend of the game board is displayed in the top-left corner of the terminal on the initial launch of the program, as well as each time the game board is updated to help users visualise in which cell they are placing their mark.

**Game-board**<br>
An empty game board is displayed to the user on launch of the program and is then redisplayed after each update of the board, allowing players to see where they have previously placed their mark.<br>
![Game legend and gameboard](/documentation/features/legend-gameboard.png)<br>
*This image shows both the game legend and the empty game board.*

**Conclusion message**<br>
One of three messages will be displayed to the user, depending on the outcome of the game. From this game stage, the user can choose to either play another game or end the program.<br>
![Game conclution message 1](/documentation/features/tie-message.png)<br>
*This image shows the message given upon a game tie.*


![Game conclution message 2](/documentation/features/win-message.png)<br>
*This image shows the message given upon a game win.*
 
### Features left to implement
**vs Computer**<br>
I plan to incorporate a player vs. computer game mode where players can enjoy the game on their own. The computer will prioritise moves that lead them to victory.

**Highlight the winning move**<br>
Another feature I aim to implement in the program is to simply display to the user the winning move combination in contrasting colour so that they can clearly see the outcome and potentially up their game!

## Technologies Used
**Python Modules**
- **Os module** was used to clear the terminal when updated to reduce any clutter in the terminal.
- **Sys module** was required to end the program
- **Time module** was used to create a delay and provide the user with breathing space between terminal updates.

## Programs Used
- **Balsamiq** was used to creating flowcharts.
- **Git** was used as a version control system for tracking changes.
- **GitHub** was used as a code hosting platform for version control.
- **Gitpod** was my choice of cloud development environment.
- **Heroku** was used as a method for the deployment of the app
- **PEP8 Python Linter** was used to validate Python code. 

## Testing
**PEP8 Python Linter**<br>
I used the Code Institute PEP8 Python Linter to validate my Python code and ensure it was free from errors.
![Validated code showing no errors](/documentation/validation/code-validation-noerrors.png)<br>
*This image shows the projects code showing no errors after being validated.*

**Detected bugs and solutions**
- When validating the user input upon them selecting their move, if players entered the value `0` they would be met with two error messages, the former that told the user `## This cell is taken, please choose an EMPTY cell! ##` and the latter that told them `## Please only enter a number between 1-9! ##`. This wasn't the intended outcome, as players should only receive the second error message due to `cell 0` not being a viable option. To fix this when validating the value, I checked to see if it was `< 1`, before checking if the cell was equal to `“ ”`.

| Feature | Expected Outcome | Testing Procedure | Result |
|----------|----------|----------|----------|
| Introduction | Upon running the program, the game runs through the instructions. | Run the program. | This feature responds as expected. |
| Render the legend. | Within the main loop of the program, the game board legend is displayed to the user, both during the launch and for each iteration of the game. | Run the program and play an iteration of the main loop. | This feature responds as expected. |
| Render the game board. | Within the main loop of the program, the game board is displayed to the user, showing empty cells on launch, and populated cells each subsequent iteration. | Run the program and play an iteration of the main loop. | This feature responds as expected. |
| Cell choice input | Request `{current_player} Make your move! (1-9):` and loop until the input is validated, then update the board. | Inputs: `“ ”`, `“0”`, `“11”`, `“Cat”` and `Enter key` | Loops until the input is validated, with appropriate error messages.<br>1.`## Input invalid. Please enter a number between 1-9! ##`<br> 2.`## Input invalid. This cell is taken, please choose an EMPTY cell! ##`<br>3.`## Input invalid. Please only enter a number between 1-9! ##`<br>4.`## Input invalid. Please enter a NUMBER between 1-9! ##` |
| Check for winner | After each game board update, the `check_winner` function checks to see if any of the winning combos have been executed for each player marker. | Run the program and play several rounds of the game. | This feature responds as expected. |
| Check for a tie | After checking for a winner, the check-tie function checks to see if any game board cells are free to either continue or conclude the game. | Run the program and play several rounds of the game. | This feature responds as expected. |
| Change the current player | Change the current player from one to the other, i.e., change `“X”` to `”O”` and vice versa. | Run the program and play a round of the game. | This feature responds as expected. |
| Replay game/ Exit game choice input | Request user to input `(Y/N)` and loops until the input is validated the either, starts a new game or exits the program. | Inputs: `“ ”`, `“0”`, `“11”`, `“Cat”` and `Enter key` | Loops until the input is validated, with appropriate error message.<br>1.`## Input invalid. Enter either 'Y' or 'N' ##`. |


## Deployment
**The site was deployed to Heroku using the following steps:**
1. Navigate to heroku.com and create an account.
2. Click the "New" button in the top right corner.
3. Select "Create new app".
4. Enter the app name.
5. Select Region and click "Create app".
6. Go to the Settings tab and click "Reveal config vars".
7. Add any necessary config vars.
8. Click the Deploy tab.
9. Scroll down to Connect to GitHub and sign in / authorize when prompted.
10. Find the repository you want to deploy and click "Connect".
11. Scroll down to Manual deploy and choose the main branch.
12. Click "Deploy Branch".
13. The app should now be deployed and you can click on the "View" button to view the live site.
  
**Clone a GitHub repository**
1. Navigate to the GitHub Repository you want to clone.
2. Click on the "Code" drop down button.
3. Click on HTTPS.
4. Copy the repository link to the clipboard.
5. Open your IDE of choice (git must be installed for the next steps).
6. Type git clone copied-git-url into the terminal.
7. The project will now have been cloned on your local machine for use.

**Fork Project**
1. Navigate to the GitHub Repository you want to fork.
2. On the top right of the page under the header, click the "Fork" button.
3. This will create a duplicate of the full project in your GitHub Repository.

## Credits
Media
- The formation of characters used for the ASCII cowboy was taken from: [emojicombos.com](https://emojicombos.com/cowboy-ascii-art)

## Acknowledgements  
The completion of this project would not have been possible without the support of my partner; the patience, motivation, and enthusiasm she offers is second to none!