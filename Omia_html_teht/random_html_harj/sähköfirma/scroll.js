document.addEventListener("DOMContentLoaded", () => {
    const scrollImage = document.querySelector(".scroll-image");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add class to slide in the image
                scrollImage.classList.add("visible");
            } else {
                // Remove class to slide out the image
                scrollImage.classList.remove("visible");
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the image is visible
    });

    observer.observe(scrollImage);
});
