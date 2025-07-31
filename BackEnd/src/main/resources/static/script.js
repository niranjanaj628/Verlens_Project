document.addEventListener("DOMContentLoaded", function () {
    const file = sessionStorage.getItem('imageFile');

    if (!file) {
        document.getElementById("verdict").textContent = "⚠️ No image found.";
        return;
    }

    // ⬇️ Preview the image directly
    const imgElement = document.getElementById("inputImagePreview");
    if (imgElement) {
        imgElement.src = file;  // file is already a base64 data URL
    }

    // Reconstruct and send to backend
    const blob = new Blob([Uint8Array.from(atob(file.split(',')[1]), c => c.charCodeAt(0))], { type: 'image/jpeg' });
    const formData = new FormData();
    formData.append('file', blob, 'image.jpg');

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(res => res.json())
        .then(data => {
            const result = data.result;
            const confidence = data.confidence;

            document.getElementById("verdict").textContent =
                result === 'real' ? '✅ This media is REAL' : '⚠️ This media is FAKE';

            document.getElementById("confidence").textContent = `${confidence}%`;
        })
        .catch(err => {
            console.error(err);
            document.getElementById("verdict").textContent = "❌ Error analyzing image.";
        });
});


document.getElementById('analyseBtn').addEventListener('click', () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    const reader = new FileReader();
    reader.onloadend = function () {
        sessionStorage.setItem('imageFile', reader.result);
        window.location.href = 'analyze.html';
    };
    if (file) {
        reader.readAsDataURL(file);
    }
});