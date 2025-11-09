from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
import diskcache as dc
from functools import lru_cache
from dotenv import load_dotenv

print("Loading package")
# -------------------------------
# 1️⃣ Load environment
# -------------------------------
load_dotenv()

# -------------------------------
# 2️⃣ Set global LLM cache
# -------------------------------
set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))

# -------------------------------
# 3️⃣ Disk-based cache for embeddings & RAG results
# -------------------------------
cache = dc.Cache("rag_cache")

# -------------------------------
# 4️⃣ Initialize once (heavy objects)
# -------------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(
    "faiss_index", embeddings, allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", temperature=0.3, max_output_tokens=1000
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful Tutor and help me understand the topic.
Give complete answer.
Use the context below to answer the question accurately and completely.
Provide sections for Definition, Uses, Types, Pros, and Cons.

<context>
{context}
</context>

Question: {input}
""")

combine_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, combine_chain)
print("Loaded package")


# -------------------------------
# 5️⃣ Add caching to the RAG execution
# -------------------------------
def get_rag_answer(query: str):
    """Cached RAG function"""
    if query in cache:
        print("⚡ Cache Hit!")
        return cache[query]

    print("🧠 Cache Miss — running RAG chain...")
    result = rag_chain.invoke({"input": query})
    answer = result["answer"]
    cache[query] = answer
    return answer


# -------------------------------
# 6️⃣ Optional: LRU cache for in-memory acceleration
# -------------------------------
@lru_cache(maxsize=100)
def get_cached_answer(query: str):
    """In-memory cache on top of disk cache."""
    return get_rag_answer(query)


# -------------------------------
# 7️⃣ Run example queries
# -------------------------------
if __name__ == "__main__":
    print("loading")
    q = "Explain about context-based recommendation system "
    print(get_cached_answer(q))  # First time — RAG pipeline runs
    print(">>")
    print(get_cached_answer(q))  # Second time — Instant (cache)
