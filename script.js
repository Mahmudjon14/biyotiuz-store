let cart = [];

async function fetchProducts() {
  const res = await fetch("https://YOUR_BACKEND_URL/api/products/");
  const products = await res.json();
  displayProducts(products);
}

function displayProducts(products) {
  const container = document.getElementById("product-list");
  container.innerHTML = "";

  products.forEach(p => {
    const card = document.createElement("div");
    card.className = "product-card";
    card.innerHTML = `
      <img src="${p.image}" alt="${p.name}" />
      <h3>${p.name}</h3>
      <p>${p.description}</p>
      <strong>${p.price} so'm</strong><br/>
      <button onclick="addToCart('${p.id}', '${p.name}')">Qo‘shish</button>
    `;
    container.appendChild(card);
  });
}

function addToCart(id, name) {
  cart.push(id);
  document.getElementById("cart-count").innerText = cart.length;
  alert(`${name} savatchaga qo‘shildi!`);
}

function openCart() {
  Telegram.WebApp.showAlert(`Savatcha: ${cart.length} ta mahsulot`);
}

document.getElementById("search").addEventListener("input", e => {
  const query = e.target.value.toLowerCase();
  document.querySelectorAll(".product-card").forEach(card => {
    const name = card.querySelector("h3").textContent.toLowerCase();
    card.style.display = name.includes(query) ? "block" : "none";
  });
});

fetchProducts();