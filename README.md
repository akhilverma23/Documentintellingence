# 📄 Azure Document Intelligence Web App

A modern Document Intelligence Web Application built using:

- Python Flask
- Azure AI Document Intelligence
- HTML
- CSS
- JavaScript

This project allows users to:

✅ Upload invoices/documents  
✅ Extract document data using Azure AI  
✅ Display extracted information in a modern UI  
✅ Analyze invoices automatically  
✅ Use drag & drop file upload  

---

# 🚀 Features

- Modern UI/UX Dashboard
- Drag & Drop Upload
- Azure AI Document Intelligence Integration
- Invoice Data Extraction
- Responsive Design
- Flask Backend API
- Real-time Processing Status
- JSON Response Handling

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web Framework |
| Azure AI Document Intelligence | OCR & Data Extraction |
| HTML | Frontend Structure |
| CSS | Styling |
| JavaScript | Frontend Logic |

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── requirements.txt
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/document-intelligence-app.git
cd document-intelligence-app
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Azure Setup

Create an Azure Document Intelligence resource from:

[Azure AI Document Intelligence](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence/?utm_source=chatgpt.com)

Get:

- Endpoint
- API Key

---

# 🌍 Environment Variables

## Windows PowerShell

```powershell
$env:DOCUMENTINTELLIGENCE_ENDPOINT="https://your-resource.cognitiveservices.azure.com/"
$env:DOCUMENTINTELLIGENCE_API_KEY="your-api-key"
```

## Linux / macOS

```bash
export DOCUMENTINTELLIGENCE_ENDPOINT="https://your-resource.cognitiveservices.azure.com/"
export DOCUMENTINTELLIGENCE_API_KEY="your-api-key"
```

---

# ▶️ Run Project

```bash
python app.py
```

Server runs on:

```bash
http://127.0.0.1:5000
```

---

# 📸 Application Workflow

1. Upload Invoice or Document
2. Flask sends file to Azure AI
3. Azure extracts invoice fields
4. Backend processes JSON response
5. UI displays extracted data

---

# 📋 Extracted Fields

The application extracts:

- Invoice Number
- Vendor Name
- Invoice Date
- Subtotal
- Tax Amount
- Total Payable

---

# 🧠 Azure AI Model Used

This project uses:

```python
prebuilt-invoice
```

Model from Azure Document Intelligence API.

---

# 📦 Requirements

```txt
flask
azure-ai-documentintelligence
```

---

# 💻 Example API Response

```json
{
  "invoice_number": "INV-2048",
  "vendor_name": "TechNova Pvt Ltd",
  "invoice_date": "13 May 2026",
  "subtotal": "₹20,990",
  "tax_amount": "₹3,510",
  "total_payable": "₹24,500"
}
```

---

# 🔥 Future Improvements

- PDF Preview
- Authentication System
- Database Integration
- OCR Confidence Score
- Export to Excel/PDF
- Dark Mode
- Multi-language Support

---

# 📚 Azure Documentation

- [Azure AI Document Intelligence Docs](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/?utm_source=chatgpt.com)
- [Azure Python SDK Docs](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-documentintelligence-readme?utm_source=chatgpt.com)

---

# 👨‍💻 Author

Developed by Akhil Verma

---

# ⭐ GitHub

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
🛠 Contribute to the project

---

# 📄 License

This project is licensed under the MIT License.
