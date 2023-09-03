#!/bin/bash

# Function to fetch weather data from the API and parse it with jq
get_weather_data() {
    local city_name="$1"
    local option="$2"
    local arg="$3"

    # Weather API URL
    local api_url="http://weather.local/api/v1/city/${city_name}.json"

    # Fetch JSON data from the API
    local json_data=$(curl -s "$api_url")

    case "$option" in
        "-C")
            case "$arg" in
                "min")
                    temp_min=$(echo "$json_data" | jq -r '.main.temp_min')
                    echo "{"
                    echo "    \"name\": \"$city_name\","
                    echo "    \"temp_min\": $temp_min"
                    echo "}"
                    ;;
                "max")
                    temp_max=$(echo "$json_data" | jq -r '.main.temp_max')
                    echo "{"
                    echo "    \"name\": \"$city_name\","
                    echo "    \"temp_max\": $temp_max"
                    echo "}"
                    ;;
                "current")
                    temp_celsius=$(echo "$json_data" | jq -r '.main.temp')
                    temp_fahrenheit=$(echo "($temp_celsius * 9/5) + 32" | bc -l)
                    echo "{"
                    echo "    \"name\": \"$city_name\","
                    echo "    \"temp\": $temp_celsius,"
                    echo "    \"F\": $temp_fahrenheit"
                    echo "}"
                    ;;
                *)
                    echo "Invalid argument for -C option: $arg" >&2
                    exit 1
                    ;;
            esac
            ;;
        "-W")
            speed=$(echo "$json_data" | jq -r '.wind.speed')
            sqrt_speed=$(echo "sqrt($speed)" | bc -l)
            echo "{"
            echo "    \"name\": \"$city_name\","
            echo "    \"speed\": $speed,"
            echo "    \"sqrtspeed\": $sqrt_speed"
            echo "}"
            ;;
        "-S")
            city_name=$(echo "$json_data" | jq -r '.name')
            date=$(date +"%d/%m/%Y")
            sunrise=$(echo "$json_data" | jq -r '.sys.sunrise' | date -u +"%H:%M:%S")
            sunset=$(echo "$json_data" | jq -r '.sys.sunset' | date -u +"%H:%M:%S")
            echo "["
            echo "    \"$city_name\","
            echo "    \"$date\","
            echo "    \"$sunrise\","
            echo "    \"$sunset\""
            echo "]"
            ;;
        *)
            echo "Invalid option: $option" >&2
            exit 1
            ;;
    esac
}

# Main script

# Check for the correct number of arguments
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 city-name [options]" >&2
    exit 1
fi

# Extract the city name
city_name="$1"
shift

# Loop through options and arguments
while [ "$#" -ge 2 ]; do
    option="$1"
    arg="$2"
    get_weather_data "$city_name" "$option" "$arg"
    shift 2
done

