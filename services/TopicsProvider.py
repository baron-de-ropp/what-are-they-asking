#!/usr/bin/python3
import services.SuggestedQueries as sq
from models.Topics import Topics

def get_topics(keywords):
    keyword_topics = sq.get_suggested_queries(keywords)
    who_topics = sq.get_suggested_queries("who " + keywords)
    what_topics = sq.get_suggested_queries("what " + keywords)
    where_topics = sq.get_suggested_queries("where " + keywords)
    when_topics = sq.get_suggested_queries("when " + keywords)
    why_topics = sq.get_suggested_queries("why " + keywords)
    how_topics = sq.get_suggested_queries("how " + keywords)
    which_topics = sq.get_suggested_queries("which " + keywords)
    will_topics = sq.get_suggested_queries("will " + keywords)
    are_topics = sq.get_suggested_queries("are " + keywords)
    is_topics = sq.get_suggested_queries("is " + keywords)
    can_topics = sq.get_suggested_queries("can " + keywords)
    or_topics = sq.get_suggested_queries("or " + keywords)
    to_topics = sq.get_suggested_queries("to " + keywords)
    for_topics = sq.get_suggested_queries("for " + keywords)
    with_topics = sq.get_suggested_queries("with " + keywords)
    without_topics = sq.get_suggested_queries("without " + keywords)
    near_topics = sq.get_suggested_queries("near " + keywords)
    like_topics = sq.get_suggested_queries("like " + keywords)
    and_topics = sq.get_suggested_queries("and " + keywords)
    versus_topics = sq.get_suggested_queries("versus " + keywords)
    vs_topics = sq.get_suggested_queries("vs " + keywords)

    model = Topics(keyword_topics, who_topics, what_topics, where_topics, when_topics, why_topics, how_topics, which_topics, will_topics, are_topics, is_topics, can_topics, or_topics, to_topics, for_topics, with_topics, without_topics, near_topics, like_topics, and_topics, versus_topics, vs_topics)

    return model