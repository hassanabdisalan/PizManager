import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SaleForm = () => {
  const [customer, setCustomer] = useState('');
  const [products, setProducts] = useState([{ product: '', quantity: 1, selling_price: '' }]);
  const [grandTotalPrice, setGrandTotalPrice] = useState(0);
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    const getCsrfToken = async () => {
      try {
        const response = await axios.get('/api/csrf_token/');
        setCsrfToken(response.data.csrfToken);
      } catch (error) {
        console.error('Error fetching CSRF token:', error);
      }
    };

    getCsrfToken();
  }, []);

  const handleProductChange = (index, event) => {
    const newProducts = [...products];
    newProducts[index][event.target.name] = event.target.value;
    setProducts(newProducts);
  };

  const handleAddProduct = () => {
    setProducts([...products, { product: '', quantity: 1, selling_price: '' }]);
  };

  const handleRemoveProduct = (index) => {
    const newProducts = products.filter((_, i) => i !== index);
    setProducts(newProducts);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const saleData = {
      customer,
      products,
    };
    try {
      const response = await axios.post('/api/create_sale/', saleData, {
        headers: {
          'X-CSRFToken': csrfToken,
        },
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Customer:</label>
        <input type="text" value={customer} onChange={(e) => setCustomer(e.target.value)} required />
      </div>
      {products.map((product, index) => (
        <div key={index}>
          <label>Product:</label>
          <input type="text" name="product" value={product.product} onChange={(e) => handleProductChange(index, e)} required />
          <label>Quantity:</label>
          <input type="number" name="quantity" value={product.quantity} onChange={(e) => handleProductChange(index, e)} min="1" required />
          <label>Selling Price:</label>
          <input type="number" name="selling_price" value={product.selling_price} onChange={(e) => handleProductChange(index, e)} required />
          <button type="button" onClick={() => handleRemoveProduct(index)}>Remove</button>
        </div>
      ))}
      <button type="button" onClick={handleAddProduct}>Add Product</button>
      <button type="submit">Submit</button>
    </form>
  );
};

export default SaleForm;