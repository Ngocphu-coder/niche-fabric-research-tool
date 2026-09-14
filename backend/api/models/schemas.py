"""Pydantic schemas for API requests/responses"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductBase(BaseModel):
    """Base product schema"""
    title: str
    description: Optional[str] = None
    material_type: Optional[str] = None
    gsm: Optional[float] = None
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    """Product creation schema"""
    pass


class Product(ProductBase):
    """Product response schema"""
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PlatformListingBase(BaseModel):
    """Base platform listing schema"""
    platform_name: str
    platform_url: str
    price: Optional[float] = None
    currency: Optional[str] = None
    sales_volume: Optional[int] = None
    rating: Optional[float] = None


class PlatformListing(PlatformListingBase):
    """Platform listing response schema"""
    id: int
    product_id: str
    scraped_at: datetime

    class Config:
        from_attributes = True
