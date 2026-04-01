from app.rag.llm import get_llm

llm = get_llm()
response = llm.invoke("What is PMAY scheme?")
print(response)