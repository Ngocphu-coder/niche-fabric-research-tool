# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Health Check
```
GET /health
```

## Search Endpoints

### Keyword Search
```
POST /search/keyword
```

Request body:
```json
{
  "query": "goat coat",
  "platforms": ["1688", "taobao", "etsy", "shopee", "amazon"],
  "material_filters": ["fabric"],
  "price_range": [10, 1000]
}
```

### Image Search
```
POST /search/image
```

### Get Search Status
```
GET /search/status/{search_id}
```

## Analysis Endpoints

### Analyze Gaps
```
POST /analyze/gaps
```

Request body:
```json
{
  "search_id": "search_001",
  "reference_platform": "amazon"
}
```

### Get Gap Matrix
```
GET /analyze/matrix/{analysis_id}
```

## Approval Endpoints

### Get Staging Area
```
GET /approval/staging
```

### Approve Product
```
POST /approval/approve
```

Request body:
```json
{
  "product_id": "prod_001",
  "reason": "High volume product",
  "tags": ["priority"]
}
```

### Reject Product
```
POST /approval/reject
```

## Export Endpoints

### Export as CSV
```
GET /export/csv?analysis_id=analysis_001
```

### Export as Excel
```
GET /export/excel?analysis_id=analysis_001
```

### Export as PDF
```
POST /export/pdf
```

Request body:
```json
{
  "analysis_id": "analysis_001",
  "include_images": true
}
```

---

For more details, see the interactive API documentation at `/docs`
