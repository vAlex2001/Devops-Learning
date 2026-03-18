#!/bin/bash


# For loop - iterate over a list
echo "--- Looping over a list. ---"
for NAME in Alex Diana Gogu Dorel Vasile; do
    echo "Salut, $NAME!"
done

# For loop - iterate over numbers
echo "--- Looping over numbers. ---"
for i in {1..5}; do
    echo "Number: $i"
done

# For loop - iterate over .sh files in folder
echo "--- Looping files with .sh. ---"
for FILE in ~/devops-journey/scripts/*.sh; do
    echo "Found script: $FILE"
done

# While loop
COUNT=1

while [ $COUNT -le 5 ]; do
    echo "Count is: $COUNT"
    COUNT=$((COUNT + 1))
done