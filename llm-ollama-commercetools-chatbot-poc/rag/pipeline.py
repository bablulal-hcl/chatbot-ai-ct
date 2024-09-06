from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
import box
import yaml
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


def load_embedding_model(model_name, normalize_embedding=True, device='cpu'):
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs={
            'normalize_embeddings': normalize_embedding
        }
    )


def load_retriever(embeddings, store_path, collection_name, vector_space, num_results=1):
    vector_store = Chroma(collection_name=collection_name,
                          persist_directory=store_path,
                          collection_metadata={"hnsw:space": vector_space},
                          embedding_function=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": num_results})

    return retriever

def load_prompt_template():
    template = """You are a helpful, respectful and honest assistant for \"MyBeautyShop\". Always answer as helpfully as possible, while being safe. 
    Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
    Use the following pieces of information to answer the user's question.

    1. If the user is requesting information on products to buy then Answer with summary product details. Also return the matching skuids. If there are no matching products then suggest matching search term..
    2. If the user is requesting information on his current or past order  then ask the user with the ordernumber and return a summary about the matching order. Also return the matching ordernumber  and orderstatus. 


    Context: {context}
    Question: {question}

    
    If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
    If you don't know the answer to a question, please don't share false information.
    Answer:"""

    prompt = PromptTemplate.from_template(template)

    return prompt


def load_qa_chain(retriever, llm, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False,
        chain_type_kwargs={'prompt': prompt}
    )


def build_rag_pipeline():
    # Import config vars
    with open('config.yml', 'r', encoding='utf8') as ymlfile:
        cfg = box.Box(yaml.safe_load(ymlfile))

    print("Loading embedding model...")
    embeddings = load_embedding_model(model_name=cfg.EMBEDDINGS,
                                      normalize_embedding=cfg.NORMALIZE_EMBEDDINGS,
                                      device=cfg.DEVICE)

    print("Loading vector store and retriever...")
    retriever = load_retriever(embeddings,
                               cfg.VECTOR_DB,
                               cfg.COLLECTION_NAME,
                               cfg.VECTOR_SPACE,
                               cfg.NUM_RESULTS)

    print("Loading prompt template...")
    prompt = load_prompt_template()

    print("Loading Ollama...")
    llm = Ollama(model=cfg.LLM, verbose=False, temperature=0)

    print("Loading QA chain...")
    qa_chain = load_qa_chain(retriever, llm, prompt)

    return qa_chain


