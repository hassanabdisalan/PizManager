import React from 'react';
import SaleForm from '../components/SaleForm';

const Sales = () => {
  return (
    <div className="sales">
      <h1 className="text-3xl font-bold mb-4">Sales</h1>
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-2">Create Sale</h2>
        <SaleForm />
      </div>
    </div>
  );
};

export default Sales;