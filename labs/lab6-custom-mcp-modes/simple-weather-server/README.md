# 🌤️ Simple Weather MCP Server

A lightweight, easy-to-use MCP server that provides weather information to Bob AI. **No complex setup required!**

## ✨ Features

- **Works immediately in DEMO mode** - No API key needed to test!
- Get current weather for any city
- Get 5-day weather forecast
- Convert temperatures between Celsius and Fahrenheit
- Access list of popular cities worldwide
- Optional: Connect to real OpenWeatherMap API (free)

## 🚀 Quick Start (3 Steps!)

### 1. Install Dependencies

```bash
cd simple-weather-server
npm install
```

### 2. Configure Bob

Add this to your `.bob/mcp.json`:

```json
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["server.js"],
      "cwd": "/Users/benabidmhamed/Documents/IBM/2026/Projets/Crédit Agricole/Perspectives-avril/Test-Bobathon/GHBObAthon/Test_Mhamed/lab6-custom-mcp-modes/simple-weather-server",
      "disabled": false
    }
  }
}
```

### 3. Restart VS Code

That's it! The server works in DEMO mode immediately.

## 🎯 Available Tools

### 1. `get_current_weather`
Get current weather conditions for any city.

**Example prompts:**
- "What's the weather in Paris?"
- "Get current weather for Tokyo"
- "How's the weather in New York in Fahrenheit?"

**Parameters:**
- `city` (required): City name
- `units` (optional): "metric" (Celsius) or "imperial" (Fahrenheit)

### 2. `get_forecast`
Get 5-day weather forecast (8 data points, every 3 hours).

**Example prompts:**
- "Show me the forecast for London"
- "What's the weather forecast for Berlin?"
- "Get forecast for Sydney in Fahrenheit"

**Parameters:**
- `city` (required): City name
- `units` (optional): "metric" or "imperial"

### 3. `convert_temperature`
Convert temperatures between units.

**Example prompts:**
- "Convert 25 Celsius to Fahrenheit"
- "What is 72 Fahrenheit in Celsius?"

**Parameters:**
- `temperature` (required): Temperature value
- `from` (required): "celsius" or "fahrenheit"
- `to` (required): "celsius" or "fahrenheit"

## 📚 Available Resources

### `weather://cities/popular`
List of popular cities organized by continent.

**Example prompt:**
- "Show me popular cities for weather queries"

## 🔑 Optional: Real Weather Data

The server works in DEMO mode by default with mock data. To get real weather:

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up (free, takes 2 minutes)
   - Copy your API key

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Add your API key to `.env`:
```env
OPENWEATHER_API_KEY=your_actual_api_key_here
```

4. Restart VS Code

## 💬 Example Conversations with Bob

**In Advanced Mode (🛠️):**

```
You: What's the weather in Paris?
Bob: [Uses get_current_weather tool]
     Temperature: 22°C
     Description: partly cloudy
     Humidity: 65%
     Wind: 5.5 m/s

You: Show me the forecast for Tokyo
Bob: [Uses get_forecast tool]
     Next 24 hours forecast with temperatures and conditions...

You: Convert 25 Celsius to Fahrenheit
Bob: [Uses convert_temperature tool]
     25°C = 77°F
```

## 🎨 Demo Mode vs Real API

| Feature | Demo Mode | Real API |
|---------|-----------|----------|
| Setup Time | 0 minutes | 2 minutes |
| API Key Required | ❌ No | ✅ Yes (free) |
| Current Weather | ✅ Mock data | ✅ Real data |
| Forecast | ✅ Mock data | ✅ Real data |
| Temperature Conversion | ✅ Works | ✅ Works |
| City List | ✅ Works | ✅ Works |
| Cost | Free | Free (with limits) |

## 🔧 Troubleshooting

### Server not appearing in Bob?
1. ✅ Make sure you're in **Advanced mode** (🛠️)
2. ✅ Check the `cwd` path in `.bob/mcp.json`
3. ✅ Restart VS Code completely
4. ✅ Run `npm install` in the server directory

### Tools not working?
1. ✅ Confirm you're in Advanced mode
2. ✅ Check console for error messages
3. ✅ Try demo mode first (no API key needed)

### Want real weather data?
1. ✅ Get free API key from OpenWeatherMap
2. ✅ Add to `.env` file
3. ✅ Restart VS Code

## 📝 Notes

- **DEMO mode** returns realistic mock data - perfect for testing
- **Real API** has free tier: 1,000 calls/day, 60 calls/minute
- Temperature conversion works offline (no API needed)
- City list resource works offline

## 🎓 Learning Points

This simple server demonstrates:
- ✅ MCP server basics without complex dependencies
- ✅ Tool implementation with clear parameters
- ✅ Resource serving (city list)
- ✅ Graceful fallback (demo mode)
- ✅ Optional external API integration
- ✅ Error handling

Perfect for learning MCP concepts before building more complex servers!

## 📄 License

MIT