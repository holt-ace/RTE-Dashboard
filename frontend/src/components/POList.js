import React, { useEffect, useState } from 'react';
import axios from '../services/api';

const POList = () => {
    const [pos, setPOs] = useState([]);

    useEffect(() => {
        // Fetch POs from the backend
        axios.get('/api/pos/')
            .then(response => {
                setPOs(response.data);
            })
            .catch(error => {
                console.error('Error fetching POs:', error);
            });
    }, []);

    return (
        <div>
            <h2>Purchase Orders</h2>
            <ul>
                {pos.map(po => (
                    <li key={po.po_number}>
                        <strong>PO Number:</strong> {po.po_number} <br />
                        <strong>Customer:</strong> {po.customer} <br />
                        <strong>Buyer:</strong> {po.buyer} <br />
                        <strong>Order Date:</strong> {po.order_date} <br />
                        <strong>Delivery Date:</strong> {po.delivery_date} <br />
                        <strong>Status:</strong> {po.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default POList;