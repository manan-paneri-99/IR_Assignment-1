from query_processer import search

def test_queries(open_web, use_zones, enable_query_relaxation=1):
    """
    Prints the top 10 doc_ids with their score and titles
    :param open_web: set to True if results are to be opened on browser window
    :param use_zones: set to True to enable Zonal indexing
    :param enable_query_relaxation:
    :return:
    """
    # Taking query input
    query = input("Type the query: ")
    print("Normal:")
    search(query, open_web=False, use_zones=False, enable_query_relaxation=False)
    print("\nWith zone:")
    search(query, open_web=False, use_zones=True, enable_query_relaxation=False)
    print("\nWith Hypernym:")
    search(query, open_web=False, use_zones=False, enable_query_relaxation=1)
    print("\nWith Synonym:")
    search(query, open_web=False, use_zones=False, enable_query_relaxation=2)


test_queries(open_web=False, use_zones=False, enable_query_relaxation=False)
