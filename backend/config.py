# Backend Configuration Management
from pydantic_settings import BaseSettings
from typing import List, Optional
import os
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings from environment variables"""

    # ========== SERVER CONFIGURATION ==========
    app_name: str = "Niche Fabric Research Tool"
    app_version: str = "0.1.0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    # ========== DATABASE CONFIGURATION ==========
    database_url: str = "sqlite:///./niche_fabric_research.db"
    sqlalchemy_echo: bool = False

    # ========== CORS CONFIGURATION ==========
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:9222",
        "http://127.0.0.1:3000",
    ]
    cors_credentials: bool = True
    cors_methods: List[str] = ["*"]
    cors_headers: List[str] = ["*"]

    # ========== LOGGING CONFIGURATION ==========
    log_level: str = "INFO"
    log_file: str = "logs/app.log"

    # ========== SCRAPER CONFIGURATION ==========
    scraper_timeout: int = 30
    scraper_max_retries: int = 3
    scraper_request_delay: float = 1.0
    scraper_max_concurrent: int = 5
    scraper_user_agents: List[str] = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    ]

    # ========== PROXY CONFIGURATION ==========
    use_proxy: bool = False
    proxy_url: Optional[str] = None
    proxy_username: Optional[str] = None
    proxy_password: Optional[str] = None

    # ========== PLATFORM CONFIGURATION ==========
    platforms_enabled: List[str] = [
        "1688",
        "taobao",
        "etsy",
        "shopee",
        "made_in_china",
        "amazon",
    ]

    # Platform URLs
    platform_1688_enabled: bool = True
    platform_1688_base_url: str = "https://www.1688.com"

    platform_taobao_enabled: bool = True
    platform_taobao_base_url: str = "https://www.taobao.com"

    platform_etsy_enabled: bool = True
    platform_etsy_base_url: str = "https://www.etsy.com"

    platform_shopee_enabled: bool = True
    platform_shopee_base_url: str = "https://shopee.com"

    platform_mic_enabled: bool = True
    platform_mic_base_url: str = "https://www.made-in-china.com"

    platform_amazon_enabled: bool = True
    platform_amazon_base_url: str = "https://www.amazon.com"
    amazon_api_key: Optional[str] = None
    amazon_api_secret: Optional[str] = None

    # ========== ML/AI CONFIGURATION ==========
    material_classifier_model_path: str = "./ml/models/material_classifier.pkl"
    feature_extractor_model_path: str = "./ml/models/feature_weights.pt"

    # Image processing
    image_max_width: int = 800
    image_max_height: int = 800
    image_quality: int = 85

    # Visual matching threshold (0-1)
    visual_match_threshold: float = 0.75

    # ========== STORAGE CONFIGURATION ==========
    image_storage_path: str = "./storage/images"
    backup_storage_path: str = "./storage/backups"

    # ========== ANALYSIS CONFIGURATION ==========
    min_sales_volume_for_opportunity: int = 100
    opportunity_score_threshold: float = 6.0
    currency_conversion_api: str = "https://api.exchangerate-api.com/v4/latest/"

    # ========== EXPORT CONFIGURATION ==========
    export_storage_path: str = "./storage/exports"
    pdf_template_path: str = "./templates/report.html"

    # ========== SECURITY ==========
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # ========== RATE LIMITING ==========
    rate_limit_enabled: bool = True
    rate_limit_per_minute: int = 60

    # ========== API KEYS ==========
    google_translate_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None

    # ========== DEVELOPMENT SETTINGS ==========
    environment: str = "development"
    reload_on_change: bool = True

    class Config:
        """Pydantic config"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def get_database_url(self) -> str:
        """Get database URL"""
        return self.database_url

    def get_proxy(self) -> Optional[dict]:
        """Get proxy configuration if enabled"""
        if self.use_proxy and self.proxy_url:
            proxy_dict = {"https": self.proxy_url, "http": self.proxy_url}
            if self.proxy_username and self.proxy_password:
                proxy_dict = {
                    "https": f"http://{self.proxy_username}:{self.proxy_password}@{self.proxy_url}",
                    "http": f"http://{self.proxy_username}:{self.proxy_password}@{self.proxy_url}",
                }
            return proxy_dict
        return None

    def get_enabled_platforms(self) -> List[str]:
        """Get list of enabled platforms"""
        enabled = []
        if self.platform_1688_enabled:
            enabled.append("1688")
        if self.platform_taobao_enabled:
            enabled.append("taobao")
        if self.platform_etsy_enabled:
            enabled.append("etsy")
        if self.platform_shopee_enabled:
            enabled.append("shopee")
        if self.platform_mic_enabled:
            enabled.append("made_in_china")
        if self.platform_amazon_enabled:
            enabled.append("amazon")
        return enabled

    def is_production(self) -> bool:
        """Check if running in production"""
        return self.environment == "production"

    def is_development(self) -> bool:
        """Check if running in development"""
        return self.environment == "development"


@lru_cache()
def get_settings() -> Settings:
    """Get settings instance (cached)"""
    return Settings()


# Create settings instance
settings = get_settings()
