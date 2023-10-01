from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader

loader = RecursiveUrlLoader(
    url=url, max_depth=2, extractor=lambda x: Soup(x, "html.parser").text
)
