#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <city-name> <min|max> <mode|average>"
    exit 1
fi

# Assign command line arguments to variables
city="$1"
temp_type="$2"
calc_mode="$3"

# Function to extract temperature values from the website
scrape_weather() {
    city_name="$1"
    temp_type="$2"
    calc_mode="$3"

    # Fetch the weather forecast page
    webpage="http://weather.local/city/${city_name}.html"
    page_content=$(curl -s "$webpage")

    # Use grep and awk to extract the relevant temperature values
    if [ "$temp_type" == "min" ]; then
        temperatures=$(echo "$page_content" | grep -oP 'Min Temp: \K\d+\.\d+' | awk '{sum += $1} END {print sum/NR}')
    elif [ "$temp_type" == "max" ]; then
        temperatures=$(echo "$page_content" | grep -oP 'Max Temp: \K\d+\.\d+' | awk '{sum += $1} END {print sum/NR}')
    else
        echo "Invalid temperature type. Use 'min' or 'max'."
        exit 1
    fi

    # Calculate the mode or average based on user input
    if [ "$calc_mode" == "mode" ]; then
        mode=$(echo "$temperatures" | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')
        echo "$mode"
    elif [ "$calc_mode" == "average" ]; then
        echo "$temperatures"
    else
        echo "Invalid calculation mode. Use 'mode' or 'average'."
        exit 1
    fi
}

# Call the function to scrape and calculate temperature
result=$(scrape_weather "$city" "$temp_type" "$calc_mode")

# Round the result to two decimal places
rounded_result=$(printf "%.2f\n" "$result")

echo "$rounded_result"

