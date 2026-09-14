import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

// Search endpoints
export const searchByKeyword = (query, platforms) => {
  return api.post('/search/keyword', { query, platforms });
};

export const searchByImage = (file) => {
  const formData = new FormData();
  formData.append('file', file);
  return api.post('/search/image', formData);
};

export const getSearchStatus = (searchId) => {
  return api.get(`/search/status/${searchId}`);
};

// Analysis endpoints
export const analyzeGaps = (searchId, referencePlatform) => {
  return api.post('/analyze/gaps', { search_id: searchId, reference_platform: referencePlatform });
};

export const getGapMatrix = (analysisId) => {
  return api.get(`/analyze/matrix/${analysisId}`);
};

// Approval endpoints
export const getStagingArea = () => {
  return api.get('/approval/staging');
};

export const approveProduct = (productId, reason) => {
  return api.post(`/approval/approve`, { product_id: productId, reason });
};

export const rejectProduct = (productId, reason) => {
  return api.post(`/approval/reject`, { product_id: productId, reason });
};

export default api;
