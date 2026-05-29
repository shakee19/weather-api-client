import requests

from config import BASE_URL, TIMEOUT


def get_weather(city):

    try:

        url = f"{BASE_URL}/{city}?format=j1"

        response = requests.get(url, timeout=TIMEOUT)

        response.raise_for_status()

        data = response.json()

        current = data.get("current_condition")

        if not current:
            raise Exception("Weather data not found")

        temperature = current[0].get("temp_C", "N/A")

        humidity = current[0].get("humidity", "N/A")

        description = current[0]["weatherDesc"][0]["value"]

        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }

    except requests.exceptions.Timeout:
        raise Exception("Request timed out")

    except requests.exceptions.ConnectionError:
        raise Exception("Internet connection problem")

    except Exception as e:
        raise Exception(f"Weather fetch failed: {e}")