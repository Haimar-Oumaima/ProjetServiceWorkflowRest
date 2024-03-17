import axios from 'axios';

const httpClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    headers: {
        'Content-Type': 'application/json',
    },
    timeout: 15000,
});

httpClient.interceptors.request.use(
    (config) => {
        const jwtToken = sessionStorage.getItem('token');
        if (jwtToken) {
            config.headers['Authorization'] = `Bearer ${jwtToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    },
);

const handleResponseSuccess = (response) => {
    return response?.data;
};

const handleResponseError = async (error) => {
    return Promise.reject(error);
};

httpClient.interceptors.response.use(
    handleResponseSuccess,
    handleResponseError,
);

const makeRequest = async (method, url, data, config) => {
    try {
        return await httpClient({
            method,
            url,
            data,
            ...config,
        });
    } catch (error) {
        throw error.response?.data;
    }
};

httpClient.get = async function (url, config) {
    return await makeRequest('get', url, null, config);
};

httpClient.post = async function (url, data, config) {
    const headers = { ...config?.headers };
    config = {
        ...config,
        headers,
    };
    return await makeRequest('post', url, data, config);
};

httpClient.put = async function (url, data, config) {
    const headers = { ...config?.headers };
    config = {
        ...config,
        headers,
    };
    return await makeRequest('put', url, data, config);
};

httpClient.patch = async function (url, data, config) {
    const headers = { ...config?.headers };
    config = {
        ...config,
        headers,
    };
    return makeRequest('patch', url, data, config);
};

httpClient.delete = async function (url, config) {
    return makeRequest('delete', url, null, config);
};

export default httpClient;
