class Config:
    # config principale de l'application
    
    # Aplication
    APP_NAME = "Check System"
    APP_VERSION = "1.0.0"
    DEBUG = True
    
    # serveur flask
    FLASK_HOST = "127.0.0.1"
    FLASK_PORT = 5000
    
    #Monitoring
    STAT_REFRESH_INTERVAL = 3  # en secondes
    CPU_INTERVAL = 1  # en secondes pou CPU
    MAX_HISTORY_SIZE = 50 # nombre max de commande en historique 
    
    #Limites d'affichage
    MAX_PROCESSES_DISPLAY = 10 
    MAX_SERVICES_DISPLAY = 20
    MAX_LOGS_DISPLAY = 10
    
    #Seuils d'alerte
    CPU_WARNING_THRESHOLD = 70  # en pourcentage
    CPU_CRITICAL_THRESHOLD = 90  # en pourcentage
    
    
    RAM_WARNING_THRESHOLD = 75 # en pourcentage
    RAM_CRITICAL_THRESHOLD = 90  # en pourcentage
    
    
    DISK_WARNING_THRESHOLD = 80  # en pourcentage
    DISK_CRITICAL_THRESHOLD = 90  # en pourcentage
    
    TEMPERATURE_WARNING_THRESHOLD = 75  # en degrés Celsius
    TEMPERATURE_CRITICAL_THRESHOLD = 90  # en degrés Celsius
    
    
    #score de santé
    HEALTH_PENALTY_HIGH_CPU = 10
    HEALTH_PENALTY_CRITICAL_CPU = 20
    
    HEALTH_PENALTY_HIGH_RAM = 10
    HEALTH_PENALTY_CRITICAL_RAM = 20
    
    HEALTH_PENALTY_HIGH_DISK = 10
    HEALTH_PENALTY_CRITICAL_DISK = 20
    
    HEALTH_PENALTY_HIGH_TEMP = 15
    
    #ping
    PING_COUNT = 2 # nombre de ping à envoyer pour le test de connectivité
    
    #securité
    REQUIRE_AUTH = False  # activer ou désactiver l'authentification pour accéder à l'application
    SECRET_KEY = "votre_clé_secrète_ici"  # clé secrète pour les sessions Flask (à changer en production)
    
    #export
    EXPORT_DIR = "exports"  # répertoire où les exports seront sauvegardés
    EXPORT_FORMAT = "txt" # format d'export (txt, csv, json)
    
    #interface 
    COMMANDS_COLLAPSED_BY_DEFAUT = False
    SHOW_QUICK_STATS = True
    ENABLE_NOTIFICATIONS = True
    
    #development
    ENABLE_PROFILING = False  # activer ou désactiver le profiling pour les performances
    LOG_COMMANDS = True  # activer ou désactiver le logging des commandes exécutées
    
# categories de commandes pour le filtrage
COMMAND_CATEGORIES = {
    "monitoring": ["cpu", "ram", "espace", "dashboard","health"],
    "network": ["ping", "network", "ports"],
    "process": ["processus", "services","kill"],
    "security": ["users", "security", "logs"],
    "diagnostic": ["sysinfo", "uptime", "temp", "battery"]
}

# messages personalises

MESSAGES = {
    "welcome": "🤖​ Bienvenue sur Check System !",
    "error_permission": "❌ Vous n'avez pas la permission d'accéder à cette ressource.",
    "error_not_found": "❌ Ressource non trouvée.",
    "error_server": "❌ Une erreur est survenue côté serveur.",
    "error_invalid_command": "❌ Commande invalide ou paramètres manquants.",
    "success_kill": "✅ Processus arrêté avec succès.",
    "info_no_battery": "🔌​ Aucune batterie détectée sur ce système.",
}