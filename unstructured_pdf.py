from langchain_community.document_loaders.pdf import UnstructuredPDFLoader

pdf_path = 'source_data_dir/subdirectory/marvel-1-10.pdf'

loader = UnstructuredPDFLoader(
    file_path=pdf_path,
    strategy="hi_res"
)

docs = list(loader.lazy_load())

for doc in docs:
    print(doc.page_content)
