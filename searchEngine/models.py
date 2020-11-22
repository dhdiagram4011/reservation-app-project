from django.db import models

## elasticSearch search-engine page


class SearchEngine(models.Model):
    searchKeyword = models.CharField(max_length=100)






