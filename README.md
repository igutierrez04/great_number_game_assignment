Great Number Game Assignment

    Create a site that allows a user to play this guessing game. Upon loading, the server should 'pick' a random number between 1-100; store the number in session. Allow the user to guess the number--tell them when they are too high or too low. If they guess the correct number, notify them and offer to play again.

    Assignment check list
        - Create a flask project called great_number_game
        - In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
        - Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
        - NINJA BONUS: Allow the user to keep guessing until they get it correct.
        - SENSEI BONUS: Only allow the user to guess up to 5 times. If they don't guess it on their 5th attempt, display a "You lose" message and allow them to try again.
        - SENSEI BONUS: If they win, allow the user to submit their name. Have a link to a leader-board page that shows winners' names and how many attempts they took to guess correctly.