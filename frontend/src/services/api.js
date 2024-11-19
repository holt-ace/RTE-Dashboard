import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000', // Update with your Django backend URL
    headers: {
        'Content-Type': 'application/json',
    },
});

export default instance;