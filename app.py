import os
import json
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DOCUMENTINTELLIGENCE_ENDPOINT = os.getenv("https://akhilverma.cognitiveservices.azure.com/")
DOCUMENTINTELLIGENCE_API_KEY = os.getenv("DjXD1EuNccXQXf0VpY9BTruACp457AcIdkJTnyv0NYdluLmhvrOCJQQJ99CEAC3pKaRXJ3w3AAALACOGuhYi")

if not DOCUMENTINTELLIGENCE_ENDPOINT or not DOCUMENTINTELLIGENCE_API_KEY:
    raise ValueError("Set DOCUMENTINTELLIGENCE_ENDPOINT and DOCUMENTINTELLIGENCE_API_KEY environment variables.")

client = DocumentIntelligenceClient(
    endpoint=DOCUMENTINTELLIGENCE_ENDPOINT,
    credential=AzureKeyCredential(DOCUMENTINTELLIGENCE_API_KEY)
)

def get_field_value(field):
    if field is None:
        return None

    if isinstance(field, dict):
        for key in [
            "valueString",
            "valueDate",
            "valueNumber",
            "valueInteger",
            "valueBoolean",
            "valueCurrency",
            "content"
        ]:
            if key in field and field[key] is not None:
                if key == "valueCurrency" and isinstance(field[key], dict):
                    return field[key].get("amount") or field[key].get("value")
                return field[key]

    return field

def extract_invoice_data(file_path):
    with open(file_path, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-invoice", body=f)
    result = poller.result()

    result_dict = result.as_dict()

    documents = result_dict.get("documents") or result_dict.get("documentResults") or []
    first_doc = documents[0] if documents else {}
    fields = first_doc.get("fields", {})

    extracted = {
        "file_name": os.path.basename(file_path),
        "invoice_number": get_field_value(fields.get("InvoiceId") or fields.get("InvoiceNumber")),
        "vendor_name": get_field_value(fields.get("VendorName")),
        "invoice_date": get_field_value(fields.get("InvoiceDate")),
        "subtotal": get_field_value(fields.get("SubTotal") or fields.get("Subtotal")),
        "tax_amount": get_field_value(fields.get("TotalTax") or fields.get("TaxAmount")),
        "total_payable": get_field_value(fields.get("InvoiceTotal") or fields.get("Total"))
    }

    return extracted, result_dict

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        extracted, raw_result = extract_invoice_data(filepath)
        return jsonify({
            "success": True,
            "extracted": extracted,
            "raw_result": raw_result
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
