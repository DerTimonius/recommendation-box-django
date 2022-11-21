# Django API for recommendation box

This little API holds the magic for my [recommendation box project](https://github.com/DerTimonius/recommendation-box). Here, the recommendation system will take action if the API is called as well as the search functionality of the project.

## Technologies used

- Pandas
- Numpy
- Scikit-learn
- Django

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
