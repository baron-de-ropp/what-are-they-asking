
import requests


def get_suggested_queries(query):
	suggestions = []
	
	# Google
	url = "http://suggestqueries.google.com/complete/search"
	parameters = {
		"client": "firefox",
		"q": "\"" + query + "\"",
		"hl": "en"
	}
	google_request = requests.get(url, params = parameters)
	for item in google_request.json()[1]:
		suggestions.append(item)

	# duckduckgo
	url = "https://ac.duckduckgo.com/ac/"
	params = {"q": query}
	duckduckgo_response = requests.get(url, params=params)
	for item in duckduckgo_response.json():
		suggestions.append(item['phrase'])


	return list(set(suggestions))




if __name__ == '__main__':
	print(get_suggested_queries('dungeons and'))

		




