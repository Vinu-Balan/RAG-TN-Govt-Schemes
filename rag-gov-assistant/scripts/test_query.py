from app.rag.pipeline import query_rag

result = query_rag("What are the schemes favourable to unmarried individuals?")

print("\nAnswer:\n", result["answer"])
print("\nSources:\n", result["sources"])