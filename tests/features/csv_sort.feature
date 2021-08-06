Feature: CSV Sort

    Sorts a CSV file in descending order
    on the given column name.

    Background: We have an input file
        Given there is a csv file called input.csv
            And it contains a header line

    Scenario: The input file sorts correctly
        Given the name of a column
        and the column is in the header
        When we parse the file
        and sort the file data
        and write the output file
        Then the output has the header row
        and the data is in descending alphabetical order based on the column passed

    Scenario: The intput column is not in the header
        Given the name of a column
        and the column is not in the header
        When we parse the file
        and look for the header index to sort on
        Then an error is printed to the console
        and we exit with a status of 1