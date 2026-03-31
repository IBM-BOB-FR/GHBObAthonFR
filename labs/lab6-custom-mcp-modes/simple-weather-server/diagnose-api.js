#!/usr/bin/env node

/**
 * Script de diagnostic pour le serveur MCP météo
 * Vérifie la configuration et la connectivité API
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Clé API fournie pour les participants du Bobathon
const API_KEY = '***REMOVED***';

// Couleurs pour la console
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  magenta: '\x1b[35m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function checkFile(filePath, description) {
  const fullPath = path.join(__dirname, filePath);
  const exists = fs.existsSync(fullPath);
  
  if (exists) {
    log(`✅ ${description}: ${filePath}`, 'green');
    return true;
  } else {
    log(`❌ ${description} manquant: ${filePath}`, 'red');
    return false;
  }
}

function checkNodeModules() {
  const modulesPath = path.join(__dirname, 'node_modules');
  const exists = fs.existsSync(modulesPath);
  
  if (exists) {
    log('✅ node_modules installé', 'green');
    
    // Vérifier les dépendances clés
    const requiredModules = [
      '@modelcontextprotocol/sdk',
      'dotenv'
    ];
    
    let allPresent = true;
    requiredModules.forEach(mod => {
      const modPath = path.join(modulesPath, mod);
      if (fs.existsSync(modPath)) {
        log(`   ✓ ${mod}`, 'green');
      } else {
        log(`   ✗ ${mod} manquant`, 'red');
        allPresent = false;
      }
    });
    
    return allPresent;
  } else {
    log('❌ node_modules non installé', 'red');
    log('   Exécutez: npm install', 'yellow');
    return false;
  }
}

function testAPIConnection() {
  return new Promise((resolve) => {
    log('\n🔌 Test de connexion API...', 'cyan');
    
    const options = {
      hostname: 'api.openweathermap.org',
      path: `/data/2.5/weather?q=Paris&appid=${API_KEY}`,
      method: 'GET',
      timeout: 5000
    };

    const req = https.request(options, (res) => {
      let data = '';
      
      res.on('data', (chunk) => {
        data += chunk;
      });
      
      res.on('end', () => {
        if (res.statusCode === 200) {
          log('✅ Connexion API réussie', 'green');
          log(`   Code: ${res.statusCode}`, 'green');
          resolve(true);
        } else if (res.statusCode === 401) {
          log('❌ Clé API invalide', 'red');
          log(`   Code: ${res.statusCode}`, 'red');
          resolve(false);
        } else {
          log(`⚠️  Réponse inattendue: ${res.statusCode}`, 'yellow');
          resolve(false);
        }
      });
    });

    req.on('error', (error) => {
      log(`❌ Erreur de connexion: ${error.message}`, 'red');
      resolve(false);
    });

    req.on('timeout', () => {
      req.destroy();
      log('❌ Timeout de connexion', 'red');
      resolve(false);
    });

    req.end();
  });
}

function checkEnvironment() {
  log('\n🔍 Vérification de l\'environnement', 'cyan');
  log('─'.repeat(50), 'blue');
  
  // Node.js version
  const nodeVersion = process.version;
  log(`Node.js: ${nodeVersion}`, nodeVersion.startsWith('v14') || nodeVersion.startsWith('v16') || nodeVersion.startsWith('v18') || nodeVersion.startsWith('v20') ? 'green' : 'yellow');
  
  // Système d'exploitation
  log(`OS: ${process.platform} ${process.arch}`, 'green');
  
  // Répertoire de travail
  log(`Répertoire: ${__dirname}`, 'green');
}

function displayAPIInfo() {
  log('\n📋 Informations API', 'cyan');
  log('─'.repeat(50), 'blue');
  log(`Clé API: ${API_KEY.substring(0, 8)}...${API_KEY.substring(API_KEY.length - 4)}`);
  log('Provider: OpenWeatherMap');
  log('Plan: Gratuit (1000 appels/jour, 60/minute)');
  log('Documentation: https://openweathermap.org/api');
}

function displayNextSteps(allChecksPass) {
  log('\n📝 Prochaines étapes', 'cyan');
  log('─'.repeat(50), 'blue');
  
  if (allChecksPass) {
    log('✅ Tout est prêt ! Vous pouvez:', 'green');
    log('   1. Tester l\'API: node test-api.js', 'cyan');
    log('   2. Démarrer le serveur: node server.js', 'cyan');
    log('   3. Configurer dans Bob (.bob/mcp.json)', 'cyan');
    log('   4. Redémarrer VS Code', 'cyan');
    log('   5. Passer en mode Avancé (🛠️)', 'cyan');
  } else {
    log('⚠️  Actions requises:', 'yellow');
    log('   1. Installer les dépendances: npm install', 'yellow');
    log('   2. Vérifier la connexion internet', 'yellow');
    log('   3. Relancer ce diagnostic', 'yellow');
  }
}

async function runDiagnostic() {
  log('\n╔════════════════════════════════════════════════╗', 'magenta');
  log('║     Diagnostic Serveur MCP Météo - Bobathon   ║', 'magenta');
  log('╚════════════════════════════════════════════════╝', 'magenta');

  // 1. Vérification de l'environnement
  checkEnvironment();

  // 2. Vérification des fichiers
  log('\n📁 Vérification des fichiers', 'cyan');
  log('─'.repeat(50), 'blue');
  
  const fileChecks = [
    checkFile('server.js', 'Serveur MCP'),
    checkFile('package.json', 'Configuration npm'),
    checkFile('.env.example', 'Exemple de configuration')
  ];

  // 3. Vérification des dépendances
  log('\n📦 Vérification des dépendances', 'cyan');
  log('─'.repeat(50), 'blue');
  const modulesCheck = checkNodeModules();

  // 4. Informations API
  displayAPIInfo();

  // 5. Test de connexion API
  const apiCheck = await testAPIConnection();

  // 6. Résumé
  log('\n' + '═'.repeat(50), 'blue');
  log('📊 RÉSUMÉ DU DIAGNOSTIC', 'cyan');
  log('═'.repeat(50), 'blue');

  const allChecksPass = fileChecks.every(c => c) && modulesCheck && apiCheck;

  if (allChecksPass) {
    log('\n✅ Diagnostic réussi ! Le serveur est prêt.', 'green');
  } else {
    log('\n⚠️  Certaines vérifications ont échoué.', 'yellow');
  }

  // 7. Prochaines étapes
  displayNextSteps(allChecksPass);

  log('\n' + '═'.repeat(50) + '\n', 'blue');

  return allChecksPass;
}

// Exécuter le diagnostic
runDiagnostic()
  .then(success => {
    process.exit(success ? 0 : 1);
  })
  .catch(error => {
    log(`\n❌ Erreur fatale: ${error.message}`, 'red');
    process.exit(1);
  });

// Made with Bob
