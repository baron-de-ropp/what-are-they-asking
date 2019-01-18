#!/usr/bin/python3
import requests

class SuggestedQueries:
	@staticmethod
	def get_suggested_queries(keywords):
		url = "http://suggestqueries.google.com/complete/search" ##?client=firefox&q=who%20dungeons%20and%20dragons&hl=en
		parameters = {
			"client": "firefox",
			"q": "\"" + keywords + "\"",
			"hl": "en"
		}
		# return "i made it!"
		request = requests.get(url, params = parameters)
		return request.json()



