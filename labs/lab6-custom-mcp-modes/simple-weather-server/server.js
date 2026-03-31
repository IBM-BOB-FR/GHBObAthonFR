#!/usr/bin/env node

/**
 * Simple Weather MCP Server
 * 
 * A lightweight MCP server that provides weather information using OpenWeatherMap API.
 * No complex external dependencies - just a free API key needed!
 * 
 * Features:
 * - Get current weather for any city
 * - Get weather forecast
 * - Convert temperature units
 * - Simple and easy to set up
 */

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} = require('@modelcontextprotocol/sdk/types.js');

require('dotenv').config();

/**
 * Simple Weather MCP Server Implementation
 */
class WeatherMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'simple-weather-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
          resources: {},
        },
      }
    );

    this.apiKey = process.env.OPENWEATHER_API_KEY || 'demo';
    this.baseUrl = 'https://api.openweathermap.org/data/2.5';
    
    this.setupHandlers();
  }

  /**
   * Setup MCP protocol handlers
   */
  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'get_current_weather',
            description: 'Get current weather for a city',
            inputSchema: {
              type: 'object',
              properties: {
                city: {
                  type: 'string',
                  description: 'City name (e.g., "Paris", "New York")',
                },
                units: {
                  type: 'string',
                  description: 'Temperature units: metric (Celsius) or imperial (Fahrenheit)',
                  enum: ['metric', 'imperial'],
                  default: 'metric',
                },
              },
              required: ['city'],
            },
          },
          {
            name: 'get_forecast',
            description: 'Get 5-day weather forecast for a city',
            inputSchema: {
              type: 'object',
              properties: {
                city: {
                  type: 'string',
                  description: 'City name',
                },
                units: {
                  type: 'string',
                  description: 'Temperature units: metric or imperial',
                  enum: ['metric', 'imperial'],
                  default: 'metric',
                },
              },
              required: ['city'],
            },
          },
          {
            name: 'convert_temperature',
            description: 'Convert temperature between Celsius and Fahrenheit',
            inputSchema: {
              type: 'object',
              properties: {
                temperature: {
                  type: 'number',
                  description: 'Temperature value',
                },
                from: {
                  type: 'string',
                  description: 'Source unit',
                  enum: ['celsius', 'fahrenheit'],
                },
                to: {
                  type: 'string',
                  description: 'Target unit',
                  enum: ['celsius', 'fahrenheit'],
                },
              },
              required: ['temperature', 'from', 'to'],
            },
          },
        ],
      };
    });

    // Execute tool
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        let result;
        
        switch (name) {
          case 'get_current_weather':
            result = await this.getCurrentWeather(args.city, args.units || 'metric');
            break;
          case 'get_forecast':
            result = await this.getForecast(args.city, args.units || 'metric');
            break;
          case 'convert_temperature':
            result = this.convertTemperature(args.temperature, args.from, args.to);
            break;
          default:
            throw new Error(`Unknown tool: ${name}`);
        }

        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    });

    // List resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: 'weather://cities/popular',
            name: 'Popular Cities',
            description: 'List of popular cities for weather queries',
            mimeType: 'application/json',
          },
        ],
      };
    });

    // Read resource
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const { uri } = request.params;

      if (uri === 'weather://cities/popular') {
        const cities = {
          europe: ['Paris', 'London', 'Berlin', 'Madrid', 'Rome'],
          americas: ['New York', 'Los Angeles', 'Toronto', 'Mexico City', 'São Paulo'],
          asia: ['Tokyo', 'Beijing', 'Mumbai', 'Seoul', 'Bangkok'],
          africa: ['Cairo', 'Lagos', 'Johannesburg', 'Nairobi', 'Casablanca'],
          oceania: ['Sydney', 'Melbourne', 'Auckland', 'Brisbane', 'Perth'],
        };

        return {
          contents: [
            {
              uri,
              mimeType: 'application/json',
              text: JSON.stringify(cities, null, 2),
            },
          ],
        };
      }

      throw new Error(`Unknown resource: ${uri}`);
    });
  }

  /**
   * Get current weather for a city
   */
  async getCurrentWeather(city, units = 'metric') {
    if (this.apiKey === 'demo') {
      // Return mock data for demo mode
      return this.getMockWeather(city, units);
    }

    const url = `${this.baseUrl}/weather?q=${encodeURIComponent(city)}&units=${units}&appid=${this.apiKey}`;
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`Weather API error: ${response.statusText}`);
    }

    const data = await response.json();
    
    return {
      city: data.name,
      country: data.sys.country,
      temperature: data.main.temp,
      feels_like: data.main.feels_like,
      humidity: data.main.humidity,
      pressure: data.main.pressure,
      description: data.weather[0].description,
      wind_speed: data.wind.speed,
      units: units === 'metric' ? '°C' : '°F',
      timestamp: new Date(data.dt * 1000).toISOString(),
    };
  }

  /**
   * Get weather forecast
   */
  async getForecast(city, units = 'metric') {
    if (this.apiKey === 'demo') {
      return this.getMockForecast(city, units);
    }

    const url = `${this.baseUrl}/forecast?q=${encodeURIComponent(city)}&units=${units}&appid=${this.apiKey}`;
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`Weather API error: ${response.statusText}`);
    }

    const data = await response.json();
    
    return {
      city: data.city.name,
      country: data.city.country,
      forecast: data.list.slice(0, 8).map(item => ({
        datetime: new Date(item.dt * 1000).toISOString(),
        temperature: item.main.temp,
        description: item.weather[0].description,
        humidity: item.main.humidity,
        wind_speed: item.wind.speed,
      })),
      units: units === 'metric' ? '°C' : '°F',
    };
  }

  /**
   * Convert temperature between units
   */
  convertTemperature(temp, from, to) {
    if (from === to) {
      return { temperature: temp, unit: to };
    }

    let result;
    if (from === 'celsius' && to === 'fahrenheit') {
      result = (temp * 9/5) + 32;
    } else if (from === 'fahrenheit' && to === 'celsius') {
      result = (temp - 32) * 5/9;
    }

    return {
      original: { value: temp, unit: from },
      converted: { value: Math.round(result * 10) / 10, unit: to },
    };
  }

  /**
   * Mock weather data for demo mode
   */
  getMockWeather(city, units) {
    const temp = units === 'metric' ? 22 : 72;
    return {
      city: city,
      country: 'DEMO',
      temperature: temp,
      feels_like: temp - 2,
      humidity: 65,
      pressure: 1013,
      description: 'partly cloudy',
      wind_speed: 5.5,
      units: units === 'metric' ? '°C' : '°F',
      timestamp: new Date().toISOString(),
      note: 'This is mock data. Set OPENWEATHER_API_KEY for real data.',
    };
  }

  /**
   * Mock forecast data for demo mode
   */
  getMockForecast(city, units) {
    const baseTemp = units === 'metric' ? 20 : 68;
    const forecast = [];
    
    for (let i = 0; i < 8; i++) {
      const date = new Date();
      date.setHours(date.getHours() + (i * 3));
      
      forecast.push({
        datetime: date.toISOString(),
        temperature: baseTemp + Math.random() * 5,
        description: ['sunny', 'cloudy', 'partly cloudy'][i % 3],
        humidity: 60 + Math.random() * 20,
        wind_speed: 3 + Math.random() * 5,
      });
    }

    return {
      city: city,
      country: 'DEMO',
      forecast: forecast,
      units: units === 'metric' ? '°C' : '°F',
      note: 'This is mock data. Set OPENWEATHER_API_KEY for real data.',
    };
  }

  /**
   * Start the MCP server
   */
  async start() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    
    if (this.apiKey === 'demo') {
      console.error('⚠️  Running in DEMO mode. Set OPENWEATHER_API_KEY for real weather data.');
    } else {
      console.error('✅ Weather MCP Server started with API key');
    }
  }
}

/**
 * Main entry point
 */
async function main() {
  try {
    const server = new WeatherMCPServer();
    await server.start();
  } catch (error) {
    console.error('Failed to start server:', error.message);
    process.exit(1);
  }
}

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.error('Shutting down gracefully...');
  process.exit(0);
});

process.on('SIGTERM', () => {
  console.error('Shutting down gracefully...');
  process.exit(0);
});

// Start the server
if (require.main === module) {
  main();
}

module.exports = WeatherMCPServer;

// Made with Bob
