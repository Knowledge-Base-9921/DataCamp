# [Project: Investigating Netflix Movies](https://app.datacamp.com/learn/projects/investigating_netflix/guided/Python)

## Credits

Datacamp

## Description

Apply the foundational Python skills you learned in Introduction to Python and Intermediate Python by manipulating and visualizing movie data.

### Project Details

Explore Netflix movie data and perform exploratory data analysis for a production company to uncover insights about movies from a particular decade.

### Project Instructions

Perform exploratory data analysis on the ``netflix_data.csv`` data to understand more about movies from the 1990s decade.

* What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called ``duration`` (use 1990 as the decade's start year).
* A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as ``short_movie_count``.

Feel free to experiment after submitting the project!

### Guides

#### 1. Filter the data for movies released in the 1990s

You'll want to subset the DataFrame to keep only the movies and then filter the years so that you are working with rows where the release year is between 1990 and 1999.

* How to subset a DataFrame
    * One way to subset a DataFrame is to use square brackets, passing in a condition.
    * First, use square brackets to select the type column you want to subset with a condition, using quotation marks around the column name: df["col_name"].
    * Then, apply a conditional operator and the condition you want. A conditional operator can be <, >=, ==, for example.
    * After the operator, type the rest of the conditional, such as the string or number you want to subset.
    * Finally, wrap all of that in other set of square brackets to subset the original DataFrame.
* Filtering by column values
    * You can filter by specifying a condition using square brackets, similar to subsetting a DataFrame.
    * First, use square brackets to select the column you want to filter with a condition, using quotation marks around the column name: df["col_name"].
    * Then, apply a conditional operator and the condition you want. A conditional operator can be <, >=, ==, for example.
    * After the operator, type the rest of the conditional, such as the string or number you want to filter.
    * To filter for a the 1990's, you'd want to filter for movies released on or after 1990, and before 2000.
    * You can filter a DataFrame multiple times to apply several filters, saving a new DataFrame each time and then using the newest DataFrame for the next filter.

#### 2. Find the most frequent movie duration

Visualize the data to view the distributions of durations for movies released in the 1990s.

* Visualizing a distribution
    * Use plt.hist() on your desired column to view the distribution of its values.
    * Look at the plot to see where the most frequent count falls and save the duration value as duration.

#### 4. Count the number of short action movies from the 1990s

First, subset the data again to keep only movies with the correct genre. Then, iterate through the data and count the number of movies depending on the condition pf a duration that is less than 90.

* Subsetting by genre
    * Use square brackets and a conditional operator to filter the "genre" column for "Action" movies from your 1990's movies DataFrame.
* Setting up a counter
    * You'll first need to set up the counter, short_movie_count as a variable with the value 0.
    * This should be outside a for loop if you are making one.
* Iterating through a DataFrame
    * Use a for loop with the .iterrows() method to iterate through the DataFrame's labels and rows.
    * You should be using the DataFrame that is filtered for 90's Action movies.
    * When doing this, you'll need to list both the label and row in the for loop since .iterrows() unpacks these items: for label, row in....
* Counting a condition
    * Use an if/else statement to check if the duration is less than 90, if it is, and 1 to short_movie_count, if it isn't, do nothing.
    * You can place this statement within a for loop to do it more than once.