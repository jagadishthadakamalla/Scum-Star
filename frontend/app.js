function generateReport() {
 fetch("http://127.0.0.1:5000/generate-report")
 .then(response => {
 if (!response.ok) {
 throw new Error("Failed to generate report");
 }
 return response.blob();
 })
 .then(blob => {
 const url = window.URL.createObjectURL(blob);
 const a = document.createElement("a");
 a.href = url;
 a.download = "sprint_report.xlsx";
 document.body.appendChild(a);
 a.click();
 a.remove();
 })
 .catch(error => {
 alert("Error: " + error.message);
 });
}
