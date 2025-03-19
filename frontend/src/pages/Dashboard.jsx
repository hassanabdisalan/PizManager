import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChartLine, faUser, faBox, faShoppingCart } from '@fortawesome/free-solid-svg-icons';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1 className="text-3xl font-bold mb-4 text-blue-900">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-bold mb-2 text-blue-900">
            <FontAwesomeIcon icon={faChartLine} className="mr-2" />
            Sales Report
          </h2>
          {/* Add sales report graph here */}
          <button className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">View Details</button>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-bold mb-2 text-blue-900">
            <FontAwesomeIcon icon={faUser} className="mr-2" />
            Customer Report
          </h2>
          {/* Add customer report graph here */}
          <button className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">View Details</button>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-bold mb-2 text-blue-900">
            <FontAwesomeIcon icon={faBox} className="mr-2" />
            Inventory Report
          </h2>
          {/* Add inventory report graph here */}
          <button className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">View Details</button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;