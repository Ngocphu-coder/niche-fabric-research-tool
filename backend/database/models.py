"""SQLAlchemy ORM models"""
from sqlalchemy import Column, String, Text, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


class Product(Base):
    """Product model"""
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    title = Column(String(500), index=True)
    description = Column(Text)
    material_type = Column(String(100))
    gsm = Column(Float)
    image_url = Column(String(500))
    image_local_path = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    listings = relationship("PlatformListing", back_populates="product")


class PlatformListing(Base):
    """Platform listing model"""
    __tablename__ = "platform_listings"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), index=True)
    platform_name = Column(String(50), index=True)
    platform_url = Column(String(500))
    platform_product_id = Column(String(200))
    price = Column(Float)
    currency = Column(String(10))
    sales_volume = Column(Integer)
    rating = Column(Float)
    stock_status = Column(String(50))
    scraped_at = Column(DateTime, default=datetime.utcnow, index=True)

    product = relationship("Product", back_populates="listings")


class ApprovalWorkflow(Base):
    """Approval workflow model"""
    __tablename__ = "approval_workflow"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), index=True)
    status = Column(String(50), default="pending", index=True)
    approval_reason = Column(Text)
    rejection_reason = Column(Text)
    approved_by = Column(String(100))
    approved_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
