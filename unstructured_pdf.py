from langchain_unstructured import UnstructuredLoader

file_path = "source_data_dir/subdirectory/marvel.pdf"
#file_path = "source_data_dir/subdirectory/Funzionalità Sito Web.docx"

# 🔍 Disattiva l'uso dell'API Unstructured con `partition_via_api=False`
loader = UnstructuredLoader(
    file_path=file_path,
    strategy="hi_res",  # Usa OCR avanzato
    partition_via_api=False  # ❌ NON usa l'API Unstructured
)

# 📄 Estrazione dei dati
docs = list(loader.lazy_load())

txt_content = ""
# 📌 Stampa il contenuto estratto
for doc in docs:
    print(doc.page_content)
    txt_content += doc.page_content + "\n\n--------------------------------------------------------------\n\n"

with open("output_extracted_text.txt", "w")as f:
    f.write(txt_content)