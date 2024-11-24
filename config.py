# 1. Configuration (config.py)
# Centralized configuration for the app, managing settings for APIs, database, and encryption.

import os

class Config:
    # General settings
    APP_NAME = "Ontologika InfoSphere"
    DEBUG = os.getenv("DEBUG", False)
    
    # Ontology settings
    ONTOLOGY_PATH = "ontologika/data/ontology.owl"

    # API keys
    PUBLIC_API_KEYS = {
        "news": os.getenv("NEWS_API_KEY"),
        "finance": os.getenv("FINANCE_API_KEY"),
        "weather": os.getenv("WEATHER_API_KEY"),
    }

    # Blockchain
    BLOCKCHAIN_NODE = os.getenv("BLOCKCHAIN_NODE_URL")
    PRIVATE_KEY = os.getenv("BLOCKCHAIN_PRIVATE_KEY")

    # Security settings
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
