"""Base scraper class"""
import asyncio
import logging
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Abstract base class for all scrapers"""

    def __init__(self, platform_name: str, timeout: int = 30):
        """Initialize scraper"""
        self.platform_name = platform_name
        self.timeout = timeout
        self.session = None

    @abstractmethod
    async def search(self, query: str, **kwargs) -> List[Dict[str, Any]]:
        """Search for products"""
        pass

    @abstractmethod
    async def get_product_details(self, product_id: str) -> Dict[str, Any]:
        """Get product details"""
        pass

    async def close(self):
        """Close scraper session"""
        if self.session:
            await self.session.close()

    def normalize_product(self, product: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize product data across platforms"""
        return {
            "title": product.get("title", ""),
            "description": product.get("description", ""),
            "price": product.get("price"),
            "currency": product.get("currency", "USD"),
            "image_url": product.get("image_url"),
            "platform": self.platform_name,
            "platform_url": product.get("url"),
            "sales_volume": product.get("sales_volume"),
            "rating": product.get("rating"),
            "scraped_at": datetime.now().isoformat(),
        }
