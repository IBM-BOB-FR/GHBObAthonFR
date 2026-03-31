# OpenWeather One Call API 3.0

## Product Concept

OpenWeather **One Call API 3.0** provides access to essential weather data, short-term and long-term forecasts, and aggregated weather data. It is designed to support easy migration from the Dark Sky API.

One Call API 3.0 includes **5 endpoints**:

1. **Current weather and forecasts**
   - Minute forecast for 1 hour
   - Hourly forecast for 48 hours
   - Daily forecast for 8 days
   - Government weather alerts
2. **Weather data for any timestamp**
   - Historical archive for 47+ years
   - Forecast up to 4 days ahead
3. **Daily aggregation of weather data**
   - Historical archive for 47+ years
   - Forecast up to 1.5 years ahead
4. **Weather overview**
   - Human-readable summary for today and tomorrow using OpenWeather AI technologies
5. **AI Weather Assistant**
   - Human-readable weather data and weather-related advice

One Call API 3.0 is based on the proprietary **OpenWeather Model** and is updated every **10 minutes**. To get the most accurate and up-to-date data, OpenWeather recommends requesting One Call API 3.0 every 10 minutes.

> **Subscription note**
>
> One Call API 3.0 is included in the **"One Call by Call"** subscription only. This separate subscription includes **1,000 calls/day for free** and allows you to pay only for the number of API calls made to this product. You do **not** need to subscribe to other OpenWeather plans to access One Call API 3.0.
>
> The original documentation also states that after subscribing to One Call API 3.0, **2,000 API calls/day** are set up by default. If you want to change this limit, go to **Billing plans** in your personal account.

For more details, see the **pricing page**, **FAQ**, or ask **Ulla**, the OpenWeather AI assistant.

---

## How to Start

1. Sign up for OpenWeather if you do not yet have an API key.
2. Review the pricing page.
3. Subscribe to **One Call API 3.0** (sold as a separate subscription).
4. By default, your account may be configured with **2,000 API calls/day** for this product.
   - To change the limit, go to **Billing plans** in your Personal account.
5. Choose the type of data you want:
   - Current & forecasts weather data
   - Weather data for a timestamp
   - Daily aggregation
   - Weather overview
   - AI Weather Assistant
6. Make the corresponding API call and include your API key in every request.

---

# 1) Current and Forecasts Weather Data

Use this endpoint to retrieve:

- Current weather
- Minute forecast for 1 hour
- Hourly forecast for 48 hours
- Daily forecast for 8 days
- Government weather alerts

If you need other One Call API 3.0 functionality, see [Product Concept](#product-concept).

## API Call

```http
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `lat` | Yes | Latitude, decimal (`-90` to `90`). If you need automatic geocoding for city names / ZIP codes, use the Geocoding API. |
| `lon` | Yes | Longitude, decimal (`-180` to `180`). If you need automatic geocoding for city names / ZIP codes, use the Geocoding API. |
| `appid` | Yes | Your unique API key (available in your account under **API key**). |
| `exclude` | No | Comma-delimited list (without spaces) of parts to exclude from the response. Available values: `current`, `minutely`, `hourly`, `daily`, `alerts` |
| `units` | No | Units of measurement: `standard`, `metric`, `imperial`. Default: `standard`. |
| `lang` | No | Language for output. |

## Example API Calls

> **Important**: One Call 3.0 is included only in the **"One Call by Call"** subscription.

Exclude some sections:

```http
https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
```

Return all sections:

```http
https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={API key}
```

## Example API Response

```json
{
  "lat": 33.44,
  "lon": -94.04,
  "timezone": "America/Chicago",
  "timezone_offset": -18000,
  "current": {
    "dt": 1684929490,
    "sunrise": 1684926645,
    "sunset": 1684977332,
    "temp": 292.55,
    "feels_like": 292.87,
    "pressure": 1014,
    "humidity": 89,
    "dew_point": 290.69,
    "uvi": 0.16,
    "clouds": 53,
    "visibility": 10000,
    "wind_speed": 3.13,
    "wind_deg": 93,
    "wind_gust": 6.71,
    "weather": [
      {
        "id": 803,
        "main": "Clouds",
        "description": "broken clouds",
        "icon": "04d"
      }
    ]
  },
  "minutely": [
    {
      "dt": 1684929540,
      "precipitation": 0
    }
  ],
  "hourly": [
    {
      "dt": 1684926000,
      "temp": 292.01,
      "feels_like": 292.33,
      "pressure": 1014,
      "humidity": 91,
      "dew_point": 290.51,
      "uvi": 0,
      "clouds": 54,
      "visibility": 10000,
      "wind_speed": 2.58,
      "wind_deg": 86,
      "wind_gust": 5.88,
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "pop": 0.15
    }
  ],
  "daily": [
    {
      "dt": 1684951200,
      "sunrise": 1684926645,
      "sunset": 1684977332,
      "moonrise": 1684941060,
      "moonset": 1684905480,
      "moon_phase": 0.16,
      "summary": "Expect a day of partly cloudy with rain",
      "temp": {
        "day": 299.03,
        "min": 290.69,
        "max": 300.35,
        "night": 291.45,
        "eve": 297.51,
        "morn": 292.55
      },
      "feels_like": {
        "day": 299.21,
        "night": 291.37,
        "eve": 297.86,
        "morn": 292.87
      },
      "pressure": 1016,
      "humidity": 59,
      "dew_point": 290.48,
      "wind_speed": 3.98,
      "wind_deg": 76,
      "wind_gust": 8.92,
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": 92,
      "pop": 0.47,
      "rain": 0.15,
      "uvi": 9.23
    }
  ],
  "alerts": [
    {
      "sender_name": "NWS Philadelphia - Mount Holly (New Jersey, Delaware, Southeastern Pennsylvania)",
      "event": "Small Craft Advisory",
      "start": 1684952747,
      "end": 1684988747,
      "description": "...SMALL CRAFT ADVISORY REMAINS IN EFFECT FROM 5 PM THIS AFTERNOON TO 3 AM EST FRIDAY...",
      "tags": []
    }
  ]
}
```

## Response Fields

> If a parameter does not appear in the response, that weather phenomenon did not occur (or was not measured/calculated) for the selected location and time.

### Root

- `lat`: Latitude of the location, decimal (`-90` to `90`)
- `lon`: Longitude of the location, decimal (`-180` to `180`)
- `timezone`: Timezone name for the requested location
- `timezone_offset`: Shift in seconds from UTC

### `current`

- `current.dt`: Current time, Unix, UTC
- `current.sunrise`: Sunrise time, Unix, UTC (omitted for polar day/night when applicable)
- `current.sunset`: Sunset time, Unix, UTC (omitted for polar day/night when applicable)
- `current.temp`: Temperature (`kelvin` by default, `°C` in metric, `°F` in imperial)
- `current.feels_like`: Human-perceived temperature
- `current.pressure`: Atmospheric pressure at sea level, hPa
- `current.humidity`: Humidity, %
- `current.dew_point`: Dew point
- `current.clouds`: Cloudiness, %
- `current.uvi`: Current UV index
- `current.visibility`: Average visibility, meters (max `10 km`)
- `current.wind_speed`: Wind speed
- `current.wind_gust`: Wind gust (when available)
- `current.wind_deg`: Wind direction, meteorological degrees
- `current.rain.1h`: Precipitation, mm/h (when available)
- `current.snow.1h`: Precipitation, mm/h (when available)
- `current.weather.id`: Weather condition ID
- `current.weather.main`: Group of weather parameters (e.g. Rain, Snow)
- `current.weather.description`: Weather condition description
- `current.weather.icon`: Weather icon ID

### `minutely`

- `minutely.dt`: Forecast time, Unix, UTC
- `minutely.precipitation`: Precipitation, mm/h

### `hourly`

- `hourly.dt`: Forecast time, Unix, UTC
- `hourly.temp`: Temperature
- `hourly.feels_like`: Human-perceived temperature
- `hourly.pressure`: Atmospheric pressure at sea level, hPa
- `hourly.humidity`: Humidity, %
- `hourly.dew_point`: Dew point
- `hourly.uvi`: UV index
- `hourly.clouds`: Cloudiness, %
- `hourly.visibility`: Average visibility, meters (max `10 km`)
- `hourly.wind_speed`: Wind speed
- `hourly.wind_gust`: Wind gust (when available)
- `hourly.wind_deg`: Wind direction, meteorological degrees
- `hourly.pop`: Probability of precipitation (`0` to `1`)
- `hourly.rain.1h`: Precipitation, mm/h (when available)
- `hourly.snow.1h`: Precipitation, mm/h (when available)
- `hourly.weather.id`: Weather condition ID
- `hourly.weather.main`: Group of weather parameters
- `hourly.weather.description`: Weather condition description
- `hourly.weather.icon`: Weather icon ID

### `daily`

- `daily.dt`: Forecast time, Unix, UTC
- `daily.sunrise`: Sunrise time, Unix, UTC (omitted for polar day/night when applicable)
- `daily.sunset`: Sunset time, Unix, UTC (omitted for polar day/night when applicable)
- `daily.moonrise`: Moonrise time, Unix, UTC
- `daily.moonset`: Moonset time, Unix, UTC
- `daily.moon_phase`: Moon phase
  - `0` and `1`: new moon
  - `0.25`: first quarter
  - `0.5`: full moon
  - `0.75`: last quarter
- `daily.summary`: Human-readable description of weather conditions for the day
- `daily.temp.morn`: Morning temperature
- `daily.temp.day`: Day temperature
- `daily.temp.eve`: Evening temperature
- `daily.temp.night`: Night temperature
- `daily.temp.min`: Minimum daily temperature
- `daily.temp.max`: Maximum daily temperature
- `daily.feels_like.morn`: Morning feels-like temperature
- `daily.feels_like.day`: Day feels-like temperature
- `daily.feels_like.eve`: Evening feels-like temperature
- `daily.feels_like.night`: Night feels-like temperature
- `daily.pressure`: Atmospheric pressure at sea level, hPa
- `daily.humidity`: Humidity, %
- `daily.dew_point`: Dew point
- `daily.wind_speed`: Wind speed
- `daily.wind_gust`: Wind gust (when available)
- `daily.wind_deg`: Wind direction, meteorological degrees
- `daily.clouds`: Cloudiness, %
- `daily.uvi`: Maximum UV index for the day
- `daily.pop`: Probability of precipitation (`0` to `1`)
- `daily.rain`: Rain volume, mm (when available)
- `daily.snow`: Snow volume, mm (when available)
- `daily.weather.id`: Weather condition ID
- `daily.weather.main`: Group of weather parameters
- `daily.weather.description`: Weather condition description
- `daily.weather.icon`: Weather icon ID

### `alerts`

- `alerts.sender_name`: Alert source name
- `alerts.event`: Alert event name
- `alerts.start`: Start date/time, Unix, UTC
- `alerts.end`: End date/time, Unix, UTC
- `alerts.description`: Alert description
- `alerts.tags`: Severe weather tags

> National weather alerts are provided in English by default. Some agencies may provide alert descriptions only in a local language.

---

# 2) Weather Data for Timestamp (`timemachine`)

Use this endpoint to get weather data for any timestamp from **1979-01-01** through **4 days ahead**.

## API Call

```http
https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `lat` | Yes | Latitude, decimal (`-90` to `90`) |
| `lon` | Yes | Longitude, decimal (`-180` to `180`) |
| `dt` | Yes | Unix timestamp in UTC, e.g. `1586468027`. Data available from `1979-01-01` to 4 days ahead. |
| `appid` | Yes | Your API key |
| `units` | No | `standard`, `metric`, `imperial`. Default: `standard` |
| `lang` | No | Output language |

> One API response contains weather data for **one specified timestamp only**.

## Example API Call

```http
https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=39.099724&lon=-94.578331&dt=1643803200&appid={API key}
```

## Example API Response

```json
{
  "lat": 52.2297,
  "lon": 21.0122,
  "timezone": "Europe/Warsaw",
  "timezone_offset": 3600,
  "data": [
    {
      "dt": 1645888976,
      "sunrise": 1645853361,
      "sunset": 1645891727,
      "temp": 279.13,
      "feels_like": 276.44,
      "pressure": 1029,
      "humidity": 64,
      "dew_point": 272.88,
      "uvi": 0.06,
      "clouds": 0,
      "visibility": 10000,
      "wind_speed": 3.6,
      "wind_deg": 340,
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ]
    }
  ]
}
```

## Response Fields

- `lat`: Latitude of the location
- `lon`: Longitude of the location
- `timezone`: Timezone name for the location
- `timezone_offset`: Shift in seconds from UTC
- `data.dt`: Requested time, Unix, UTC
- `data.sunrise`: Sunrise time, Unix, UTC (if applicable)
- `data.sunset`: Sunset time, Unix, UTC (if applicable)
- `data.temp`: Temperature
- `data.feels_like`: Human-perceived temperature
- `data.pressure`: Atmospheric pressure, hPa
- `data.humidity`: Humidity, %
- `data.dew_point`: Dew point
- `data.clouds`: Cloudiness, %
- `data.uvi`: UV index
  - Historical UV data is only available for the previous **5 days**.
  - For historical UVI data starting from **2020-09-20**, OpenWeather asks users to contact them.
- `data.visibility`: Average visibility, meters
- `data.wind_speed`: Wind speed
- `data.wind_gust`: Wind gust (when available)
- `data.wind_deg`: Wind direction, meteorological degrees
- `data.weather.id`: Weather condition ID
- `data.weather.main`: Group of weather parameters
- `data.weather.description`: Weather condition description
- `data.weather.icon`: Weather icon ID
- `data.rain.1h`: Precipitation, mm/h (when available)
- `data.snow.1h`: Precipitation, mm/h (when available)

---

# 3) Daily Aggregation (`day_summary`)

Use this endpoint to get aggregated weather data for a particular date from **1979-01-02** through **1.5 years ahead**.

## API Call

```http
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={API key}
```

If the service detects the timezone incorrectly, you can provide it manually:

```http
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&tz={tz}&appid={API key}
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `lat` | Yes | Latitude, decimal (`-90` to `90`) |
| `lon` | Yes | Longitude, decimal (`-180` to `180`) |
| `date` | Yes | Date in `YYYY-MM-DD` format. Available from `1979-01-02` through 1.5 years ahead of the current date. |
| `appid` | Yes | Your API key |
| `units` | No | `standard`, `metric`, `imperial`. Default: `standard` |
| `lang` | No | Output language |
| `tz` | No | Timezone override in `±XX:XX` format |

> If `tz` is specified, afternoon/night/evening/morning temperatures, pressure, and humidity are returned using the specified timezone.

## Example API Calls

```http
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=60.45&lon=-38.67&date=2023-03-30&tz=+03:00&appid={API key}
```

```http
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=39.099724&lon=-94.578331&date=2020-03-04&appid={API key}
```

## Example API Response

```json
{
  "lat": 33,
  "lon": 35,
  "tz": "+02:00",
  "date": "2020-03-04",
  "units": "standard",
  "cloud_cover": {
    "afternoon": 0
  },
  "humidity": {
    "afternoon": 33
  },
  "precipitation": {
    "total": 0
  },
  "temperature": {
    "min": 286.48,
    "max": 299.24,
    "afternoon": 296.15,
    "night": 289.56,
    "evening": 295.93,
    "morning": 287.59
  },
  "pressure": {
    "afternoon": 1015
  },
  "wind": {
    "max": {
      "speed": 8.7,
      "direction": 120
    }
  }
}
```

## Response Fields

- `lat`: Latitude of the location
- `lon`: Longitude of the location
- `tz`: Timezone in `±XX:XX` format
- `date`: Requested date in `YYYY-MM-DD` format
- `units`: Units used in the request

### `cloud_cover`

- `cloud_cover.afternoon`: Cloud cover at `12:00`, %

### `humidity`

- `humidity.afternoon`: Relative humidity at `12:00`, %

### `precipitation`

- `precipitation.total`: Total liquid water equivalent precipitation for the day, mm

### `pressure`

- `pressure.afternoon`: Atmospheric pressure at `12:00`, hPa

### `temperature`

- `temperature.min`: Minimum temperature for the day
- `temperature.max`: Maximum temperature for the day
- `temperature.afternoon`: Temperature at `12:00`
- `temperature.night`: Temperature at `00:00`
- `temperature.evening`: Temperature at `18:00`
- `temperature.morning`: Temperature at `06:00`

### `wind`

- `wind.max.speed`: Maximum wind speed for the day
- `wind.max.direction`: Cardinal direction (meteorological degrees) corresponding to maximum wind speed

---

# 4) Weather Overview (`overview`)

This endpoint returns a human-readable weather summary for **today** or **tomorrow** using OpenWeather AI technologies.

## API Call

```http
https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API key}
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `lat` | Yes | Latitude, decimal (`-90` to `90`) |
| `lon` | Yes | Longitude, decimal (`-180` to `180`) |
| `appid` | Yes | Your API key |
| `date` | No | Date in `YYYY-MM-DD` format. Available only for today and tomorrow. If not specified, the current date is used. The date is determined using the timezone for the provided coordinates. |
| `units` | No | `standard`, `metric`, `imperial`. Default: `standard` |

## Example API Call

```http
https://api.openweathermap.org/data/3.0/onecall/overview?lon=-11.8092&lat=51.509865&appid={API key}
```

## Example API Response

```json
{
  "lat": 51.509865,
  "lon": -0.118092,
  "tz": "+01:00",
  "date": "2024-05-13",
  "units": "metric",
  "weather_overview": "The current weather is overcast with a temperature of 16°C and a feels-like temperature of 16°C. The wind speed is 4 meter/sec with gusts up to 6 meter/sec coming from the west-southwest direction. The air pressure is at 1007 hPa with a humidity level of 79%. The dew point is at 12°C and the visibility is 10000 meters. The UV index is at 4, indicating moderate risk from the sun's UV rays. The sky is covered with overcast clouds, and there is no precipitation expected at the moment. Overall, it is a moderately cool and cloudy day with light to moderate winds from the west-southwest."
}
```

## Response Fields

- `lat`: Latitude of the location
- `lon`: Longitude of the location
- `tz`: Timezone in `±XX:XX` format
- `date`: Date for which the summary is generated (`YYYY-MM-DD`)
- `units`: Units specified in the request
- `weather_overview`: AI-generated weather overview for the requested date

---

# 5) AI Weather Assistant

The **AI Weather Assistant** provides weather data and weather-related advice in a human-readable format.

If you are interested in other functionality in One Call API 3.0, refer back to [Product Concept](#product-concept).

The AI Weather Assistant is available:

- via **API**, for direct integration into applications and workflows
- via a **web interface**, to experiment with prompts and understand behavior before implementation

> **Pricing note**
>
> All interactions with the AI Assistant endpoint are **free of charge**. However, the AI Weather Assistant retrieves weather information from the **Current & Forecast** endpoint of One Call API 3.0, and those requests count toward your One Call API 3.0 usage statistics.

Currently, the AI Weather Assistant considers:

- Current weather
- Minutely forecast
- Hourly forecast
- Daily forecast for the next 7 days

It supports **global coverage** and accepts:

- cities
- provinces
- countries

The assistant remembers the location you are asking about and reuses it in future questions until a new location is specified.

## Example Questions

- "What's the weather in London like?"
- "Is it a good idea to go for a swim?"
- "Will it rain tomorrow in Paris?"
- "What should my 8-year-old child wear?"
- "Where is it better to go on holiday next weekend: London or Paris?"

The AI Weather Assistant understands **50+ languages**, including English, French, Italian, German, Chinese, Arabic, and Hindi.

> The AI Weather Assistant is a work in progress and is continuously being enhanced.

---

## 5.1 Web Interface

Use the web interface to explore the assistant in a chatbot-style experience.

### URL

```http
https://openweathermap.org/weather-assistant?apikey={API key}
```

### Parameter

| Parameter | Required | Description |
|---|---|---|
| `api_key` | Yes | Your unique OpenWeather API key |

After successful validation of the API key, you will be redirected to the default chat page, where you can start asking weather-related questions.

---

## 5.2 API Endpoints

### Step 1: Start a Session

Start a session and ask an initial weather-related question.

- **Method**: `POST`
- **Headers**:
  - `Content-Type: application/json`
  - `X-Api-Key: [your OpenWeather API key]`
- **URL**:

```http
https://api.openweathermap.org/assistant/session
```

#### Example Request Body

```json
{
  "prompt": "What's weather like in London?"
}
```

#### Parameters

| Parameter | Required | Description |
|---|---|---|
| `prompt` | Yes | A question about weather or weather-based activities. If location is omitted, the assistant asks the user to specify it. |

#### Example API Response

```json
{
  "answer": "Hello! Right now in London, it's quite cloudy with overcast skies. The temperature is around 9.5°C, but it feels a little cooler at 9.2°C. The humidity is at 91%, so it might feel a bit damp. Winds are light at 1.54 m/s coming from the southwest. With these conditions, it's a cozy day to perhaps enjoy indoor activities or a calm walk with a warm jacket. If you're heading out, there's no rain reported at the moment, but it's a good idea to keep an umbrella handy just in case. Stay cozy and enjoy your day in London!",
  "data": {
    "London": {
      "Current UTC Time": "15 January 2025, 14:25",
      "Current Week Day UTC": "Wednesday",
      "clouds": 100,
      "dew_point": 281.26,
      "dt": 1736951146,
      "feels_like": 282.19,
      "humidity": 91,
      "pressure": 1034,
      "sunrise": 1736927957,
      "sunset": 1736958011,
      "temp": 282.65,
      "uvi": 0.43,
      "visibility": 10000,
      "weather": [
        {
          "description": "overcast clouds",
          "icon": "04d",
          "id": 804,
          "main": "Clouds"
        }
      ],
      "wind_deg": 240,
      "wind_speed": 1.54
    }
  },
  "session_id": "d47d2211-f1cf-409c-8297-617d74945571"
}
```

#### Response Fields

- `answer`: LLM-generated answer to the prompt
- `data`: Weather data used to generate the answer
  - Only sections relevant to the period mentioned in the prompt are included.
  - If the user continues asking about the same location, `data` may be empty.
  - If a different location or forecast type is requested, `data` will contain updated weather data.
- `session_id`: ID of the conversation session

The weather structures returned in `data` follow the same conventions as the One Call API 3.0 objects such as:

- current weather
- minutely forecast
- hourly forecast
- daily forecast
- alerts

This includes familiar fields such as:

- `lat`, `lon`, `timezone`, `timezone_offset`
- `current.*`
- `minutely.*`
- `hourly.*`
- `daily.*`
- `alerts.*`

### Step 2: Resume a Session

Resume an existing conversation while preserving previous messages and location context.

- **Method**: `POST`
- **Headers**:
  - `Content-Type: application/json`
  - `X-Api-Key: [your OpenWeather API key]`
- **URL**:

```http
https://api.openweathermap.org/assistant/session/{session_id}
```

#### Example Request Body

```json
{
  "prompt": "Do I need a hat?"
}
```

#### Parameters

| Parameter | Required | Description |
|---|---|---|
| `prompt` | Yes | A question about the weather or weather-related activities. If no location was provided in the initial request, the assistant asks for it. |

#### Example API Response

```json
{
  "answer": "Given the mild temperature of around 9.76°C in London and the gentle north wind at 2.68 m/s, wearing a hat could be a good idea, especially if you tend to feel a bit chilly or if you're sensitive to cooler weather. Plus, a hat can add a nice style touch to your outfit! Stay cozy and enjoy your day, whatever you choose! 😊",
  "data": {},
  "session_id": "xxxxxxxxx"
}
```

#### Response Fields

- `answer`: LLM-generated answer to the prompt
- `data`: Weather data used to generate the answer
- `session_id`: ID of the conversation session

> To reset context, start a **new session** instead of resuming the existing one.

---

# Other Features

## Weather Condition Codes

OpenWeather provides a list of weather condition codes with icons covering categories such as:

- thunderstorm
- drizzle
- rain
- snow
- clouds
- atmosphere

## Units of Measurement

Available unit systems:

- `standard`
- `metric`
- `imperial`

### API Call

```http
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}
```

### Parameter

| Parameter | Required | Description |
|---|---|---|
| `units` | No | Units of measurement. If omitted, `standard` is used by default. |

### Unit Details

- **Imperial**: Fahrenheit for temperature, miles/hour for wind speed
- **Metric**: Celsius for temperature, meter/sec for wind speed
- **Standard (default)**: Kelvin for temperature, meter/sec for wind speed

### Examples

**Standard (default)**

```http
api.openweathermap.org/data/3.0/onecall?lat=30.489772&lon=-99.771335
```

**Metric**

```http
api.openweathermap.org/data/3.0/onecall?lat=30.489772&lon=-99.771335&units=metric
```

**Imperial**

```http
api.openweathermap.org/data/3.0/onecall?lat=30.489772&lon=-99.771335&units=imperial
```

## Multilingual Support

Use `lang` to receive translated weather descriptions.

### API Call

```http
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&lang={lang}
```

### Parameter

| Parameter | Required | Description |
|---|---|---|
| `lang` | No | Output language code |

### Example API Call

```http
https://api.openweathermap.org/data/3.0/onecall?lat=30.489772&lon=-99.771335&lang=zh_cn
```

### Supported Languages

| Code | Language |
|---|---|
| `sq` | Albanian |
| `af` | Afrikaans |
| `ar` | Arabic |
| `az` | Azerbaijani |
| `eu` | Basque |
| `be` | Belarusian |
| `bg` | Bulgarian |
| `ca` | Catalan |
| `zh_cn` | Chinese Simplified |
| `zh_tw` | Chinese Traditional |
| `hr` | Croatian |
| `cz` | Czech |
| `da` | Danish |
| `nl` | Dutch |
| `en` | English |
| `fi` | Finnish |
| `fr` | French |
| `gl` | Galician |
| `de` | German |
| `el` | Greek |
| `he` | Hebrew |
| `hi` | Hindi |
| `hu` | Hungarian |
| `is` | Icelandic |
| `id` | Indonesian |
| `it` | Italian |
| `ja` | Japanese |
| `kr` | Korean |
| `ku` | Kurmanji (Kurdish) |
| `la` | Latvian |
| `lt` | Lithuanian |
| `mk` | Macedonian |
| `no` | Norwegian |
| `fa` | Persian (Farsi) |
| `pl` | Polish |
| `pt` | Portuguese |
| `pt_br` | Português Brasil |
| `ro` | Romanian |
| `ru` | Russian |
| `sr` | Serbian |
| `sk` | Slovak |
| `sl` | Slovenian |
| `sp`, `es` | Spanish |
| `sv`, `se` | Swedish |
| `th` | Thai |
| `tr` | Turkish |
| `ua`, `uk` | Ukrainian |
| `vi` | Vietnamese |
| `zu` | Zulu |

## List of National Weather Alert Sources

| Country | Agency |
|---|---|
| Albania | Institute of GeoSciences, Energy, Water and Environment of Albania |
| Algeria | National Meteorological Office |
| Argentina | National Weather Service of Argentina |
| Australia | Australian Bureau of Meteorology |
| Austria | Central Institute for Meteorology and Geodynamics; Water Balance Department |
| Bahrain | Bahrain Meteorological Directorate |
| Barbados | Barbados Meteorological Service |
| Belarus | State institution "Republican center for hydrometeorology, control of radioactive contamination and environmental monitoring" (Belhydromet) |
| Belgium | Royal Meteorological Institute |
| Belize | National Meteorological Service of Belize |
| Benin | National Meteorological Agency (METEO-BENIN) |
| Bosnia and Herzegovina | Federal Hydrometeorological Institute of BiH; Republic Hydrometeorological Institute |
| Botswana | Botswana Meteorological Services |
| Brazil | National Meteorological Institute - INMET |
| Bulgaria | National Institute of Meteorology and Hydrology - Plovdiv branch |
| Cameroon | Cameroon National Meteorological Service |
| Canada | Alberta Emergency Management Agency; Meteorological Service of Canada; Quebec Ministry of Public Safety; Yukon Emergency Measures Organization; Manitoba Emergency Management Organization |
| Chile | Meteorological Directorate of Chile |
| Congo | National Civil Aviation Agency (ANAC Congo) |
| Costa Rica | National Meteorological Institute of Costa Rica |
| Croatia | State Hydrometeorological Institute (DHMZ) |
| Curacao and Sint Maarten | Meteorological Department Curacao |
| Cyprus | Republic of Cyprus - Department of Meteorology |
| Czech Republic | Czech Hydrometeorological Institute |
| Denmark | Danish Meteorological Institute |
| Ecuador | Ecuadoran Institute for Meteorology and Hydrology (INAMHI) |
| Egypt | Egyptian Meteorological Authority |
| Estonia | Estonian Environment Agency |
| Eswatini | Eswatini Meteorological Service |
| Finland | Finnish Meteorological Institute |
| France | Meteo-France |
| Gabon | General Directorate of Meteorology of Gabon |
| Germany | German Meteorological Office |
| Ghana | Ghana Meteorological Agency |
| Greece | Hellenic National Meteorological Service |
| Guinea | National Meteorological Agency of Guinea |
| Guyana | Hydrometeorological Service of Guyana |
| Hong Kong China | Hong Kong Observatory |
| Hungary | Hungarian Meteorological Service |
| Iceland | Icelandic Meteorological Office |
| India | India Meteorological Department |
| Indonesia | Agency for Meteorology Climatology and Geophysics of Republic Indonesia (BMKG); InaTEWS BMKG |
| Ireland | Met Eireann - Irish Meteorological Service |
| Israel | Israel Meteorological Service |
| Italy | Italian Air Force National Meteorological Service |
| Ivory Coast | Airport, aeronautical and meteorological operating and development company (SODEXAM) |
| Jamaica | Meteorological Service of Jamaica |
| Japan | Japan Meteorological Business Support Center |
| Jordan | Jordanian Meteorological Department |
| Kazakhstan | National Hydrometeorological Service of the Republic of Kazakhstan (Kazhydromet) |
| Kenya | Kenya Meteorological Department |
| Kuwait | Kuwait Meteorological Department |
| Latvia | Latvian Environment, Geology and Meteorology Center |
| Lesotho | Lesotho Meteorological Services |
| Libya | Libyan National Meteorological Center |
| Lithuania | Lithuanian Hydrometeorological Service under the Ministry of Environment of the Republic of Lithuania (LHMS) |
| Luxembourg | Luxembourg Airport Administration |
| Macao China | Macao Meteorological and Geophysical Bureau |
| Madagascar | METEO Madagascar |
| Malawi | Malawi Department of Climate Change and Meteorological Services |
| Maldives | Maldives Meteorological Service |
| Mauritania | National Meteorological Office of Mauritania |
| Mauritius | Mauritius Meteorological Services |
| Mexico | CONAGUA - National Meteorological Service of Mexico |
| Moldova | State Hydrometeorological Service of Moldova |
| Mongolia | National Agency Meteorology and the Environmental Monitoring of Mongolia |
| Mozambique | National Institute of Meteorology of Mozambique |
| Myanmar | Myanmar Department of Meteorology and Hydrology |
| Netherlands | Royal Netherlands Meteorological Institute (KNMI) |
| New Zealand | Meteorological Service of New Zealand Limited; National Emergency Management Agency; Fire and Emergency New Zealand; Civil Defence Emergency Management (CDEM) Groups; New Zealand Emergency Mobile Alert |
| Niger | National Meteorological Directorate of Niger |
| Nigeria | Nigerian Meteorological Agency (NiMet) |
| North Macedonia | National Hydrometeorological Service - Republic of Macedonia |
| Norway | Norwegian Meteorological Institute; Norwegian Water Resources and Energy Directorate |
| Paraguay | Directorate of Meteorology and Hydrology |
| Philippines | Philippine Atmospheric Geophysical and Astronomical Services Administration |
| Poland | Institute of Meteorology and Water Management (IMGW-PIB) |
| Portugal | Portuguese Institute of Sea and Atmosphere, I.P. |
| Qatar | Qatar Meteorology Department |
| Republic of Korea | Korea Meteorological Administration, Weather Information |
| Romania | National Meteorological Administration |
| Russia | Hydrometcenter of Russia |
| Saudi Arabia | National Center for Meteorology - Kingdom of Saudi Arabia |
| Serbia | Republic Hydrometeorological Service of Serbia |
| Seychelles | Seychelles Meteorological Authority |
| Singapore | Meteorological Service Singapore |
| Slovakia | Slovak Hydrometeorological Institute |
| Slovenia | National Meteorological Service of Slovenia |
| Solomon Islands | Solomon Islands Meteorological Services |
| South Africa | South African Weather Service (SAWS) |
| Spain | State Meteorological Agency (AEMET) |
| Sudan | Sudan Meteorological Authority |
| Sweden | Swedish Meteorological and Hydrological Institute |
| Switzerland | MeteoSwiss |
| Tanzania | Tanzania Meteorological Authority |
| Thailand | Thai Meteorological Department |
| Timor-Leste | National Directorate of Meteorology and Geophysics of Timor-Leste |
| Trinidad and Tobago | Trinidad and Tobago Meteorological Service |
| Ukraine | Ukrainian Hydrometeorological Center |
| United Arab Emirates (UAE) | National Center of Meteorology (NCM), United Arab Emirates |
| United Kingdom of Great Britain and Northern Ireland | UK Met Office |
| Uruguay | Uruguayan Institute of Meteorology |
| USA | Environmental Protection Agency (EPA), Air Quality Alerts; Integrated Public Alert and Warning System (IPAWS); National Oceanic and Atmospheric Administration (NOAA), National Tsunami Warning Center; NOAA National Weather Service; NOAA National Weather Service - Marine Zones; U.S. Geological Survey (USGS), Volcano Hazard Program |
| Uzbekistan | Uzhydromet |
| Yemen | Yemeni Civil Aviation and Meteorology Authority (CAMA) |
| Zambia | Meteorological Department Zambia |
| Zimbabwe | Meteorological Services Department |

> Some agencies may stop providing alert information. If alerts are missing for an agency, OpenWeather asks users to contact them.

## JSONP Callback for JavaScript

You can transfer a callback function name to JSONP using the `callback` parameter.

### Example API Call

```http
api.openweathermap.org/data/3.0/onecall?lat=38.8&lon=12.09&callback=test
```

---

# API Errors

If the API call is incorrect, the API returns an error response with the structure below.

## Example Error Response

```json
{
  "cod": 400,
  "message": "Invalid date format",
  "parameters": [
    "date"
  ]
}
```

## Error Fields

- `cod`: Error code
- `message`: Error description
- `parameters` (optional): List of request parameter names related to the error
