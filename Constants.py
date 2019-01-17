class Constants:

	def __init__(self):
		self.location = './ProjectCorpus/Corpus/'
		self.solrUrl = 'http://localhost:8983/solr/'
		self.project = 'FinalProjectCorpus'
		#'nlp_project'
		self.solrTimeOut = 60
		self.solrBatchSize = 10
		self.wordWt = 10
		self.posWt = -1
		self.lemmasWt = 4
		self.stemmaWt = 4
		self.hypernymsWt = 8
		self.hyponymsWt = 0
		self.meronymsWt = 1
		self.holonymsWt = 1
		self.headWordWt = 14
