import React, { useEffect, useState } from 'react';
import axios from '../services/api';

const InvoiceList = () => {
    const [invoices, setInvoices] = useState([]);

    useEffect(() => {
        // Fetch invoices from the backend
        axios.get('/api/invoices/')
            .then(response => {
                setInvoices(response.data);
            })
            .catch(error => {
                console.error('Error fetching invoices:', error);
            });
    }, []);

    return (
        <div>
            <h2>Invoices</h2>
            <ul>
                {invoices.map(invoice => (
                    <li key={invoice.invoice_number}>
                        <strong>Invoice Number:</strong> {invoice.invoice_number} <br />
                        <strong>PO Number:</strong> {invoice.po} <br />
                        <strong>Total Amount:</strong> ${invoice.total_amount} <br />
                        <strong>Due Date:</strong> {invoice.due_date} <br />
                        <strong>Status:</strong> {invoice.payment_status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default InvoiceList;