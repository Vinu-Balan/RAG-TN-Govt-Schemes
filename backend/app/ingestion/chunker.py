from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_sections(sections):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    all_chunks = []

    for section in sections:
        chunks = splitter.split_text(section["content"])

        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "section": section["title"]
            })

    return all_chunks