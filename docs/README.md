# Integrating ModelKits into Jupyter Notebook Workflows: A Practical Example

## Introduction

The kaggle competition, [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic), issues a challenge to create a model that uses Titanic passenger data (name, age, price of ticket, etc) to try to predict who survived and who died.  

While this Notebook does build out a solution to the problem posed, the primary goal isn't to create the best predictive model, but, instead, to demonstrate how to leverage [KitOps Modelkits](https://www.kitops.ml) within a machine learning workflow.

And,though the current context applies to Jupyter Notebooks written in Python, the code provided could be used just as effectively in workflows existing outside of a Notebook environment, as well.  Also, the code's functionality could be easily reproduced in other programming languages.

## Before You Begin

1. If you haven't aready done so, [sign up for a free account with Jozu.ml](https://api.jozu.ml/signup)

2. After you log into Jozu, add a new Repository named *"titanic-survivability"*, which we'll use in this Notebook.

3. In the same directory as this Notebook--which we'll call the *Project directory*--create a `.env` file.

4. Edit the `.env` file and add an entry for your **JOZU_USERNAME**, your **JOZU_PASSWORD** and your **JOZU_NAMESPACE** (aka your **Personal Organization** name). For example:
```bash
    JOZU_USERNAME=brett@jozu.org
    JOZU_PASSWORD=my_password
    JOZU_NAMESPACE=brett
```
5. Be sure to save the changes to your .env file before continuing.

## Project Setup

### Set Up Your Python Environment

- This project was created using Python 3.12, but should work for Python versions >= 3.9.

- We recommend using a Python or Conda virtual environment to isolate this project's code to prevent it from affecting the system-installed Python.

- If you name your Python or Conda environment something other than ".venv" or "venv", then be sure to add the name to the `.gitignore` file. *This step assumes you'll be using `git` for version control of this project.*

## Project Deliverables

While working through the project's Notebook, a total of three separate ModelKits will be packed and pushed to Jozu Hub:

1. Immediately after the training and test datasets are loaded, the first ModelKit version is packed and pushed with a tag similar to: `collated-data_v1_2024-10-21_13-03-28_UTC`.

2. After the data has been cleaned and processed for model training, but before any model training is done, the second ModelKit version is packed and pushed with a tag similar to: `processed-data_v2_2024-10-21_13-19-02_UTC`.

3. Finally, when the model has been trained and validated, the third ModelKit version is packed and pushed with a tag similar to: `trained_model_v2_2024-10-21_13-42-49_UTC`.

You can view the details for these tagged ModelKit versions by viewing your `titanic-survivability` repository in Jozu Hub.

