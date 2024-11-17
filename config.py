import os


class Config:
    # Define the database - we are working with Postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jader@localhost:5432/hcm'

    # Signal application everytime there is a change in Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret Key for flash messages
    SECRET_KEY = os.urandom(24)
