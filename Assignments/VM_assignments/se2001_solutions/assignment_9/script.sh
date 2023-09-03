#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <class> <feature_name>"
  exit 1
fi

# Assign the arguments to variables
class="$1"
feature_name="$2"

# Check if the provided class is valid
case "$class" in
  "setosa" | "versicolor" | "virginica")
    ;;
  *)
    echo "Invalid class: $class"
    exit 1
    ;;
esac

# Check if the provided feature name is valid
case "$feature_name" in
  "sepal_length" | "sepal_width" | "petal_length" | "petal_width")
    ;;
  *)
    echo "Invalid feature name: $feature_name"
    exit 1
    ;;
esac

# Database and table information
database_path="/opt/iris/iris-flower.sqlite3"
table_name="iris"

# SQL query to calculate the mean of the specified feature for the given class
sql_query="SELECT AVG($feature_name) FROM $table_name WHERE class = '$class';"

# Execute the SQL query and store the result in a variable
mean=$(sqlite3 "$database_path" "$sql_query")

# Format the output in JSON
output="{\"class\":\"$class\",\"feature\":\"$feature_name\",\"mean\":$mean}"

# Print the JSON output
echo "$output"

