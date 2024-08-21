API_GATEWAY_HOST = "api.allenneuraldynamics.org"
DATABASE = "metadata_index"
COLLECTION = "data_assets"

docdb_api_client = MetadataDbClient(
   host=API_GATEWAY_HOST,
   database=DATABASE,
   collection=COLLECTION,
)

def one_doc_retrieval(filter_query):
    '''
    Retrieves one document from DocDB. Ideal for queries for a specific document
    
    :param filter_query: MongoDB Query
    :return: JSON File
    '''
    limit = 1000
    paginate_batch_size = 100
    response = docdb_api_client.retrieve_docdb_records(
       filter_query=filter_query,
       limit=limit,
       paginate_batch_size=paginate_batch_size
    )
    return(response[0])

def multi_doc_retrieval(filter_query):
    '''
    Retrieves multiple document from DocDB. Ideal for general queries.
    
    :param filter_query: MongoDB Query
    :return: JSON Files
    '''
    limit = 1000
    paginate_batch_size = 100
    response = docdb_api_client.retrieve_docdb_records(
       filter_query=filter_query,
       limit=limit,
       paginate_batch_size=paginate_batch_size
    )
    return(response)