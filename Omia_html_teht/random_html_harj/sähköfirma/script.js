document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const header = document.querySelector('header');
    
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('show');
        header.classList.toggle('expanded'); // Add class to expand header
    });
    
    });
