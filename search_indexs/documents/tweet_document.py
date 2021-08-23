from twitter.models.tweet_model import TweetModel
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields


@registry.register_document
class TweetDocument(Document):
    class Index:
        name = 'tweet_index'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    author = fields.ObjectField(properties={
        'name': fields.TextField(),
        'username': fields.TextField(),
        'email': fields.TextField()
    })

    class Django:
        model = TweetModel
        fields = (
            'text',
        )
