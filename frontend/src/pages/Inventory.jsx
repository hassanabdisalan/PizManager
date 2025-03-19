import React from 'react';

const Inventory = () => {
  return (
    <div className="inventory">
      <h1 className="text-3xl font-bold mb-4 text-blue-900">Inventory</h1>
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-2 text-blue-900">Inventory List</h2>
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Product</th>
              <th className="py-2 px-4 border-b">Quantity</th>
              <th className="py-2 px-4 border-b">Price</th>
              <th className="py-2 px-4 border-b">Actions</th>
            </tr>
          </thead>
          <tbody>
            {/* Add inventory rows here */}
            <tr>
              <td className="py-2 px-4 border-b">Pizza</td>
              <td className="py-2 px-4 border-b">50</td>
              <td className="py-2 px-4 border-b">$10.00</td>
              <td className="py-2 px-4 border-b">
                <button className="bg-green-500 text-white px-2 py-1 rounded mr-2">Edit</button>
                <button className="bg-red-500 text-white px-2 py-1 rounded">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Add Product</button>
      </div>
    </div>
  );
};

export default Inventory;