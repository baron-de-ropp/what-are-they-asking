#!/usr/bin/python3
from services.SuggestedQueries import SuggestedQueries
from models.Topics import Topics

class TopicsProvider:
    @staticmethod
    def get_topics(keywords):
        keyword_topics = SuggestedQueries.get_suggested_queries(keywords)[1]
        who_topics = SuggestedQueries.get_suggested_queries("who " + keywords)[1]
        what_topics = SuggestedQueries.get_suggested_queries("what " + keywords)[1]
        where_topics = SuggestedQueries.get_suggested_queries("where " + keywords)[1]
        when_topics = SuggestedQueries.get_suggested_queries("when " + keywords)[1]
        why_topics = SuggestedQueries.get_suggested_queries("why " + keywords)[1]
        how_topics = SuggestedQueries.get_suggested_queries("how " + keywords)[1]
        which_topics = SuggestedQueries.get_suggested_queries("which " + keywords)[1]
        will_topics = SuggestedQueries.get_suggested_queries("will " + keywords)[1]
        are_topics = SuggestedQueries.get_suggested_queries("are " + keywords)[1]
        is_topics = SuggestedQueries.get_suggested_queries("is " + keywords)[1]
        can_topics = SuggestedQueries.get_suggested_queries("can " + keywords)[1]
        or_topics = SuggestedQueries.get_suggested_queries("or " + keywords)[1]
        to_topics = SuggestedQueries.get_suggested_queries("to " + keywords)[1]
        for_topics = SuggestedQueries.get_suggested_queries("for " + keywords)[1]
        with_topics = SuggestedQueries.get_suggested_queries("with " + keywords)[1]
        without_topics = SuggestedQueries.get_suggested_queries("without " + keywords)[1]
        near_topics = SuggestedQueries.get_suggested_queries("near " + keywords)[1]
        like_topics = SuggestedQueries.get_suggested_queries("like " + keywords)[1]
        and_topics = SuggestedQueries.get_suggested_queries("and " + keywords)[1]
        versus_topics = SuggestedQueries.get_suggested_queries("versus " + keywords)[1]
        vs_topics = SuggestedQueries.get_suggested_queries("vs " + keywords)[1]

        model = Topics(keyword_topics, who_topics, what_topics, where_topics, when_topics, why_topics, how_topics, which_topics, will_topics, are_topics, is_topics, can_topics, or_topics, to_topics, for_topics, with_topics, without_topics, near_topics, like_topics, and_topics, versus_topics, vs_topics)

        return model