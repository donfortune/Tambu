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
