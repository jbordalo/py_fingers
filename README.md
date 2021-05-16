# 10FastFingers Bot

## About The Project
Selenium bot which plays the [10FastFingers typing test](https://10fastfingers.com/).

## Getting Started

Clone the project locally.</br>

## Prerequisites

*selenium* must be [installed](https://selenium-python.readthedocs.io/installation.html) on the machine:

This project uses version 90 of [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/).

You can change this by downloading another ChromeDriver or by changing this line for different browsers.

`driver = webdriver.Chrome()`

## Usage

You can define the desired words per minute:

`python3 py_fingers WPM`

For unlimited speed:

`python3 py_fingers 0`

## Built With

* [selenium](https://selenium-python.readthedocs.io/)

## Authors

* **João Bordalo** - *Initial work* - [jbordalo](https://github.com/jbordalo)
