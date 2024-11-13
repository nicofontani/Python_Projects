# /******************************************************************************/ 
# /*                                                                            */
# /*                          CSV Read and Append Example                        */
# /*                                                                            */
# /* DESCRIPTION:                                                               */
# /* This script demonstrates how to read data from one CSV file and append it  */
# /* to another. It reads the contents of 'test.csv', prints them to the console,*/
# /* and appends the data to 'test2.csv'.                                        */
# /*                                                                            */
# /* Copyright (c) 2024, Nico Fontani                                           */
# /* Creation Date: 13 Nov 2024                                                 */
# /*                                                                            */
# /* Original Author: Nico Fontani                                              */
# /* Last Modified: 13 Nov 2024                                                 */
# /*                                                                            */
# /* Supported by Python                                                         */
# /*                                                                            */
# /******************************************************************************/

import csv

# Open the first CSV file to read data
with open('test.csv') as f:

    # Read the rows of the CSV file
    rows = csv.reader(f)

    # Convert the rows into a list
    l = list(rows)

    # Print each row
    for row in l:
        print(row)

# Open the second CSV file in append mode to write data
with open('test2.csv', mode='a') as f:

    # Create a CSV writer
    writer = csv.writer(f)

    # Write all rows from the first CSV file to the second file
    for row in l:
        writer.writerows([row])
