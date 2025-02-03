from langchain_unstructured import UnstructuredLoader

file_path = "source_data_dir/subdirectory/marvel-1-10.pdf"

loader = UnstructuredLoader(
    file_path=file_path,
    strategy="hi_res",
    partition_via_api=True,
    coordinates=True,
)
docs = []
for doc in loader.lazy_load():
    docs.append(doc)