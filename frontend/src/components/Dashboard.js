import React from 'react';
import POList from './POList';
import InvoiceList from './InvoiceList';

const Dashboard = () => {
    return (
        <div>
            <header>
                <h1>PO Dashboard</h1>
            </header>
            <main>
                <POList />
                <InvoiceList />
            </main>
        </div>
    );
};

export default Dashboard;