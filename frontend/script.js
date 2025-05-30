const productsSection = document.getElementById("products-section");
const searchInput = document.getElementById("search-input");
const cartItems = document.getElementById("cart-items");
const checkoutBtn = document.getElementById("checkout-btn");
const orderSection = document.getElementById("order-section");
const orderForm = document.getElementById("order-form");

let products = [];
let cart = [];

// Backend URL manzilingizni shu yerga yozing
const backendUrl = "http://localhost:8000";  // Render.com’da joylashgan backend manzilini yozasiz

// Mahsulotlarni backenddan olish
async function fetchProducts() {
    try {
        const res = await fetch(`${backendUrl}/products`);
        products = await res.json();
        displayProducts(products);
    } catch (error) {
        productsSection.innerHTML = "<p>Mahsulotlarni yuklashda xatolik yuz berdi.</p>";
        console.error(error);
    }
}

// Mahsulotlarni sahifaga chiqarish
function displayProducts(items) {
    productsSection.innerHTML = "";
    if (items.length === 0) {
        productsSection.innerHTML = "<p>Mahsulot topilmadi.</p>";
        return;
    }
    items.forEach(product => {
        const div = document.createElement("div");
        div.className = "product-card";
        div.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Narxi: ${product.price} so'm</p>
            <button onclick="addToCart(${product.id})">Savatchaga qo'shish</button>
        `;
        productsSection.appendChild(div);
    });
}

// Qidiruv
searchInput.addEventListener("input", () => {
    const filtered = products.filter(p =>
        p.name.toLowerCase().includes(searchInput.value.toLowerCase())
    );
    displayProducts(filtered);
});

// Savatchaga mahsulot qo‘shish
function addToCart(id) {
    const product = products.find(p => p.id === id);
    if (!product) return;
    const existing = cart.find(item => item.id === id);
    if (existing) {
        existing.quantity++;
    } else {
        cart.push({...product, quantity: 1});
    }
    renderCart();
}

// Savatchani yangilash va ko‘rsatish
function renderCart() {
    cartItems.innerHTML = "";
    cart.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - ${item.quantity} dona`;
        const removeBtn = document.createElement("button");
        removeBtn.textContent = "O‘chirish";
        removeBtn.onclick = () => removeFromCart(item.id);
        li.appendChild(removeBtn);
        cartItems.appendChild(li);
    });
    checkoutBtn
