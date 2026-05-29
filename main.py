from weather import get_weather
from logger import log_info, log_error


def main():

    try:

        city = input("\nEnter city name: ").strip()

        if not city:
            print("City name cannot be empty")
            return

        weather = get_weather(city)

        print("\n========== WEATHER REPORT ==========")

        print(f"City        : {city}")

        print(f"Temperature : {weather['temperature']}°C")

        print(f"Humidity    : {weather['humidity']}%")

        print(f"Condition   : {weather['description']}")

        print("====================================\n")

        log_info(f"Weather fetched successfully for {city}")

    except Exception as e:

        print(f"\nERROR: {e}\n")

        log_error(str(e))


if __name__ == "__main__":
    main()