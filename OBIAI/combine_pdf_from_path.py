import os
from PyPDF2 import PdfMerger

# Replace this with the actual path to your OBIAI folder
folder_path = r"C:\Path\To\Your\OBIAI"
output_file = os.path.join(folder_path, "Combined_OBIAI_Proofs.pdf")

# Grab all PDF files in the folder, sorted by name
pdf_files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith(".pdf"))

# Combine using PdfMerger
merger = PdfMerger()
for pdf in pdf_files:
    full_path = os.path.join(folder_path, pdf)
    merger.append(full_path)

merger.write(output_file)
merger.close()

print(f"Combined PDF created: {output_file}")
