# SloVerb Flask App

This is a Flask web application named SloVerb, designed to transform any song. 

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [File Structure](#file-structure)
4. [Installation](#installation)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Overview

SloVerb allows users to paste a YouTube link to a song and adjust three parameters:
- **Speed:** Adjust the speed of the song playback.
- **Room Size:** Control the simulated room size effect.
- **Wetness:** Control the wetness or reverb effect of the song.

## Features

- **User Interface:** The web interface is designed to be intuitive and easy to use.
- **Dark Mode:** Users can toggle between light and dark modes by clicking on the lightbulb icon.
- **Slider Controls:** Sliders are provided for each parameter to allow fine adjustments.
- **Submission:** Once the user is satisfied with their adjustments, they can submit the form to process the data.

## File Structure

- `app.py`: Contains the Flask application code including routes and logic.
- `templates/index.html`: HTML template for the user interface.
- `static/css/style.css`: CSS styles for the UI.
- `static/js/script.js`: JavaScript functions for interactive elements.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run `python app.py` to start the Flask application.
4. Open your web browser and go to `http://localhost:5000` to access the SloVerb app.

## Dependencies

- Flask: A micro web framework for Python.
- Bootstrap: CSS framework for responsive and mobile-first web development.
- Font Awesome: Icon set and toolkit.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request on the GitHub repository.

