document.getElementById('download-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form from submitting normally

    // Get the video URL from the input field
    const videoUrl = document.getElementById('video-url').value;

    // Simulating an API call or a download function
    // In a real application, you would send the URL to your backend
    // For now, just show a message
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = `Download initiated for: ${videoUrl}`;

    // Here, you would typically make an API request to your Python server
    // Example: fetch('/download', { method: 'POST', body: JSON.stringify({ url: videoUrl }) });
});
