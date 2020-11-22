from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from elasticsearch import Elasticsearch

class SearchView(APIView):
    def get(self, request):
        es = Elasticsearch()

        search_word = request.query_params.get('search=')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'search word missing'})
        else:
            docs = es.search(index='dictionary',
                            doc_type = 'dictionary_datas',
                            body = {
                                "query": {
                                    "multi_match": {
                                        "query": search_word,
                                        "fields" : ["title","content"]
                                 }
                             }
                         })
            data_list = docs['hits']
        
            return Response(data_list)

