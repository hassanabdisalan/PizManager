import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTachometerAlt, faUsers, faBox, faShoppingCart, faBars, faTimes } from '@fortawesome/free-solid-svg-icons';

const Sidebar = ({ isOpen, toggleSidebar }) => {
  return (
    <div className={`fixed inset-y-0 left-0 transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} transition-transform duration-300 ease-in-out bg-gradient-to-r from-blue-500 to-blue-700 text-white w-64 h-screen z-50`}>
      <div className="p-4 text-2xl font-bold flex justify-between items-center">
        <span className="text-3xl font-extrabold">PizManager</span>
        <button onClick ={ toggleSidebar} className="text-white focus:outline-none">
          <FontAwesomeIcon icon={faTimes} />
        </button>
      </div>
      <ul className="flex-1">
        <li className="p-4 hover:bg-blue-600">
          <Link to="/" onClick={toggleSidebar}>
            <FontAwesomeIcon icon={faTachometerAlt} className="mr-2" />
            Dashboard
          </Link>
        </li>
        <li className="p-4 hover:bg-blue-600">
          <Link to="/customers" onClick={toggleSidebar}>
            <FontAwesomeIcon icon={faUsers} className="mr-2" />
            Customers
          </Link>
        </li>
        <li className="p-4 hover:bg-blue-600">
          <Link to="/inventory" onClick={toggleSidebar}>
            <FontAwesomeIcon icon={faBox} className="mr-2" />
            Inventory
          </Link>
        </li>
        <li className="p-4 hover:bg-blue-600">
          <Link to="/sales" onClick={toggleSidebar}>
            <FontAwesomeIcon icon={faShoppingCart} className="mr-2" />
            Sales
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;