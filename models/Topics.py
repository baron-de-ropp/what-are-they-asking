#!/usr/bin/python3

class Topics:
    #interogatives
    keyword_topics = []
    who_topics = []
    what_topics = []
    where_topics = []
    when_topics = []
    why_topics = []
    how_topics = []
    which_topics = []

    #verbs
    will_topics = []
    are_topics = []
    is_topics = []
    can_topics = []

    #prepositions
    or_topics = []
    to_topics = []
    for_topics = []
    with_topics = []
    near_topics = []
    without_topics = []

    #comparisons
    like_topics = []
    and_topics = []
    versus_topics = []
    vs_topics = []

    def __init__(self, keyword_topics, who_topics, what_topics, where_topics, when_topics, why_topics, how_topics, which_topics, will_topics, are_topics, is_topics, can_topics, or_topics, to_topics, for_topics, with_topics, without_topics, near_topics, like_topics, and_topics, versus_topics, vs_topics):
        #interogatives
        self.keyword_topics = keyword_topics
        self.who_topics = who_topics
        self.what_topics = what_topics
        self.where_topics = where_topics
        self.when_topics = when_topics
        self.why_topics = why_topics
        self.how_topics = how_topics
        self.which_topics = which_topics
        
        #verbs
        self.will_topics = will_topics
        self.are_topics = are_topics
        self.is_topics = is_topics
        self.can_topics = can_topics

        #prepositions
        self.or_topics = or_topics
        self.to_topics = to_topics
        self.for_topics = for_topics
        self.with_topics = with_topics
        self.without_topics = without_topics
        self.near_topics = near_topics


        #comparisons
        self.like_topics = like_topics
        self.and_topics = and_topics
        self.versus_topics = versus_topics
        self.vs_topics = vs_topics