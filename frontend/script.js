let products = [];
let cart = [];

// Mahsulotlarni backenddan yuklash
async function loadProducts() {
  const res = await fetch('http://localhost:8000/products');
  products = await res.json();
  displayProducts(products);
}

// Mahsulotlarni ekranga chiqarish
function displayProducts(items) {
  const container = document.getElementById('products-list');
  container.innerHTML = '';
  items.forEach(product => {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `
      <img src="${product.images[0]}" alt="${product.name}">
      <h3>${product.name}</h3>
      <p>Narxi: ${product.price} so'm</p>
      <button onclick="addToCart('${product.id}')">Savatchaga qo'shish</button>
    `;
    container.appendChild(card);
  });
}

// Qidiruv funksiyasi
function searchProducts() {
  const query = document.getElementById('search-input').value.toLowerCase();
  const filtered = products.filter(p => p.name.toLowerCase().includes(query));
  displayProducts(filtered);
}

// Savatchaga qo'shish
function addToCart(productId) {
  const product = products.find(p => p.id === productId);
  if (!product) return;
  const cartItem = cart.find(item => item.id === productId);
  if (cartItem) {
    cartItem.quantity += 1;
  } else {
    cart.push({...product, quantity: 1});
  }
  updateCartUI();
}

// Savatchani ekranga chiqarish
function updateCartUI() {
  const cartList = document.getElementById('cart-items');
  cartList.innerHTML = '';
  cart.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.name} x${item.quantity}`;
    cartList.appendChild(li);
  });
  document.getElementById('cart-count').textContent = cart.length;
}

// Buyurtma berish
async function placeOrder() {
  const name = document.getElementById('order-name').value.trim();
  const phone = document.getElementById('order-phone').value.trim();
  const address = document.getElementById('order-address').value.trim();

  if (!name || !phone || !address) {
    alert('Iltimos, barcha ma\'lumotlarni to\'ldiring');
    return;
  }

  if (cart.length === 0) {
    alert('Savatcha bo\'sh');
    return;
  }

  const orderData = {
    name,
    phone,
    address,
    items: cart.map(item => ({
      id: item.id,
      name: item.name,
      quantity: item.quantity
    }))
  };

  const res = await fetch('http://localhost:8000/orders', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(orderData)
  });

  const data = await res.json();

  if (res.ok) {
    alert(`Buyurtma qabul qilindi. ID: ${data.order_id}`);
    cart = [];
    updateCartUI();
    document.getElementById('order-form').reset();
  } else {
    alert('Buyurtma berishda xatolik yuz berdi');
  }
}

// Eventlar qo'shish
document.getElementById('search-input').addEventListener('input', searchProducts);
document.getElementById('checkout-btn').addEventListener('click', placeOrder);

// Sahifa yuklanganda mahsulotlarni yuklash
window.onload = loadProducts;
