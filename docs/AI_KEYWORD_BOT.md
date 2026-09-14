# 🤖 AI Keyword Generation Bot Integration

## 1. OVERVIEW

The **AI Keyword Generation Bot** is an intelligent background service that automatically generates, expands, and optimizes search keywords for niche fabric products. It runs asynchronously in the backend and intelligently queues scraping tasks across multiple platforms.

### Key Capabilities
- 🌐 **Bilingual Support**: English & Vietnamese keyword generation
- 🔄 **Keyword Expansion**: Contextual keyword variations and synonyms
- 📊 **Auto-Suggest Integration**: Real-time trending keywords from Amazon & 1688
- 🔗 **Smart Queue Management**: Automatic task queuing and prioritization
- 🎯 **Opportunity Detection**: Direct integration with Approval Workspace
- 📈 **Trend Analysis**: Monitor keyword popularity and demand signals

---

## 2. ARCHITECTURE UPDATES

### 2.1 Backend Module Structure

```
backend/
├── ai/                              # NEW: AI & Keyword Module
│   ├── __init__.py
│   ├── keyword_generator.py         # Main keyword generation engine
│   ├── keyword_expander.py          # Keyword expansion & synonyms
│   ├── trend_analyzer.py            # Trend detection from platforms
│   ├── queue_manager.py             # Intelligent queue management
│   ├── auto_suggest.py              # Amazon & 1688 suggestion scraper
│   ├── language_processor.py        # Bilingual processing (EN/VI)
│   ├── materialization_mapper.py    # Material-to-keyword mapping
│   └── models/
│       ├── keyword_vocabulary.json  # Prebuilt keyword database
│       └── material_taxonomy.json   # Material type taxonomy
│
├── tasks/                           # UPDATED: Background Tasks
│   ├── __init__.py
│   ├── celery_app.py               # Celery configuration (NEW)
│   ├── keyword_tasks.py            # Keyword generation tasks (NEW)
│   └── scraping_tasks.py           # Scraping orchestration (NEW)
│
└── database/
    └── models.py                    # UPDATED: Add keyword & queue models
```

### 2.2 Data Flow Architecture

```
┌────────────────────────────────────────────────────────��────┐
│          FRONTEND - Approval Workspace / Dashboard           │
└─────────────────────────────────────┬───────────────────────┘
                                      ↑
                    ┌─────────────────┴──────────────────┐
                    │                                    │
        ┌───────────▼──────────┐          ┌─────────────▼─────────┐
        │  Manual Keyword      │          │  AI Bot Auto Results  │
        │  Input               │          │  (Approval Queue)     │
        └───────────┬──────────┘          └─────────────▲─────────┘
                    │                                    │
                    └────────────────┬───────────────────┘
                                     ↓
                    ┌─────────────────────────────────────┐
                    │   BACKEND - AI Keyword Bot          │
                    └─────────────────────────────────────┘
                                     │
        ┌────────────┬───────────────┼────────────┬────────────┐
        ↓            ↓               ↓            ↓            ↓
    ┌───────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
    │Keyword│  │Keyword   │  │Trend     │  │Language  │  │Material  │
    │Gene-  │  │Expander  │  │Analyzer  │  │Processor │  │Mapper    │
    │rator  │  │          │  │          │  │          │  │          │
    └───────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘
        │            │            │            │            │
        └────────────┴────────────┴────────────┴────────────┘
                         │
                    ┌────▼────┐
                    │  Queue   │
                    │ Manager  │
                    └────┬────┘
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
    ┌────────┐      ┌────────┐      ┌────────┐
    │1688    │      │Taobao  │      │Amazon  │
    │Scraper │      │Scraper │      │Scraper │
    └────────┘      └────────┘      └────────┘
        │                ↓                ↓
        └────────────────┼────────────────┘
                         │
                ┌────────▼────────┐
                │  Gap Detection  │
                │  & Opportunity  │
                │  Scoring        │
                └────────┬────────┘
                         │
                ┌────────▼───────────┐
                │ Approval Workspace │
                │ (Auto-populated)   │
                └────────────────────┘
```

### 2.3 Database Schema Updates

```sql
-- Keyword Generation Table
CREATE TABLE keywords (
    id INTEGER PRIMARY KEY,
    keyword VARCHAR(255) UNIQUE,
    keyword_vi VARCHAR(255),          -- Vietnamese version
    category VARCHAR(100),             -- Fabric category
    language VARCHAR(10),              -- 'en', 'vi'
    source VARCHAR(50),                -- 'manual', 'generated', 'trend'
    search_volume INTEGER,
    difficulty_score FLOAT,            -- 0-100 (SEO difficulty)
    trend_score FLOAT,                 -- 0-100 (trending indicator)
    material_type VARCHAR(100),
    related_keywords TEXT,             -- JSON array of related keywords
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT True
);

-- Queue Management Table
CREATE TABLE scraping_queue (
    id INTEGER PRIMARY KEY,
    keyword_id INTEGER,
    keyword VARCHAR(255),
    platforms VARCHAR(500),            -- JSON array
    priority INTEGER DEFAULT 5,        -- 1-10 (higher = more important)
    status VARCHAR(50),                -- 'pending', 'processing', 'completed', 'failed'
    source VARCHAR(50),                -- 'manual', 'ai_generated', 'trending'
    scheduled_at TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    result_count INTEGER,
    error_message TEXT,
    retry_count INTEGER DEFAULT 0,
    max_retries INTEGER DEFAULT 3,
    created_at TIMESTAMP,
    FOREIGN KEY (keyword_id) REFERENCES keywords(id)
);

-- Auto-Suggest Cache Table
CREATE TABLE keyword_suggestions (
    id INTEGER PRIMARY KEY,
    suggestion_text VARCHAR(255),
    platform VARCHAR(50),              -- 'amazon', '1688'
    category VARCHAR(100),
    search_volume INTEGER,
    trend_direction VARCHAR(20),       -- 'up', 'down', 'stable'
    last_scraped_at TIMESTAMP,
    created_at TIMESTAMP
);

-- AI Bot Activity Log
CREATE TABLE ai_bot_logs (
    id INTEGER PRIMARY KEY,
    action VARCHAR(100),               -- 'keyword_generated', 'queue_created', 'suggestion_fetched'
    keywords_count INTEGER,
    queue_items_created INTEGER,
    execution_time_ms INTEGER,
    status VARCHAR(50),                -- 'success', 'partial_success', 'failed'
    error_message TEXT,
    created_at TIMESTAMP
);
```

---

## 3. AI KEYWORD GENERATION BOT COMPONENTS

### 3.1 Keyword Generator (`keyword_generator.py`)

```python
# Core keyword generation engine
class AIKeywordGenerator:
    """Main AI engine for keyword generation"""
    
    def __init__(self):
        self.vocabulary = load_vocabulary()
        self.material_taxonomy = load_material_taxonomy()
        self.language_processor = LanguageProcessor()
    
    async def generate_keywords(self, seed_keyword: str, 
                               category: str, 
                               language: str = 'en') -> List[str]:
        """Generate keyword variations"""
        # Core logic
        
    async def batch_generate(self, categories: List[str]) -> Dict:
        """Generate keywords for multiple categories"""
        # Batch processing logic
```

**Features:**
- Seed-based keyword generation
- Category-specific expansion
- Synonym & variant generation
- Bilingual support (EN ↔ VI)

### 3.2 Keyword Expander (`keyword_expander.py`)

```python
class KeywordExpander:
    """Expand keywords with contextual variations"""
    
    async def expand_keyword(self, keyword: str) -> List[str]:
        """Generate keyword variations"""
        # Variations:
        # - "goat coat" → "goat coats", "goat coat jacket", "goat wool coat"
        # - With material: "oxford goat coat", "canvas goat coat"
        # - Compound: "outdoor goat coat", "waterproof goat coat"
```

**Expansion Strategies:**
- Pluralization & variations
- Material + product combinations
- Feature + product combinations
- Size/color variants
- Related product expansions

### 3.3 Trend Analyzer (`trend_analyzer.py`)

```python
class TrendAnalyzer:
    """Analyze trending keywords from platforms"""
    
    async def fetch_trending_keywords(self, platform: str) -> List[Dict]:
        """Fetch trending search terms"""
        # Scrape search suggestions from:
        # - Amazon: autocomplete API
        # - 1688: trending searches
```

### 3.4 Queue Manager (`queue_manager.py`)

```python
class QueueManager:
    """Intelligent queue management for scraping tasks"""
    
    async def enqueue_keywords(self, keywords: List[str], 
                              priority: int = 5) -> List[str]:
        """Add keywords to processing queue"""
        
    async def prioritize_queue(self) -> None:
        """Dynamically reprioritize queue based on:
        - Search volume
        - Trend score
        - Manual prioritization
        - Difficulty score
        """
        
    async def get_next_batch(self, batch_size: int = 10):
        """Get next batch for processing"""
```

### 3.5 Language Processor (`language_processor.py`)

```python
class LanguageProcessor:
    """Bilingual keyword processing"""
    
    async def translate_keyword(self, keyword: str, 
                               from_lang: str, 
                               to_lang: str) -> str:
        """Translate keywords EN ↔ VI"""
        
    async def normalize_language(self, text: str) -> str:
        """Normalize text for consistency"""
```

### 3.6 Material Mapper (`materialization_mapper.py`)

```python
class MaterialMapper:
    """Map materials to related keywords"""
    
    async def get_keywords_for_material(self, material: str) -> List[str]:
        """Get all relevant keywords for a material"""
        # E.g., "Oxford" → ["oxford cloth", "oxford fabric", 
        #                     "oxford cover", "oxford tarp"]
        
    async def get_material_variants(self, material: str) -> List[str]:
        """Get material variations"""
```

---

## 4. BACKGROUND TASK ORCHESTRATION

### 4.1 Celery Integration

```python
# backend/tasks/celery_app.py
from celery import Celery
from celery.schedules import crontab

app = Celery('niche_fabric_research')

# Periodic Tasks Configuration
app.conf.beat_schedule = {
    'generate-keywords-daily': {
        'task': 'tasks.keyword_tasks.generate_daily_keywords',
        'schedule': crontab(hour=0, minute=0),  # 00:00 daily
    },
    'fetch-trending-keywords-4h': {
        'task': 'tasks.keyword_tasks.fetch_trending_keywords',
        'schedule': crontab(minute=0, hour='*/4'),  # Every 4 hours
    },
    'process-keyword-queue': {
        'task': 'tasks.scraping_tasks.process_keyword_queue',
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
    },
    'analyze-queue-performance': {
        'task': 'tasks.keyword_tasks.analyze_queue_performance',
        'schedule': crontab(hour=23, minute=59),  # Daily at 23:59
    },
}
```

### 4.2 Keyword Tasks

```python
# backend/tasks/keyword_tasks.py
@app.task
async def generate_daily_keywords():
    """Generate keywords for all fabric categories daily"""
    
@app.task
async def fetch_trending_keywords():
    """Fetch trending keywords from Amazon & 1688"""
    
@app.task
async def expand_keyword_batch(keywords: List[str]):
    """Batch expand keywords"""
    
@app.task
async def analyze_queue_performance():
    """Analyze queue processing performance"""
```

### 4.3 Scraping Task Orchestration

```python
# backend/tasks/scraping_tasks.py
@app.task
async def process_keyword_queue():
    """Process pending keywords in queue"""
    # 1. Get next batch from queue
    # 2. Distribute to scrapers
    # 3. Collect & normalize results
    # 4. Perform gap analysis
    # 5. Push to approval workspace
    
@app.task
async def scrape_keyword_multi_platform(keyword: str, platforms: List[str]):
    """Scrape single keyword across platforms"""
```

---

## 5. API ENDPOINTS FOR AI BOT

### 5.1 New Endpoints

```
POST /api/ai/keywords/generate
  Request:
    {
      "seed_keyword": "goat coat",
      "category": "pet-clothing",
      "language": "en",
      "count": 20
    }
  Response:
    {
      "keywords": [...],
      "variations": {...}
    }

GET /api/ai/keywords/trending
  Query params: platform (amazon|1688), limit
  Response:
    {
      "trending": [...]
    }

POST /api/ai/queue/enqueue
  Request:
    {
      "keywords": [...],
      "priority": 7,
      "platforms": ["1688", "taobao", "amazon"]
    }
  Response:
    {
      "queue_ids": [...],
      "total_enqueued": 15
    }

GET /api/ai/queue/status
  Response:
    {
      "pending_count": 50,
      "processing_count": 5,
      "completed_today": 120,
      "average_time_per_keyword": 45  # seconds
    }

GET /api/ai/bot/logs
  Query params: limit, offset, action_type
  Response:
    {
      "logs": [...]
    }
```

---

## 6. MATERIAL TAXONOMY & KEYWORD DATABASE

### 6.1 Material Taxonomy (`material_taxonomy.json`)

```json
{
  "fabrics": {
    "oxford": {
      "keywords": ["oxford cloth", "oxford fabric", "oxford cover"],
      "aliases": ["oxford weave"],
      "related_materials": ["canvas", "cotton"]
    },
    "canvas": {
      "keywords": ["canvas fabric", "canvas cloth", "canvas material"],
      "aliases": ["canvas weave"],
      "related_materials": ["oxford", "cotton"]
    },
    "pvc": {
      "keywords": ["PVC coating", "PVC fabric", "PVC cover"],
      "aliases": ["polyvinyl chloride"],
      "related_materials": ["nylon", "polyester"]
    }
  },
  "categories": {
    "pet-clothing": {
      "products": ["goat coat", "horse blanket", "dog jacket"],
      "materials": ["oxford", "canvas", "fleece"],
      "keywords": ["pet apparel", "animal wear"]
    },
    "outdoor-covers": {
      "products": ["equipment cover", "generator cover", "furniture cover"],
      "materials": ["oxford", "canvas", "pvc"],
      "keywords": ["outdoor protection", "weatherproof cover"]
    }
  }
}
```

### 6.2 Keyword Vocabulary (`keyword_vocabulary.json`)

```json
{
  "en": {
    "pet-clothing": ["goat coat", "horse blanket", "dog vest", ...],
    "outdoor-covers": ["generator cover", "AC unit cover", ...]
  },
  "vi": {
    "pet-clothing": ["áo dê", "chăn ngựa", "áo chó", ...],
    "outdoor-covers": ["bạt máy phát", "bạt máy lạnh", ...]
  }
}
```

---

## 7. WORKFLOW EXAMPLE

```
1. User Triggers (Manual or Scheduled):
   └─> Calls: POST /api/ai/keywords/generate
   
2. AI Keyword Generator:
   ├─> Generate 20 keyword variations
   ├─> Translate to Vietnamese
   └─> Assign priority scores based on:
       - Search volume
       - Trending score
       - Difficulty level

3. Queue Manager:
   ├─> Create scraping queue entries
   └─> Sort by priority

4. Background Task (Celery):
   ├─> Every 15 min: GET next 10 keywords from queue
   ├─> Trigger parallel scraping across platforms
   ├─> Collect & normalize results
   └─> Perform gap analysis

5. Opportunity Detection:
   ├─> Identify gaps (Amazon X, Taobao V)
   ├─> Calculate opportunity score
   └─> Push to Approval Workspace

6. User Review:
   └─> User sees auto-populated results
       └─> Approve/Reject with 1 click
```

---

## 8. PERFORMANCE METRICS

### Monitoring KPIs
- Keywords generated per hour
- Queue processing time
- Gap detection accuracy
- Approval rate of AI suggestions
- False positive rate
- Average time to market (keyword to approval)

### Logging & Telemetry
- Track all keyword generations
- Monitor queue performance
- Log suggestion sources
- Record approval/rejection feedback

---

## 9. INTEGRATION WITH EXISTING MODULES

### With Search Service
- Direct integration with `SearchService`
- Auto-trigger scraping on keyword generation

### With Approval Workflow
- Auto-populate staging area with AI results
- Tag results with "AI Generated" badge
- Track approval rate for ML feedback

### With Analytics
- Dashboard widget showing:
  - Daily keywords generated
  - Queue status in real-time
  - Top performing keywords
  - Trending keywords today

---

## Document Version: 1.1
**Last Updated**: 2024
**Status**: AI Bot Integration Complete
**Related Files**: ROADMAP.md (Phase 1.5), ARCHITECTURE.md
