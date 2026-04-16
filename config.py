class Config:
  #configuration principale de l'application

  # Application
  APP_NAME = "Check System"
  VERSION = "1.0"
  DEBUG = True

  # Serveur Flask
  HOST = "127.0.0.1"
  PORT = 5000

  # Monitoring
  STAT_REFRESH_INTERAL = 3 # secondes entre les mise a jour stats
  CPU_INTERVAL = 1 # seconde pour mesure CPU
  MAX_HISTORY_SIZE = 50 # nombre max de commande en historique

  #Limites d'affichage
  MAX_PROCESS_DISPLAY = 10
  MAX_SERVICES_DISPLAY = 20
  MAX_LOGS_DISPLAY = 10

  # Seuils d'alert (en pourcentage)
  CPU_WARNING_THRESHOLD = 70
  CPU_CRITICAL_THRESHOLD = 90

  RAM_WARNING_THRESHOLD = 75
  RAM_CRITICAL_THRESHOLD = 90

  DISK_WARNING_THRESHOLD = 80
  DISK_CRITICAL_THRESHOLD = 90

  TEMP_WARNING_THRESHOLD = 75 # en °C
  TEMP_CRITICAL_THRESHOLD = 85 # en °C

  # Score de santé
  HEALTH_PENALTY_CPU_HIGH = 10
  HEALTH_PENALTY_CPU_CRITICAL = 20

  HEALTH_PENALTY_RAM_HIGH = 15
  HEALTH_PENALTY_RAM_CRITICAL = 25

  HEALTH_PENALTY_DISK_HIGH = 10
  HEALTH_PENALTY_DISK_CRITICAL = 20

  HEALTH_PENALTY_TEMP_HIGH = 15

  #ping
  PING_COUNT = 2 # nombre de pings

  # securité
  REQUIRE_AUTH = False
  SECRET_KEY = "changer-en-production"

  # export
  EXPORT_DIRECTORY = "exports" # dossier pour export
  EXPORT_FORMAT = "txt"

  # interface
  COMMANDS_COLLAPSED_BY_DEFAUT = False # replier la liste des commandes
  SHOW_QUICK_STATS = True #afficher les stats rapides en header
  ENABLE_NOTIFICATIONS = True # notification javascript

  # developpemnt
  ENABLE_PROFILING = False  # Profiling des performances
  LOG_COMMANDS = True  # Logger les commandes exécutées

# categories de commandes pour filtrage
COMMAND_CATEGORIES = {
  "monitoring": ["cpu", "ram", "espace", "dashboard", "health"],
  "network": ["ping", "network", "ports"],
  "process": ["processus", "services", "kill"],
  "security": ["users", "security", "logs"],
  "diagnostic": ["sysinfo", "uptime", "temp", "battery"]
}

# messages personnalisés
MESSAGES = {
  "welcome": "🤖 Bienvenue sur Check System",
  "error_permission": "❌ Permission refusée. Droits administrateur requis",
  "error_not_found": "❌ Ressource non trouvée",
  "error_invalid_command": "❌ Commande invalide. Tapez 'help' pour l'aide",
  "success_kill": "✅ Processus arrêté avec succès",
  "info_no_battery": "🔌 Pas de batterie détectée (PC de bureau)"
}
