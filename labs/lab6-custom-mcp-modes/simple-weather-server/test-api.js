#!/usr/bin/env node

/**
 * Script de test pour le serveur MCP météo
 * Teste les appels API OpenWeatherMap avec la clé fournie
 */

const https = require('https');
const path = require('path');

// Charger les variables d'environnement depuis .env
require('dotenv').config({ path: path.join(__dirname, '.env') });

// Récupérer la clé API depuis les variables d'environnement
const API_KEY = process.env.OPENWEATHER_API_KEY;
const BASE_URL = 'api.openweathermap.org';

// Vérifier que la clé API est configurée
if (!API_KEY || API_KEY === 'votre_cle_api_ici') {
  console.error('\x1b[31m❌ ERREUR: Clé API non configurée\x1b[0m');
  console.error('\x1b[33m');
  console.error('Pour configurer la clé API:');
  console.error('1. Copiez le fichier .env.example vers .env');
  console.error('   cp .env.example .env');
  console.error('2. Éditez .env et remplacez "votre_cle_api_ici" par la vraie clé');
  console.error('3. La clé sera fournie par les organisateurs du hackathon');
  console.error('\x1b[0m');
  process.exit(1);
}

// Couleurs pour la console
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function makeRequest(path) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: BASE_URL,
      path: path,
      method: 'GET',
      headers: {
        'User-Agent': 'MCP-Weather-Server-Test/1.0'
      }
    };

    const req = https.request(options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          resolve({ status: res.statusCode, data: parsed });
        } catch (e) {
          reject(new Error(`Failed to parse response: ${e.message}`));
        }
      });
    });

    req.on('error', (error) => {
      reject(error);
    });

    req.setTimeout(10000, () => {
      req.destroy();
      reject(new Error('Request timeout'));
    });

    req.end();
  });
}

async function testCurrentWeather(city = 'Paris') {
  log(`\n🌤️  Test 1: Météo actuelle pour ${city}`, 'cyan');
  log('─'.repeat(50), 'blue');

  try {
    const path = `/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric&lang=fr`;
    const result = await makeRequest(path);

    if (result.status === 200) {
      const weather = result.data;
      log('✅ Succès !', 'green');
      log(`   Ville: ${weather.name}, ${weather.sys.country}`);
      log(`   Température: ${weather.main.temp}°C (ressenti: ${weather.main.feels_like}°C)`);
      log(`   Conditions: ${weather.weather[0].description}`);
      log(`   Humidité: ${weather.main.humidity}%`);
      log(`   Vent: ${weather.wind.speed} m/s`);
      return true;
    } else {
      log(`❌ Erreur ${result.status}: ${result.data.message || 'Unknown error'}`, 'red');
      return false;
    }
  } catch (error) {
    log(`❌ Erreur: ${error.message}`, 'red');
    return false;
  }
}

async function testForecast(city = 'Tokyo') {
  log(`\n📅 Test 2: Prévisions sur 5 jours pour ${city}`, 'cyan');
  log('─'.repeat(50), 'blue');

  try {
    const path = `/data/2.5/forecast?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric&lang=fr`;
    const result = await makeRequest(path);

    if (result.status === 200) {
      const forecast = result.data;
      log('✅ Succès !', 'green');
      log(`   Ville: ${forecast.city.name}, ${forecast.city.country}`);
      log(`   Nombre de prévisions: ${forecast.list.length}`);
      
      // Afficher les 3 premières prévisions
      log('\n   Prochaines prévisions:');
      forecast.list.slice(0, 3).forEach((item, index) => {
        const date = new Date(item.dt * 1000);
        log(`   ${index + 1}. ${date.toLocaleString('fr-FR')}`);
        log(`      ${item.main.temp}°C - ${item.weather[0].description}`);
      });
      return true;
    } else {
      log(`❌ Erreur ${result.status}: ${result.data.message || 'Unknown error'}`, 'red');
      return false;
    }
  } catch (error) {
    log(`❌ Erreur: ${error.message}`, 'red');
    return false;
  }
}

async function testAPIKey() {
  log(`\n🔑 Test 3: Validation de la clé API`, 'cyan');
  log('─'.repeat(50), 'blue');

  try {
    const path = `/data/2.5/weather?q=London&appid=${API_KEY}`;
    const result = await makeRequest(path);

    if (result.status === 200) {
      log('✅ Clé API valide et fonctionnelle !', 'green');
      return true;
    } else if (result.status === 401) {
      log('❌ Clé API invalide ou expirée', 'red');
      return false;
    } else {
      log(`⚠️  Réponse inattendue: ${result.status}`, 'yellow');
      return false;
    }
  } catch (error) {
    log(`❌ Erreur: ${error.message}`, 'red');
    return false;
  }
}

async function runAllTests() {
  log('\n╔════════════════════════════════════════════════╗', 'blue');
  log('║   Test du Serveur MCP Météo - Bobathon 2026   ║', 'blue');
  log('╚════════════════════════════════════════════════╝', 'blue');

  log('\n📋 Configuration:', 'cyan');
  log(`   Clé API: ${API_KEY.substring(0, 8)}...${API_KEY.substring(API_KEY.length - 4)}`);
  log(`   Base URL: ${BASE_URL}`);

  const results = [];

  // Test 1: Météo actuelle
  results.push(await testCurrentWeather('Paris'));
  await new Promise(resolve => setTimeout(resolve, 1000)); // Pause 1s

  // Test 2: Prévisions
  results.push(await testForecast('Tokyo'));
  await new Promise(resolve => setTimeout(resolve, 1000)); // Pause 1s

  // Test 3: Validation clé API
  results.push(await testAPIKey());

  // Résumé
  log('\n' + '═'.repeat(50), 'blue');
  log('📊 RÉSUMÉ DES TESTS', 'cyan');
  log('═'.repeat(50), 'blue');

  const passed = results.filter(r => r).length;
  const total = results.length;

  if (passed === total) {
    log(`\n✅ Tous les tests réussis ! (${passed}/${total})`, 'green');
    log('\n🎉 Le serveur MCP météo est prêt à être utilisé avec Bob !', 'green');
    log('\n💡 Prochaines étapes:', 'cyan');
    log('   1. Configurez le serveur dans Bob (.bob/mcp.json)');
    log('   2. Redémarrez VS Code');
    log('   3. Passez en mode Avancé (🛠️)');
    log('   4. Testez avec: "Quelle est la météo à Paris ?"');
  } else {
    log(`\n⚠️  ${passed}/${total} tests réussis`, 'yellow');
    if (passed === 0) {
      log('\n❌ Aucun test n\'a réussi. Vérifiez:', 'red');
      log('   - Votre connexion internet');
      log('   - La clé API fournie');
      log('   - Les logs d\'erreur ci-dessus');
    }
  }

  log('\n' + '═'.repeat(50) + '\n', 'blue');
}

// Exécuter les tests
runAllTests().catch(error => {
  log(`\n❌ Erreur fatale: ${error.message}`, 'red');
  process.exit(1);
});

// Made with Bob
