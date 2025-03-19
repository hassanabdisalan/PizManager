import React from 'react';

const Customers = () => {
  return (
    <div className="customers">
      <h1 className="text-3xl font-bold mb-4 text-blue-900">Customers</h1>
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-2 text-blue-900">Customer List</h2>
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Name</th>
              <th className="py-2 px-4 border-b">Email</th>
              <th className="py-2 px-4 border-b">Phone</th>
              <th className="py-2 px-4 border-b">Actions</th>
            </tr>
          </thead>
          <tbody>
            {/* Add customer rows here */}
            <tr>
              <td className="py-2 px-4 border-b">John Doe</td>
              <td className="py-2 px-4 border-b">john@example.com</td>
              <td className="py-2 px-4 border-b">123-456-7890</td>
              <td className="py-2 px-4 border-b">
                <button className="bg-green-500 text-white px-2 py-1 rounded mr-2">Edit</button>
                <button className="bg-red-500 text-white px-2 py-1 rounded">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Add Customer</button>
      </div>
    </div>
  );
};

export default Customers;