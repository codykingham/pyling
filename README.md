# Python for Linguists and Humanists
**Cody Kingham, `cak47[put "at-sign" here].cam.ac.uk`**

**Contents**

* [Intro](#Intro) - description of the course 
* [Getting Started](#Getting-Started) – [how to download this repository](#Download-Repository); [instructions to install Anaconda](#Install-Anaconda); [selecting your own text](#Select-Your-Own-Text) for exercises
* [Course Schedule](#Course-Schedule) - course schedule for Spring 2020
* [Directory (Folder) Structure](#Directory-Structure) - structure of this directory (i.e. folder)
* [Learning Strategies](#Learning-Strategies) - advice for learning how to code in Python
* [Bibliography](#Bibliography) - resources used to develop this course

## Intro

Welcome to the Python for Linguists and Humanists course! In this course you will learn the basics of Python and how to begin using Python to address corpus-driven, quantitative research questions in your field. This course puts an emphasis on a **Bring Your Own Text** (BYOT) approach, where the exercises work from a plain-text file of a text you are interested in. While there are many existing off-the-shelf tools for English texts, humanists often work with non-English texts that are comparatively resource poor. Many Python courses use dummy problems for the exercises. But I've worked to relate many of the exercises to a worthwhile concept in corpus linguistics. Another distinctive of this course is that [Pandas DataFrames](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html) are introduced early on. Pandas is a Python package which provides [data containers](https://docs.python.org/3/library/collections.html) such as [DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame). DataFrames are tables of rows and columns (see [matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:mat-intro/a/intro-to-matrices)) that contain numerical or categorical data. This data structure comes standard in R, for instance, due to its necessity for statistics and data science. Knowledge of Pandas DataFrames are likewise critical if you'd like to later on expand to machine learning.

The total duration of this course is 8 weeks. The first 5 weeks of the course focuses on the bare-bones basics of Python (+Pandas DataFrames). From weeks 6—7, the course introduces corpus linguistic methods for a variety of research questions. We will look at some useful packages for text-modeling such as [Text-Fabric](https://annotation.github.io/text-fabric/) as well as a few mainstream tools like the [Natural Language Toolkit](https://www.nltk.org) and [spaCy](https://spacy.io). The 8th and final week will be dedicated to the final project, in which you will formulate a research question/hypothesis, and design a quantitative experiment to test that hypothesis within your own text. As the culmination of that experiment, you will upload your work to Github and archive it in [Zenodo](https://zenodo.org). 

## Getting Started

To get started with the course, you need to do two things.

    1. Download this repository to your own computer to get all of the exercises and data. 
    2. Install the Anaconda distribution of Python
    3. Select an eligible plain-text document for your exercises

More details are given below.

### Download Repository

The page you're reading now is a part of what's called a Github repository. A "repository" is just another way of saying "folder" or project. Github gives us a way to store and share code openly online. 

You will need a copy of this repository on your own machine for the course. You can download a copy by clicking the green `Clone or download` button:

<img src="images/download_repo.png" height=50% width=50%>

Or if you are familiar with command line and have the developer tools installed (Mac), in a directory of your choice just say:

`git clone https://github.com/codykingham/pyling`

### Install Anaconda

For this course we rely heavily on packages and tools that come prepackaged in the Anaconda distribution of Python. **Even if you already have a version of Python installed**, it is best to install a parallel Anaconda version to avoid potential problems.  

Follow these steps to install and launch Python:

**1.** Proceed to [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/), scroll down, download and install Anaconda **for Python 3.7**.

See the [Anaconda cheatsheet for additional information about installing](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf)

Be sure to select Python 3.7:

<a href="https://www.anaconda.com/distribution/"><img src="images/anaconda_3_7.png" height=50% width=50%></a>

**2.** After installation, open the Anaconda Launcher which should've appeared somewhere in your applications area. Launch the Jupter notebook application. It will open in your web browser. **Note that Jupyter only uses your web browser as an interface, it is not actually connected to the internet and therefore does not need the internet to launch.**

<img src="images/jupyter_launch.png" height=30% width=30%>

You will now see the Jupyter Notebook pane in your browser. Inside a folder of your choice, click `New` at the upper right hand corner. You will see `Notebook: Python 3`. Click it. This will launch you into your first Jupyter notebook!

<img src="images/jupyter_pane.png" height=75% width=75%>

You should also be able to navigate within the Jupyter file navigator to your local copy of this repository. Under the `lessons/` folder you will find a bunch of Jupyter notebooks that are already pre-loaded with code and content. This is how we will begin the course!

### Select Your Own Text

For this course, you should bring your own plain-text corpus OR select one of the texts supplied in the data folder under `texts`, [`data/texts/`](texts). There you will find a selection of pre-made texts from which you can choose. 

The course exercises will automatically load whatever text you have placed inside the `BYOT/` folder. There are few requirements for the text that you choose:

* the text should be plain-text, i.e. NOT Microsoft Word or equivalent, NOT rich text (`.rtf`). Plain-text is provided at some of the options below and is most often saved with `.txt` extension (ending).

## Course Schedule  

## Directory Structure

## Learning Strategies

## Bibliography

