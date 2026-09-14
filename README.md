# Multi-Platform Niche Fabric Research Tool

> A desktop application for multi-platform fabric product research and market gap analysis

## 🎯 Project Overview

**Multi-Platform Niche Fabric Research Tool** is a sophisticated desktop application designed to help e-commerce entrepreneurs and product researchers identify market opportunities in niche fabric products (outdoor covers, pet clothing, etc.) by analyzing cross-platform presence across supplier platforms (1688, Taobao, Etsy, Shopee, etc.) and verification platform (Amazon).

### Key Features
- 🔍 **Multi-Platform Search**: Simultaneous search across 5+ supplier platforms
- 🤖 **AI Visual Matching**: Intelligent product matching using computer vision
- 📊 **Gap Analysis Matrix**: Automatic detection of market opportunities
- ✅ **Approval Workflow**: Smart staging & decision management
- 📈 **Analytics Dashboard**: Comprehensive market insights
- 📥 **Multiple Export Formats**: CSV, Excel, PDF reports

## 🚀 Quick Start

### Prerequisites
- **Node.js** 16+ and npm
- **Python** 3.9+
- **Git**
- Windows, macOS, or Linux

### Installation

#### 1. Clone Repository
```bash
git clone https://github.com/Ngocphu-coder/niche-fabric-research-tool.git
cd niche-fabric-research-tool
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
alembic upgrade head

# Start development server
python -m uvicorn main:app --reload
```

Backend will be available at: `http://localhost:8000`

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend development server will launch automatically.

#### 4. Access Application
- Open Electron app: `npm run start` (from frontend directory)
- API Documentation: `http://localhost:8000/docs`

## 📁 Project Structure

```
niche-fabric-research-tool/
│
├── 📄 README.md                    # This file
├── 📄 ARCHITECTURE.md              # Detailed system architecture
├── 📄 ROADMAP.md                   # Development roadmap & phases
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
│
├── backend/                        # Python FastAPI Backend
│   ├── main.py                     # FastAPI application entry point
│   ├── config.py                   # Configuration management
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example               # Environment variables template
│   │
│   ├── api/                        # API routes & endpoints
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── search.py          # Search endpoints
│   │   │   ├── scrape.py          # Scraping endpoints
│   │   │   ├── analyze.py         # Analysis endpoints
│   │   │   ├── approval.py        # Approval workflow endpoints
│   │   │   └── export.py          # Export endpoints
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── schemas.py         # Pydantic schemas
│   │       └── validators.py      # Input validation
│   │
│   ├── scrapers/                   # Web scraping modules
│   │   ├── __init__.py
│   │   ├── base_scraper.py        # Base scraper class
│   │   ├── scraper_1688.py        # 1688.com scraper
│   │   ├── scraper_taobao.py      # Taobao scraper
│   │   ├── scraper_etsy.py        # Etsy scraper
│   │   ├── scraper_shopee.py      # Shopee scraper
│   │   ├── scraper_made_in_china.py
│   │   ├── scraper_amazon.py      # Amazon verification scraper
│   │   ├── scraper_factory.py     # Factory pattern implementation
│   │   └── async_queue.py         # Async task queue
│   │
│   ├── ml/                         # Machine Learning & AI modules
│   │   ├── __init__.py
│   │   ├── visual_matcher.py      # Product visual matching
│   │   ├── image_processor.py     # Image processing pipeline
│   │   ├── material_classifier.py # Fabric material classification
│   │   ├── feature_extractor.py   # CNN feature extraction
│   │   └── models/               # Pre-trained model weights
│   │       ├── material_classifier.pkl
│   │       └── feature_weights.pt
│   │
│   ├── analysis/                   # Data analysis & gap detection
│   │   ├── __init__.py
│   │   ├── gap_detector.py        # Gap detection logic
│   │   ├── opportunity_scorer.py  # Opportunity scoring
│   │   ├── price_analyzer.py      # Price analysis
│   │   └── trend_analyzer.py      # Trend analysis
│   │
│   ├── database/                   # Database layer
│   │   ├── __init__.py
│   │   ├── db.py                  # Database connection
│   │   ├── models.py              # SQLAlchemy ORM models
│   │   └── crud.py                # CRUD operations
│   │
│   ├── services/                   # Business logic services
│   │   ├── __init__.py
│   │   ├── search_service.py      # Search orchestration
│   │   ├── scraping_service.py    # Scraper coordination
│   │   ├── analysis_service.py    # Analysis coordination
│   │   ├── approval_service.py    # Approval workflow
│   │   └── export_service.py      # Export functionality
│   │
│   ├── utils/                      # Utility functions
│   │   ├── __init__.py
│   │   ├── logger.py              # Logging configuration
│   │   ├── validators.py          # Data validators
│   │   ├── formatters.py          # Data formatters
│   │   ├── translator.py          # Multi-language support
│   │   └── proxy_manager.py       # Proxy management
│   │
│   ├── migrations/                 # Database migrations (Alembic)
│   │   └── ... (generated by Alembic)
│   │
│   └── tests/                      # Backend tests
│       ├── __init__.py
│       ├── test_scrapers.py
│       ├── test_ml_models.py
│       ├── test_analysis.py
│       └── test_api.py
│
├── frontend/                       # Electron + React Frontend
│   ├── public/
│   │   ├── index.html
│   │   └── logo.png
│   │
│   ├── src/
│   │   ├── index.js               # Entry point
│   │   ├── App.jsx                # Main app component
│   │   │
│   │   ├── components/            # React components
│   │   │   ├── SearchPanel/
│   │   │   │   ├── KeywordSearch.jsx
│   │   │   │   ├── ImageSearch.jsx
│   │   │   │   └── SearchBar.jsx
│   │   │   │
│   │   │   ├── MatrixViewer/
│   │   │   │   ├── GapMatrix.jsx
│   │   │   │   ├── MatrixRow.jsx
│   │   │   │   └── MatrixFilters.jsx
│   │   │   │
│   │   │   ├── ApprovalWorkspace/
│   │   │   │   ├── StagingArea.jsx
│   │   │   │   ├── ProductCard.jsx
│   │   │   │   └── BulkApprovalActions.jsx
│   │   │   │
│   │   │   ├── Dashboard/
│   │   │   │   ├── Analytics.jsx
│   │   │   │   ├── Charts.jsx
│   │   │   │   └── Statistics.jsx
│   │   │   │
│   │   │   ├── Settings/
│   │   │   │   ├── PlatformConfig.jsx
│   │   │   │   ├── ProxySettings.jsx
│   │   │   │   └── UserPreferences.jsx
│   │   │   │
│   │   │   └── Common/
│   │   │       ├── Header.jsx
│   │   │       ├── Sidebar.jsx
│   │   │       ├── LoadingSpinner.jsx
│   │   │       └── ErrorBoundary.jsx
│   │   │
│   │   ├── pages/                 # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── SearchResultsPage.jsx
│   │   │   ├── ApprovalPage.jsx
│   │   │   ├── AnalyticsPage.jsx
│   │   │   └── SettingsPage.jsx
│   │   │
│   │   ├── store/                 # Redux state management
│   │   │   ├── actions/
│   │   │   │   ├── searchActions.js
│   │   │   │   ├── approvalActions.js
│   │   │   │   └── analysisActions.js
│   │   │   ├── reducers/
│   │   │   │   ├── searchReducer.js
│   │   │   │   ├── approvalReducer.js
│   │   │   │   └── uiReducer.js
│   │   │   └── store.js
│   │   │
│   │   ├── services/              # Frontend services
│   │   │   ├── api.js             # API client
│   │   │   ├── ipcService.js      # Electron IPC communication
│   │   │   └── storageService.js  # Local storage
│   │   │
│   │   ├── utils/                 # Utility functions
│   │   │   ├── validators.js
│   │   │   ├── formatters.js
│   │   │   └── helpers.js
│   │   │
│   │   ├── styles/                # CSS styles
│   │   │   ├── globals.css
│   │   │   ├── theme.css
│   │   │   └── components.css
│   │   │
│   │   └── electron/              # Electron main process
│   │       ├── main.js            # Electron app entry
│   │       ├── preload.js         # Context bridge
│   │       └── ipc-handlers.js    # IPC event handlers
│   │
│   ├── package.json
│   ├── webpack.config.js
│   ├── .gitignore
│   └── public/                     # Static assets
│       └── ...
│
├── docs/                           # Documentation
│   ├── API.md                      # API documentation
│   ├── INSTALLATION.md             # Detailed installation guide
│   ├── USER_GUIDE.md              # User manual
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── TROUBLESHOOTING.md         # Troubleshooting guide
│   └── SCREENSHOTS.md             # Screenshots & examples
│
└── .github/
    ├── workflows/                  # GitHub Actions CI/CD
    │   ├── test.yml
    │   ├── build.yml
    │   └── release.yml
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

## 🛠️ Technology Stack

### Frontend
- **Electron** - Cross-platform desktop framework
- **React** 18+ - UI library
- **Redux** - State management
- **Ant Design** - UI component library
- **Axios** - HTTP client
- **Webpack** - Module bundler

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **aiohttp** - Async HTTP client
- **BeautifulSoup4** - HTML parsing
- **Selenium** - Browser automation
- **OpenCV** - Computer vision
- **PyTorch/TensorFlow** - Deep learning (optional)

### Database
- **SQLite** - Local database (default)
- **Redis** - Caching (optional)

## 📖 Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System architecture & design
- **[ROADMAP.md](./ROADMAP.md)** - Development roadmap with phases
- **[docs/API.md](./docs/API.md)** - API endpoint documentation
- **[docs/INSTALLATION.md](./docs/INSTALLATION.md)** - Detailed setup guide
- **[docs/USER_GUIDE.md](./docs/USER_GUIDE.md)** - User manual
- **[docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)** - Contribution guide

## 🔄 Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches

### Commit Convention
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 🚢 Deployment

### Development
```bash
# Terminal 1: Backend
cd backend && python -m uvicorn main:app --reload

# Terminal 2: Frontend (Electron dev)
cd frontend && npm run dev
```

### Production Build
```bash
# Build Electron app
cd frontend
npm run build

# Executables will be in dist/ folder
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](./LICENSE) file for details.

## 🐛 Bug Reports & Features

- **Report Bugs**: [GitHub Issues](https://github.com/Ngocphu-coder/niche-fabric-research-tool/issues)
- **Request Features**: [GitHub Discussions](https://github.com/Ngocphu-coder/niche-fabric-research-tool/discussions)

## 📮 Support & Contact

- **Documentation**: See [docs/](./docs/) directory
- **Issues**: [GitHub Issues](https://github.com/Ngocphu-coder/niche-fabric-research-tool/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Ngocphu-coder/niche-fabric-research-tool/discussions)

## 🙏 Acknowledgments

- Inspired by the need for better multi-platform market research tools
- Built with modern web technologies
- Community contributions welcome

## 📊 Project Status

- **Phase**: 0 - Foundation & Setup
- **Version**: 0.1.0-alpha
- **Last Updated**: 2024
- **Actively Maintained**: ✅ Yes

---

**Made with ❤️ by Ngocphu-coder**

[⬆ Back to top](#multi-platform-niche-fabric-research-tool)
