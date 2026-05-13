const fileInput = document.getElementById("fileInput");
const dropZone = document.getElementById("dropZone");
const statusText = document.getElementById("statusText");
const progressBar = document.getElementById("progressBar");
const demoBtn = document.getElementById("demoBtn");
const docPreview = document.getElementById("docPreview");
const results = document.getElementById("results");

const demoData = {
    preview: `
    Invoice No: <span class="highlight">INV-8891</span><br />
    Vendor: <span class="highlight">Azure Solutions</span><br />
    Date: <span class="highlight">13 May 2026</span><br />
    Total Amount: <span class="highlight">₹18,900</span><br />
    Tax: <span class="highlight">₹2,880</span>
  `,
    fields: [
        ["Invoice Number", "INV-8891"],
        ["Vendor Name", "Azure Solutions"],
        ["Invoice Date", "13 May 2026"],
        ["Subtotal", "₹16,020"],
        ["Tax Amount", "₹2,880"],
        ["Total Payable", "₹18,900"]
    ]
};

function updateResults(data) {
    docPreview.innerHTML = data.preview;
    results.innerHTML = data.fields
        .map(
            ([label, value]) => `
        <div class="result-item">
          <label>${label}</label>
          <strong>${value}</strong>
        </div>
      `
        )
        .join("");
}

function simulateUpload(fileName) {
    let progress = 0;
    statusText.textContent = `Processing ${fileName}...`;
    progressBar.style.width = "0%";

    const timer = setInterval(() => {
        progress += 10;
        progressBar.style.width = progress + "%";

        if (progress >= 100) {
            clearInterval(timer);
            statusText.textContent = `Completed: ${fileName}`;
            updateResults(demoData);
        }
    }, 180);
}

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        simulateUpload(fileInput.files[0].name);
    }
});

demoBtn.addEventListener("click", () => {
    simulateUpload("demo-invoice.pdf");
});

dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
});

dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragover");

    if (e.dataTransfer.files.length > 0) {
        const file = e.dataTransfer.files[0];
        simulateUpload(file.name);
    }
});
