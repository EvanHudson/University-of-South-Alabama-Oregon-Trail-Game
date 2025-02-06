#Roleplay Game - University of South Alabama Adventure


Google Drive with EXE https://drive.google.com/file/d/1Zro38gEgC_zJedhoy1ZUfVchXC6T975J/view?usp=drive_link

This project is a text-based roleplay game set in the style of the classic "Oregon Trail" game. The game takes place at the University of South Alabama, where you, the player, will navigate campus locations, interact with characters, and manage various aspects of your student life, including health, grades, and finances.

The game is powered by an AI assistant that responds to your choices and drives the story forward. The experience is enhanced with background music and animations.
Features

    Interactive Storytelling: The game provides a dynamic and interactive story based on user choices.
    AI Integration: Uses the ollama AI model to generate narrative responses.
    Animation: Background animation is displayed while the game is running, enhancing the immersion.
    Music: Background music plays during the game to set the tone, featuring "Spaghetti Western Showdown."
    Multiple Locations: Explore different buildings and locations around the University of South Alabama campus.
    Character Stats: Manage stats such as health, GPA, and sleep deprivation, which affect the story progression.

Installation

    Clone the repository: If you haven’t already cloned the repository, use the following command:

git clone https://github.com/yourusername/roleplay-game-usa.git

Install Required Libraries: The project requires the following Python libraries:

    ollama
    threading
    gtts
    pygame
    colorama
    CharacterAnimation (this may be a custom module)

You can install these dependencies using pip:

    pip install ollama gtts pygame colorama

    Note: Ensure you have the CharacterAnimation module available in your project directory.

    Download Music File: The game plays background music during the experience. You need to download the Spaghetti Western Showdown.mp3 file and place it in the appropriate path (specified in the script). Alternatively, change the music_file variable to point to your own music file.

Usage
Running the Game

To start the game, simply run the game.py script:

python game.py

Gameplay

    Starting the Game: When you run the script, you'll be prompted to enter your player name.
    AI Interaction: The AI will ask for your major and describe the scenario under 10 words. The game will then proceed to provide different choices to navigate through various campus locations, meet professors, and handle student life.
    Background Music: Music will play continuously in the background, setting the tone for the adventure.
    Animation: Animations will run in a separate thread to keep the environment lively and engaging.
    Stats Management: You will have to manage your stats such as health, GPA, and jag bucks as you make decisions that affect your progress.

Exiting the Game

You can type exit at any point to end the game.
Example Interaction

Player name: John Doe
Welcome to the University of South Alabama Adventure!

What is your major?

Technologies Used

    Python: The game is written in Python and uses various libraries for functionality.
    ollama API: Used for generating AI-powered dialogue and responses.
    pygame: Used for playing background music during gameplay.
    gTTS (Google Text-to-Speech): Used for converting text into speech (potentially for future updates).
    colorama: Used to color text output for improved readability.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

Feel free to fork the project and submit pull requests for improvements. If you find any bugs or issues, please create an issue ticket in the repository.
