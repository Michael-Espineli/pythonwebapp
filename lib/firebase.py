import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase Admin SDK


def my_function()->str:
    cred = credentials.Certificate('key.json')  # Path to your service account key
    firebase_admin.initialize_app(cred)

# Create a Firestore client
    db = firestore.client()
    # Get a document
    #doc_ref = db.collection('users').document('user1')
    #doc = doc_ref.get()

    #if doc.exists:
        #print(f'Document data: {doc.to_dict()}')
    #else:
    #print('No such document!')

# Query data
    users_ref = db.collection('users')
    query = users_ref.stream()

    #for doc in query:
        #print(f'{doc.id} => {doc.to_dict()}')
    val = "Hello from a function" + str(len(query))
    return val
