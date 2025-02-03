from unstructured.partition.pdf import partition_pdf

# Percorso al file PDF scansionato
pdf_path = 'source_data_dir/subdirectory/marvel-1-10.pdf'

# Estrazione del testo
elements = partition_pdf(filename=pdf_path, strategy="hi_res")

# Concatenazione del testo estratto
extracted_text = "\n\n".join([str(element) for element in elements])

print(extracted_text)


