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
    fetch('http://127.0.0.1:8000/api/categories/')
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

/* document.addEventListener('DOMContentLoaded', function() {
    const recentActivityElement = document.getElementById('recent-activity');
    if (recentActivityElement) {
        fetch('http://127.0.0.1:8000/api/recent-reviews/')
            .then(response => response.json())
            .then(recentReviews => {
                recentReviews.forEach(review => {
                    const activityCard = document.createElement('div');
                    activityCard.className = 'activity-card';

                    const userInfo = document.createElement('div');
                    userInfo.className = 'user-info';
                    userInfo.innerHTML = `
                        <img src="${review.user.profile_image}" alt="User Profile">
                        <p>${review.user.username} added a review</p>
                        <span>${getTimeAgo(review.created_at)}</span>
                    `;

                    const activityContent = document.createElement('div');
                    activityContent.className = 'activity-content';
                    activityContent.innerHTML = `
                        <h3>${review.business.name}</h3>
                        <div class="rating">${getStarRating(review.rating)} ${review.rating}</div>
                        <p>${review.business.category}</p>
                        <img src="${review.business.image}" alt="${review.business.name}">
                    `;

                    activityCard.appendChild(userInfo);
                    activityCard.appendChild(activityContent);
                    recentActivityElement.appendChild(activityCard);
                });
            })
            .catch(error => console.error('Error fetching recent reviews:', error));
    } else {
        console.error('Element with ID "recent-activity" not found');
    }

    function getTimeAgo(dateString) {
        // Calculate time difference between now and the provided date string
        // and return a human-readable string like "X minutes ago", "X hours ago", etc.
    }

    function getStarRating(rating) {
        // Convert numeric rating to star emojis or any other representation you prefer
        // For example, if rating is 4, return '⭐⭐⭐⭐'
    }
}); */

document.addEventListener('DOMContentLoaded', function() {
    const recentActivityElements = document.getElementsByClassName('recent-activity');
    if (recentActivityElements.length > 0) {
        const recentActivityElement = recentActivityElements[0]; // Assuming you only have one element with the class "recent-activity"
        fetch('http://127.0.0.1:8000/api/recent-reviews/')
            .then(response => response.json())
            .then(recentReviews => {
                recentReviews.forEach(reviews => {
                    const activityCard = document.createElement('div');
                    activityCard.className = 'activity-card';

                    const userInfo = document.createElement('div');
                    userInfo.className = 'user-info';
                    userInfo.innerHTML = `
                        <img src="${reviews.user.profile_image}" alt="User Profile">
                        <p>${reviews.user.username} added a review</p>
                        <span>${getTimeAgo(reviews.created_at)}</span>
                    `;

                    const activityContent = document.createElement('div');
                    activityContent.className = 'activity-content';
                    activityContent.innerHTML = `
                        <h3>${reviews.business.name}</h3>
                        <h3>${reviews.body}</h3>
                        <div class="rating">${getStarRating(reviews.rating)} ${reviews.rating}</div>
                        <p>${reviews.business.category}</p>
                        <img src="${reviews.business.image}" alt="${reviews.business.name}">
                    `;

                    activityCard.appendChild(userInfo);
                    activityCard.appendChild(activityContent);
                    recentActivityElement.appendChild(activityCard);
                });
            })
            .catch(error => console.error('Error fetching recent reviews:', error));
    } else {
        console.error('Element with class "recent-activity" not found');
    }

    function getTimeAgo(dateString) {
        // Calculate time difference between now and the provided date string
        // and return a human-readable string like "X minutes ago", "X hours ago", etc.
    }

    function getStarRating(rating) {
        // Convert numeric rating to star emojis or any other representation you prefer
        // For example, if rating is 4, return '⭐⭐⭐⭐'
    }
});


document.getElementById('add-business-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);

    fetch('http://127.0.0.1:8000/api/businesses/create/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('Business added successfully!');
        this.reset(); // Reset the form after successful submission
    })
    .catch(error => {
        console.error('Error adding business:', error);
        alert('There was an error adding the business. Please try again.');
    });
});


