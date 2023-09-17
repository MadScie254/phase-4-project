# Sentiment Analysis Project

![Sentiment Analysis](sentiment-analysis.jpg)

## Overview

This repository contains the code and resources for a sentiment analysis project. Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotional tone expressed in a piece of text, such as a tweet or a product review. In this project, we use machine learning techniques to classify text data into different sentiment categories.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The main goal of this project is to build a sentiment analysis model capable of classifying text data into different sentiment categories, such as positive, negative, or neutral. The project follows a series of data science steps, including data preprocessing, model development, and evaluation.

## Dataset

We used two datasets in this project:

1. **twitter_data.csv**: This dataset contains raw Twitter data, including tweet text and other relevant information.

2. **preprocessed_twitter_data.csv**: This dataset is the result of our data preprocessing pipeline, where we cleaned, tokenized, and prepared the data for model training.

## Project Structure

The project is structured as follows:

- `app.py`: Flask web application for deploying the sentiment analysis model.
- `requests.py`: Contains HTTP request examples for interacting with the deployed model.
- `sentiment_analysis.ipynb`: Jupyter Notebook containing the data preprocessing, model training, and evaluation code.
- `sentiment_model.h5`: The trained sentiment analysis model in HDF5 format.
- `sentiment_prediction.py`: Python script for making predictions using the trained model.
- `tokenizer.pkl`: Pickle file containing the tokenizer used for text tokenization.

## Installation

To set up the project environment, follow these steps:

1. Clone this repository to your local machine using the following command:


2. Install the required Python libraries using pip:


## Usage

- To train and evaluate the sentiment analysis model, open and run the `sentiment_analysis.ipynb` Jupyter Notebook.

- To deploy the model locally, run `app.py` and make HTTP POST requests using `requests.py`.

- To make predictions using the trained model, use `sentiment_prediction.py`.

## Model

The sentiment analysis model is built using deep learning techniques and is available as `sentiment_model.h5`.

## Evaluation

We evaluated the model's performance using various evaluation metrics, including accuracy, precision, recall, and F1-score. You can find the detailed evaluation results in the Jupyter Notebook.

## Deployment

The model can be deployed locally using the Flask web application in `app.py`. Follow the instructions in the `Deployment` section of the notebook for more details.
![ExcitedGIF](https://github.com/MadScie254/phase-4-project/assets/134260642/56e39d40-3e91-456a-8ca9-3eeb6d2179ee)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
