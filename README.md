### The server for the API has been taken offline, so if you have to clone this repo to use it locally!

# Django API for recommendation box

This little API holds the magic for my [recommendation box project](https://github.com/DerTimonius/recommendation-box). Here, the recommendation system will take action if the API is called as well as the search functionality of the project.

## Technologies used

- Pandas
- Numpy
- Scikit-learn
- Django

## Overview

To get a quick overview on how this recommendation system is working, please consult this schema:
![Drawing of the functionality](/schema/excalidraw.png)

## How it's working

I combined two different datasets of movies and TV shows from Netflix and Amazon Prime, so it's now about 19k movies/shows. What I also did, was to combine the `cast`, `description`, `genres` etc into a new column called `features`. The dataset is then loaded into a Pandas dataframe.

As an input the application is getting four things:

1. List of selected movies/TV shows
2. Type of entertainment wanted (movie, TV shows or both)
3. Number of recommendations wanted
4. User preference on Bollywood movies

First we're stripping the dataframe if the user wants to get only movie or TV show recommendations.
As a next step, the `features` column of every movie is compared against each other movie using a Count Vectorizer, and similarity scores are created (from 0 to 1, 0 being nothing alike and 1 being the same movie) and added to a cosine_similarity_matrix.
Now, we have to create a new list of the 20 most similar movies/shows for every movie in the selected movie list and save the index and scores. Then, for every movie in this list, the scores are checked and added up.
If the user wants to exclude Bollywood movies they will be removed here.
The list is then sorted according to the total scores and the application is returning the number of recommendations the user specified.

## Deployment

This API was deployed on [fly.io](https://fly.io) with a dockerized image.

## Cloning and usage

If you want to use this API locally, you can clone this project using the following steps:

```bash
git clone https://github.com/DerTimonius/recommendation-box-django
cd recommendation-box-django
```

Make sure you have Python installed by running:

```bash
python -V
```

It should be above 3.10

Next you want to create a virtual environment:

```bash
python -m venv <your-virtual-environment-name>
```

To activate it, on Windows run the following:

```bash
source <your-virtual-environment-name>/Scripts/activate
```

Or on Mac/Linux:

```bash
source <your-virtual-environment-name>/bin/activate
```

Now you need to install the necessary packages:

```bash
pip install -r requirements.txt
```

To start the server on localhost:8000:

```bash
python recommendationbox/manage.py runserver
```

You also need to setup a `.env` file in the `recommendationsbox` directory and add the `SECRET_KEY` there. I provided a `generate_secret.py` file which you can use to get a random key.
