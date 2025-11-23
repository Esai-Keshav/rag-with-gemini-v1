# RAG with Gemini v1

This project is a Retrieval-Augmented Generation (RAG) prototype that leverages Gemini embeddings, a PostgreSQL vector store (PGVector), and LangChain. It's designed to load PDF documents, embed their content, store these embeddings, and provide a question-answering system by retrieving relevant information and generating responses using a Language Model.

## Features

-   **Document Ingestion:** Loads and chunks PDF documents.
-   **Embedding Generation:** Converts text chunks into vector representations using Gemini embeddings.
-   **Vector Storage:** Stores embeddings and metadata in PostgreSQL with the `pgvector` extension.
-   **Retrieval-Augmented Generation (RAG):** Answers user questions by retrieving relevant document chunks and feeding them to an LLM for generation.

## Installation & Setup

### Prerequisites

-   Python 3.8+
-   PostgreSQL with `pgvector` extension enabled
-   Gemini API Key

### Gemini API Key Setup

Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and add it to a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_key_here
```

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Esai-Keshav/rag-with-gemini-v1.git
    cd rag-with-gemini-v1
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Linux / macOS
    # venv\Scripts\activate # Windows
    ```

3.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install frontend dependencies:**
    ```bash
    cd frontend
    npm install
    cd ..
    ```

## Usage

### Backend

To start the backend API:
```bash
python backend/main.py
```

### Frontend

To start the frontend development server:
```bash
cd frontend
npm run dev
```

## Output Examples

Here are some examples of the system's output:

![Output 1](./output/1.png)
![Output 2](./output/2.png)
![Output 3](./output/3.png)