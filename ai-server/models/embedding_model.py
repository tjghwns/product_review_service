try:
    from sentence_transformers import SentenceTransformer
    embedding_model = SentenceTransformer("upskyy/e5-small-korean")
except ImportError:
    embedding_model = None