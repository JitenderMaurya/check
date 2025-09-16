import argparse
from pymongo import MongoClient
from bson.objectid import ObjectId


def filter_data(user_id, session_id, doc_type=None, limit=None):
    """
    Connects to a MongoDB database and filters data from a collection
    based on user_id, session_id, and other optional criteria.
    """
    client = MongoClient(
        'mongodb+srv://PitchFit:O53VQznVSANqhdqh@cluster1.jvfxwrw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1')
    db = client['test']
    collection = db['financialmodelchatmessages']
    try:
        # Build the base query
        query = {
            'user': ObjectId(user_id),
            'session': ObjectId(session_id)
        }

        # Add the document type to the query if provided
        if doc_type:
            query['type'] = doc_type

    except Exception as e:
        print(e)
        client.close()
        return

    try:
        # Execute the query, applying a limit if provided
        cursor = collection.find(query)
        if limit is not None:
            cursor = cursor.limit(limit)

        results = list(cursor)

        if results:
            print(f"Found {len(results)} matching document(s):")
            for doc in results:
                print(doc)
        else:
            print("No matching documents found.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
        print("Connection to MongoDB closed.")


if __name__ == '__main__':
    # --- Command-line Argument Parsing ---
    parser = argparse.ArgumentParser(description='Filter data from MongoDB.')
    parser.add_argument('--user-id', required=True, help='The user ID to filter by.')
    parser.add_argument('--session-id', required=True, help='The session ID to filter by.')
    parser.add_argument('--type', help='The type of document to filter by.')
    parser.add_argument('--limit', type=int, help='The maximum number of documents to return.')

    args = parser.parse_args()

    filter_data(args.user_id, args.session_id, args.type, args.limit)
