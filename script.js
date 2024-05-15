const minimapContent = document.getElementById('minimap-content');
const mainContent = document.getElementById('content');
const minimapOverlay = document.getElementById('minimap-overlay');
const minimapWrapper = document.getElementById('minimap-wrapper');

const setupMinimap = () => {
    // Clone the main content into the minimap content
    const clonedContent = mainContent.cloneNode(true);
    minimapContent.appendChild(clonedContent);

    // Calculate the scale factor
    const scale = minimapWrapper.offsetWidth / mainContent.offsetWidth;

    // Apply the scale to the minimap content
    minimapContent.style.transform = `scale(${scale})`;
    minimapContent.style.height = `${mainContent.offsetHeight * scale}px`;

    // Update the overlay size
    updateOverlay(scale);
};

const updateOverlay = (scale) => {
    // Calculate the dimensions of the overlay
    const visibleHeight = window.innerHeight;
    const contentHeight = mainContent.scrollHeight;
    const overlayHeight = (visibleHeight / contentHeight) * minimapWrapper.offsetHeight;
    const overlayTop = (document.documentElement.scrollTop / contentHeight) * minimapWrapper.offsetHeight;

    // Apply the dimensions and position to the overlay
    minimapOverlay.style.height = `${overlayHeight}px`;
    minimapOverlay.style.top = `${overlayTop}px`;
};

// Setup the minimap when the page loads
window.addEventListener('DOMContentLoaded', setupMinimap);

// Update the overlay on scroll
window.addEventListener('scroll', () => {
    updateOverlay();
});

// Update the minimap on window resize
window.addEventListener('resize', () => {
    setupMinimap();
});
