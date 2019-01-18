#!/usr/bin/python3
from services.SuggestedQueries import SuggestedQueries
from models.Topics import Topics

class TopicsProvider:
    @staticmethod
    def get_topics(keywords):
        keyword_topics = SuggestedQueries.get_suggested_queries(keywords)[1]
        who_topics = SuggestedQueries.get_suggested_queries("who " + keywords)[1]

        model = Topics(keyword_topics, who_topics)

        return model