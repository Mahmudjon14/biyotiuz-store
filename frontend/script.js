let cart = [];

document.addEventListener("DOMContentLoaded", () => {
    fetchProducts();

    document.getElementById("searchInput").addEventListener("input", (e) => {
        fetchProducts(e.target.value);
    });
});

function fetchProducts(query = "") {
    fetch(`/products?q=${query}`)
        .then(res => res.json())
        .then(data => displayProducts(data))
        .catch(err => console.error("Xatolik:", err));
}

function displayProducts(products) {
    const container = document.getElementById("productsContainer");
    container.innerHTML = "";

    products.forEach(product => {
        const card = document.createElement("div");
        card.className = "product-card";

        card.innerHTML = `
            <img src="${product.image_urls[0] || 'https://via.placeholder.com/200'}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.price} so'm</p>
            <button onclick="addToCart('${product.id}')">Savatga qo‘shish</button>
        `;

        container.appendChild(card);
    });
}

function addToCart(productId) {
    cart.push(productId);
    document.getElementById("cartCount").textContent = cart.length;
}
