"""Scraper factory for creating scraper instances"""
from typing import Dict, Type, Optional
from .base_scraper import BaseScraper


class ScraperFactory:
    """Factory for creating scraper instances"""

    _scrapers: Dict[str, Type[BaseScraper]] = {}

    @classmethod
    def register(cls, platform: str, scraper_class: Type[BaseScraper]):
        """Register a scraper class"""
        cls._scrapers[platform.lower()] = scraper_class

    @classmethod
    def create(cls, platform: str) -> Optional[BaseScraper]:
        """Create a scraper instance"""
        scraper_class = cls._scrapers.get(platform.lower())
        if scraper_class:
            return scraper_class(platform)
        return None

    @classmethod
    def get_available_platforms(cls) -> list:
        """Get list of available platforms"""
        return list(cls._scrapers.keys())
