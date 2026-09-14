# 🏗️ Multi-Platform Niche Fabric Research Tool - System Architecture

## 1. HIGH-LEVEL ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────┐
│                    DESKTOP APPLICATION (Electron)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         FRONTEND LAYER (React + Redux/Context)           │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ • Search Interface (Keyword/Image Input)                  │   │
│  │ • Cross-Platform Gap Matrix Viewer                        │   │
│  │ • Approval Workspace (Staging Area)                       │   │
│  │ • Analytics Dashboard                                     │   │
│  │ • Settings & Configuration Panel                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↓↑                                  │
│                    IPC Bridge (Electron)                         │
│                              ↓↑                                  │
└─────────────────────────────────────────────────────────────────┘
                                 ↓↑
┌─────────────────────────────────────────────────────────────────┐
│              BACKEND LAYER (Python FastAPI)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              API Routes & Services                        │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ • /api/search          - Multi-platform search           │   │
│  │ • /api/scrape          - Web scraper orchestration       │   │
│  │ • /api/analyze         - Data analysis & gap detection   │   │
│  │ • /api/approve         - Approval workflow               │   │
│  │ • /api/export          - Export results                  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↓↑                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           Processing Engines & Services                   │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │                                                            │   │
│  │  ┌───────────────────┐  ┌──────────────────────────┐     │   │
│  │  │  Scraper Module   │  │  AI/ML Module            │     │   │
│  │  ├───────────────────┤  ├──────────────────────────┤     │   │
│  │  │ • 1688 Scraper    │  │ • Visual Matching        │     │   │
│  │  │ • Taobao Scraper  │  │ • Image Recognition      │     │   │
│  │  │ • Etsy Scraper    │  │ • Material Classification│     │   │
│  │  │ • Shopee Scraper  │  │ • GSM Detection          │     │   │
│  │  │ • MIC Scraper     │  │ • Price Prediction       │     │   │
│  │  │ • Amazon Scraper  │  └──────────────────────────┘     │   │
│  │  │ • Async Queue     │                                    │   │
│  │  └───────────────────┘                                    │   │
│  │                                                            │   │
│  │  ┌──────────────────────┐  ┌─────────────────────────┐   │   │
│  │  │  Data Analysis       │  │  Storage & Cache        │   │   │
│  │  ├──────────────────────┤  ├─────────────────────────┤   │   │
│  │  │ • Gap Detection      │  │ • SQLite Database       │   │   │
│  │  │ • Cross-match Logic  │  │ • Redis Cache (opt)     │   │   │
│  │  │ • Price Comparison   │  │ • File Storage          │   │   │
│  │  │ • Trend Analysis     │  └─────────────────────────┘   │   │
│  │  └──────────────────────┘                                │   │
│  │                                                            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                                 ↓↑
┌─────────────────────────────────────────────────────────────────┐
│              EXTERNAL DATA SOURCES                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Supplier Platforms:        Verification Platform:              │
│  • 1688.com                 • Amazon.com                         │
│  • Taobao.com               • Amazon APIs (if available)         │
│  • Etsy.com                                                      │
│  • Shopee.com                                                    │
│  • Made-in-China.com                                             │
│  • AliExpress.com (optional)                                     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. TECHNOLOGY STACK

### Frontend (Electron + React)
```
Node.js/npm Ecosystem:
├── electron              (^latest) - Desktop framework
├── react                 (^18.0)   - UI library
├── react-dom             (^18.0)   - React DOM renderer
├── redux                 (^4.x)    - State management
├── react-redux           (^8.x)    - Redux binding
├── axios                 (^1.x)    - HTTP client
├── electron-store        (^8.x)    - Persistent storage
├── antd                  (^5.x)    - UI components
├── react-icons           (^4.x)    - Icon library
└── webpack               (^5.x)    - Module bundler
```

### Backend (Python FastAPI)
```
Python (^3.9):
├── fastapi               (^0.100)  - Web framework
├── uvicorn               (^0.23)   - ASGI server
├── sqlalchemy            (^2.0)    - ORM
├── pydantic              (^2.0)    - Data validation
├── aiohttp               (^3.8)    - Async HTTP client
├── beautifulsoup4        (^4.12)   - HTML parsing
├── selenium              (^4.x)    - Browser automation
├── pillow                (^10.0)   - Image processing
├── opencv-python         (^4.8)    - Computer vision
├── torch/torchvision     (^2.0)    - Deep learning (optional)
├── scikit-learn          (^1.3)    - ML algorithms
├── pandas                (^2.0)    - Data analysis
├── requests              (^2.31)   - HTTP library
├── python-dotenv         (^1.0)    - Environment config
└── pytest                (^7.x)    - Testing
```

---

## 3. DATA FLOW DIAGRAM

### Flow 1: Multi-Platform Search with Keyword
```
User Input (Keyword)
        ↓
  [Frontend - Search UI]
        ↓
  [IPC Channel: "search-request"]
        ↓
  [Backend - FastAPI: POST /api/search]
        ↓
  ┌─────────────────────────────┐
  │  Query Preparation          │
  │  • Normalize keyword        │
  │  • Translate (if needed)    │
  │  • Generate variants        │
  └─────────────────────────────┘
        ↓
  ┌─────────────────────────────┐
  │  Parallel Scraping          │
  │  • 1688 Scraper             │
  │  • Taobao Scraper           │
  │  • Etsy Scraper             │
  │  • Shopee Scraper           │
  │  • Made-in-China Scraper    │
  │  • Amazon Scraper           │
  └─────────────────────────────┘
        ↓
  ┌─────────────────────────────┐
  │  Data Filtering             │
  │  • Material classification  │
  │  • Remove non-fabric items  │
  │  • Extract metadata         │
  └─────────────────────────────┘
        ↓
  ┌─────────────────────────────┐
  │  Database Storage           │
  │  • Save to SQLite           │
  │  • Index for search         │
  └─────────────────────────────┘
        ↓
  [Response: Search Results]
        ↓
  [Frontend - Display Results]
```

### Flow 2: Image-Based Search
```
User Input (Image File)
        ↓
  [Frontend - Image Upload]
        ↓
  [IPC Channel: "image-search-request"]
        ↓
  [Backend - FastAPI: POST /api/search/image]
        ↓
  ┌─────────────────────────────┐
  │  Image Processing           │
  │  • Extract features         │
  │  • Material detection (CNN) │
  │  • Generate text keywords   │
  └─────────────────────────────┘
        ↓
  [Parallel Scraping] (same as Flow 1)
        ↓
  [Visual Matching Engine]
        ↓
  [Response: Matched Products]
```

### Flow 3: Gap Analysis & Approval Workflow
```
Scraped Products from Multiple Platforms
        ↓
  [AI Visual Matching]
  • Match same products across platforms
  • Calculate similarity scores
        ↓
  [Cross-Platform Gap Detection]
  • Platform A: [Product exists]
  • Platform B: [Product exists]
  • Amazon:    [Product missing] ← GAP DETECTED
        ↓
  [Filter & Rank Opportunities]
  • Sort by volume/sales
  • Filter by material
  • Calculate profit potential
        ↓
  [Approval Workspace (Staging Area)]
  ┌──────────────────────────────┐
  │ Product 1 | V | V | X | X     │ ← Approve/Reject
  │ Product 2 | V | X | X | V     │
  │ Product 3 | V | V | V | V     │
  └──────────────────────────────┘
        ↓
  [User Action: Approve]
        ↓
  [Move to Official List]
  • Store decision
  • Generate report
  • Export data
```

---

## 4. DATABASE SCHEMA (SQLite)

```sql
-- Products Table
CREATE TABLE products (
    id TEXT PRIMARY KEY,
    title VARCHAR(500),
    description TEXT,
    material_type VARCHAR(100),
    gsm FLOAT,
    image_url TEXT,
    image_local_path TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Platform Listings Table
CREATE TABLE platform_listings (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    platform_name VARCHAR(50),
    platform_url TEXT,
    platform_product_id VARCHAR(200),
    price FLOAT,
    currency VARCHAR(10),
    sales_volume INTEGER,
    rating FLOAT,
    stock_status VARCHAR(50),
    scraped_at TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Visual Matches Table
CREATE TABLE visual_matches (
    id INTEGER PRIMARY KEY,
    product_id_1 TEXT,
    product_id_2 TEXT,
    platform_1 VARCHAR(50),
    platform_2 VARCHAR(50),
    similarity_score FLOAT,
    match_confidence VARCHAR(50),
    matched_at TIMESTAMP,
    FOREIGN KEY (product_id_1) REFERENCES products(id),
    FOREIGN KEY (product_id_2) REFERENCES products(id)
);

-- Gap Analysis Results Table
CREATE TABLE gap_analysis (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    original_platform VARCHAR(50),
    missing_platform VARCHAR(50),
    sales_volume INTEGER,
    estimated_demand VARCHAR(50),
    opportunity_score FLOAT,
    analyzed_at TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Approval Workflow Table
CREATE TABLE approval_workflow (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    status VARCHAR(50),  -- 'pending', 'approved', 'rejected'
    approval_reason TEXT,
    rejection_reason TEXT,
    approved_by VARCHAR(100),
    approved_at TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Search History Table
CREATE TABLE search_history (
    id INTEGER PRIMARY KEY,
    search_type VARCHAR(50),  -- 'keyword', 'image'
    search_query TEXT,
    result_count INTEGER,
    execution_time_ms INTEGER,
    searched_at TIMESTAMP
);
```

---

## 5. MODULE BREAKDOWN

### 5.1 Frontend Modules (React)

```
src/
├── components/
│   ├── SearchPanel/
│   │   ├── KeywordSearch.jsx
│   │   ├── ImageSearch.jsx
│   │   └── SearchBar.jsx
│   ├── MatrixViewer/
│   │   ├── GapMatrix.jsx
│   │   ├── MatrixRow.jsx
│   │   └── MatrixFilters.jsx
│   ├── ApprovalWorkspace/
│   │   ├── StagingArea.jsx
│   │   ├── ProductCard.jsx
│   │   └── BulkApprovalActions.jsx
│   ├── Dashboard/
│   │   ├── Analytics.jsx
│   │   ├── Charts.jsx
│   │   └── Statistics.jsx
│   ├── Settings/
│   │   ├── PlatformConfig.jsx
│   │   ├── ProxySettings.jsx
│   │   └── UserPreferences.jsx
│   └── Common/
│       ├── Header.jsx
│       ├── Sidebar.jsx
│       ├── LoadingSpinner.jsx
│       └── ErrorBoundary.jsx
├── pages/
│   ├── HomePage.jsx
│   ├── SearchResultsPage.jsx
│   ├── ApprovalPage.jsx
│   ├── AnalyticsPage.jsx
│   └── SettingsPage.jsx
├── store/
│   ├── actions/
│   │   ├── searchActions.js
│   │   ├── approvalActions.js
│   │   └── analysisActions.js
│   ├── reducers/
│   │   ├── searchReducer.js
│   │   ├── approvalReducer.js
│   │   └── uiReducer.js
│   └── store.js
├── services/
│   ├── api.js
│   ├── ipcService.js
│   └── storageService.js
├── utils/
│   ├── validators.js
│   ├── formatters.js
│   └── helpers.js
├── styles/
│   ├── globals.css
│   ├── theme.css
│   └── components.css
└── App.jsx
```

### 5.2 Backend Modules (Python FastAPI)

```
backend/
├── main.py
├── config.py
├── requirements.txt
├── .env.example
│
├── api/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── search.py
│   │   ├── scrape.py
│   │   ├── analyze.py
│   │   ├── approval.py
│   │   └── export.py
│   └── models/
│       ├── __init__.py
│       ├── schemas.py
│       └── validators.py
│
├── scrapers/
│   ├── __init__.py
│   ├── base_scraper.py
│   ├── scrapers_1688.py
│   ├── scrapers_taobao.py
│   ├── scrapers_etsy.py
│   ├── scrapers_shopee.py
│   ├── scrapers_made_in_china.py
│   ├── scrapers_amazon.py
│   ├── scraper_factory.py
│   └── async_queue.py
│
├── ml/
│   ├── __init__.py
│   ├── visual_matcher.py
│   ├── image_processor.py
│   ├── material_classifier.py
│   ├── feature_extractor.py
│   └── models/
│       ├── material_classifier_model.pkl
│       └── feature_extractor_weights.pt
│
├── analysis/
│   ├── __init__.py
│   ├── gap_detector.py
│   ├── opportunity_scorer.py
│   ├── price_analyzer.py
│   └── trend_analyzer.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── crud.py
│
├── services/
│   ├── __init__.py
│   ├── search_service.py
│   ├── scraping_service.py
│   ├── analysis_service.py
│   ├── approval_service.py
│   └── export_service.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── validators.py
│   ├── formatters.py
│   ├── translator.py
│   └── proxy_manager.py
│
└── tests/
    ├── __init__.py
    ├── test_scrapers.py
    ├── test_ml_models.py
    ├── test_analysis.py
    └── test_api.py
```

---

## 6. API ENDPOINTS SPECIFICATION

### Search Endpoints
```
POST /api/search/keyword
  Request:
    {
      "query": "goat coat",
      "platforms": ["1688", "taobao", "etsy", "shopee", "amazon"],
      "material_filters": ["fabric"],
      "price_range": [10, 1000]
    }
  Response:
    {
      "search_id": "uuid",
      "status": "processing",
      "results": [...]
    }

POST /api/search/image
  Request: multipart/form-data (image file)
  Response:
    {
      "search_id": "uuid",
      "detected_materials": ["oxford", "canvas"],
      "suggested_keywords": ["outdoor cover", "equipment protection"],
      "results": [...]
    }

GET /api/search/{search_id}/status
  Response:
    {
      "search_id": "uuid",
      "status": "completed",
      "progress_percent": 100,
      "result_count": 45
    }
```

### Analysis Endpoints
```
POST /api/analyze/gaps
  Request:
    {
      "search_id": "uuid",
      "reference_platform": "amazon"
    }
  Response:
    {
      "gap_analysis_id": "uuid",
      "opportunities": [
        {
          "product_id": "...",
          "original_platform": "1688",
          "missing_platforms": ["amazon"],
          "sales_volume": 1500,
          "opportunity_score": 8.5
        }
      ]
    }

GET /api/analyze/{analysis_id}/matrix
  Response:
    {
      "matrix": [
        {
          "product_name": "...",
          "image_url": "...",
          "platforms": {
            "1688": "V",
            "taobao": "V",
            "etsy": "X",
            "shopee": "X",
            "amazon": "X"
          },
          "opportunity_rating": "High"
        }
      ]
    }
```

### Approval Endpoints
```
GET /api/approval/staging
  Response:
    {
      "pending_products": [...]
    }

POST /api/approval/{product_id}/approve
  Request:
    {
      "reason": "High volume, good margins",
      "tags": ["priority", "fast-mover"]
    }
  Response:
    {
      "status": "approved",
      "approved_at": "timestamp"
    }

POST /api/approval/{product_id}/reject
  Request:
    {
      "reason": "Limited market size"
    }
  Response:
    {
      "status": "rejected"
    }
```

### Export Endpoints
```
GET /api/export/csv
  Query params: analysis_id, format=csv
  Response: CSV file download

GET /api/export/excel
  Query params: analysis_id
  Response: Excel file download with charts

POST /api/export/pdf
  Request:
    {
      "analysis_id": "uuid",
      "include_charts": true,
      "include_images": true
    }
  Response: PDF file download
```

---

## 7. KEY DESIGN PATTERNS

### 7.1 Service Layer Pattern
- Each business logic is isolated in a service class
- Services are called by API routes
- Services coordinate between scrapers, ML models, and database

### 7.2 Factory Pattern
- Scraper factory creates appropriate scraper based on platform name
- Allows easy addition of new platforms

### 7.3 Async/Await Pattern
- All I/O operations (scraping, API calls) are asynchronous
- Parallel execution of scrapers using asyncio

### 7.4 Repository Pattern
- CRUD operations isolated in repository layer
- Database queries are centralized

### 7.5 State Management (Frontend)
- Redux for global state management
- Actions & reducers for state updates
- Middleware for async operations

---

## 8. EXTERNAL INTEGRATIONS

### 8.1 Platform APIs (if available)
- Amazon Product Advertising API (for product lookup)
- Etsy API (search & product details)
- Shopee API (if available)

### 8.2 Services
- Translation API (Google Translate) - for keyword translation
- Proxy Service - for scraper reliability
- Image Upload Service (local or cloud storage)

---

## 9. SECURITY CONSIDERATIONS

1. **User Data Protection**
   - Local SQLite database (no cloud sync without explicit user consent)
   - Encrypted storage for sensitive config (API keys, proxies)

2. **Web Scraping Ethics**
   - Respect robots.txt
   - Rate limiting (delays between requests)
   - User-Agent rotation
   - Proxy rotation to avoid IP blocking

3. **API Security**
   - CORS configuration
   - Input validation (Pydantic)
   - SQL injection prevention (SQLAlchemy ORM)

4. **Data Privacy**
   - No tracking/telemetry by default
   - Option for anonymous usage analytics

---

## 10. PERFORMANCE OPTIMIZATION

1. **Frontend**
   - Code splitting
   - Lazy loading components
   - Memoization of expensive components
   - Virtual scrolling for large lists

2. **Backend**
   - Connection pooling (database)
   - Redis caching (optional)
   - Batch processing
   - Image compression before storage

3. **Scraping**
   - Parallel requests with asyncio
   - Connection pooling
   - Request timeout management
   - Smart retry logic

---

## 11. DEPLOYMENT

### Development
```bash
# Terminal 1: Backend
cd backend && python -m uvicorn main:app --reload

# Terminal 2: Frontend (Electron)
cd frontend && npm run dev
```

### Production
```bash
# Backend: Docker container or standalone executable
# Frontend: Packaged Electron app (Windows/Mac/Linux)
```

---

## 12. MONITORING & LOGGING

- Centralized logging (Python logging module)
- Error tracking (Sentry integration - optional)
- Performance metrics (execution time, success rate)
- User activity logs (anonymized)

---

## Document Version: 1.0
**Last Updated**: 2024
**Status**: Architecture Design Complete
