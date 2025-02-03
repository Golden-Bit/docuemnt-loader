from langchain_unstructured import UnstructuredLoader

file_path = "source_data_dir/subdirectory/marvel-1-10.pdf"


# 🔍 Disattiva l'uso dell'API Unstructured con `partition_via_api=False`
loader = UnstructuredLoader(
    file_path=file_path,
    strategy="hi_res",  # Usa OCR avanzato
    partition_via_api=False  # ❌ NON usa l'API Unstructured
)

# 📄 Estrazione dei dati
docs = list(loader.lazy_load())

# 📌 Stampa il contenuto estratto
for doc in docs:
    print(doc.page_content)