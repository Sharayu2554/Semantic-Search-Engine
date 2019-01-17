#Semantic Search Engine

PreRequiste :

  Python, 
   [Solr](https://lucene.apache.org/solr/guide/6_6/installing-solr.html), 
    [stanford-corenlp-full-2017-06-09](https://stanfordnlp.github.io/CoreNLP/download.html)
  
  
  

Add your Corpus location in Constants.py (self.location = './ProjectCorpus/Corpus/' ) If you are running solr on different port(other than 8983), update that port in Constants.py (self.solrUrl = 'http://localhost:8983/solr/') If you project name is different that "gettingstarted", update project in Constants.py (self.project = 'gettingstarted')

To create project in sorl : sudo su solr /opt/solr/bin/solr create -c FinalProjectCorpus -n data_driven_schema_configs

To delete existing data from solr execute followinf curl commands : curl http://localhost:8983/solr/gettingstarted/update -H "Content-Type: text/xml" --data-binary ':' curl http://localhost:8983/solr/gettingstarted/update --data '' -H 'Content-type:text/xml; charset=utf-8'

####To Run Project Prerequiste: need to install pysolr and nltk #nltk.download('stopwords') Unzip "stanford-corenlp-full-2017-06-09" folder, and add its path in Task3.py at "path_to_models_jar" and "path_to_jar"

####Run Command : Following Command will Read corpus, tokenize it , get lemmas, stemma, hypernyms , etc and store it in solr. This is done by Task3.ReadCorpus() Task3.searchSolr() , is function that will search for hardcoded values Task3.analyzeSingleSentence("Australia accused the U.S. of increasing") will perform Task3 only for one sentence sent as an argument.

####TO Execute Search Engine :

    python test.py Read_Corpus
    python test.py Task2 "Company suffering from losses"
    python test.py Task3 "Company suffering from losses"  
    python test.py Task4 "Company suffering from losses"
	
	Where "Company suffering from losses" is the query we need to search for.
