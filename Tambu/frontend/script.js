function search() {
    const searchInput = document.getElementById('search-input').value;
    const locationInput = document.getElementById('location-input').value;
    alert(`Searching for ${searchInput} in ${locationInput}`);
}

// Function to open a modal
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    }
}

// Function to close a modal
function closeModal() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.style.display = 'none';
    });
}

// Event listener for the close buttons
document.querySelectorAll('.close-button').forEach(button => {
    button.addEventListener('click', closeModal);
});

// Event listener for clicking outside the modal to close it
window.addEventListener('click', event => {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            closeModal();
        }
    });
});

// Open the sign-up modal
document.getElementById('signup-btn').addEventListener('click', () => {
    openModal('signup-modal');
});

// Open the sign-in modal
document.getElementById('signin-btn').addEventListener('click', () => {
    openModal('signin-modal');
});



// Function to fetch categories from the API and display them
function getCategories() {
    fetch('/api/categories/')
        .then(response => response.json())
        .then(data => {
            displayCategories(data);
        })
        .catch(error => console.error('Error fetching categories:', error));
}

// Function to display categories on the webpage
function displayCategories(categories) {
    const categoryContainer = document.querySelector('.categories-container');
    categoryContainer.innerHTML = ''; // Clear existing content

    categories.forEach(category => {
        const categoryCard = document.createElement('div');
        categoryCard.classList.add('category-card');

        // Add category image
        const categoryImage = document.createElement('img');
        categoryImage.src = category.image; // Replace with your property name
        categoryImage.alt = category.name; // Replace with your property name
        categoryCard.appendChild(categoryImage);

        // Add category name
        const categoryName = document.createElement('p');
        categoryName.textContent = category.name; // Replace with your property name
        categoryCard.appendChild(categoryName);

        categoryContainer.appendChild(categoryCard);
    });
}

// Call getCategories when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', getCategories);
