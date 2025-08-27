import argparse
from google.cloud import firestore

def update(book_id, chapter_id, url):
    db = firestore.Client()
    # Estrutura: /audio_cache/{bookId}_{chapterId}
    doc_ref = db.collection("audio_cache").document(f"{book_id}_{chapter_id}")
    
    print(f"Atualizando Firestore em: audio_cache/{book_id}_{chapter_id}")
    doc_ref.set({
        "status": "ready",
        "audioUrl": url,
        "createdAt": firestore.SERVER_TIMESTAMP
    })
    
    print("Firestore atualizado com sucesso.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--chapter-id", required=True)
    parser.add_argument("--audio-url", required=True)
    args = parser.parse_args()
    update(args.book_id, args.chapter_id, args.audio_url)
