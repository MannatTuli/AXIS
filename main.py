import csv
import random
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

greet_in = ('hey', 'sup', 'waddup', 'wassup', 'hi', 'hello', 'good day','ola', 'bonjour', 'namastay', 'hola', 'heya', 'hiya', 'howdy',
'greetings', 'yo', 'ahoy')
greet_out = ['hey', 'hello', 'hi there', 'hi', 'heya', 'hiya', 'howdy', 'greetings', '*nods*', 'ola', 'bonjour', 'namastay']
def greeting(sent):
   for word in sent.split():
      if word.lower() in greet_in:
         return random.choice(greet_out)


def naming(name):
   a = name.split()
   if('my name is' in name):
      for j in a:
         if(j!='my' and j!= 'name' and j!='is'):
            return j
   elif('call me' in name):
      for j in a:
         if(j!='call' and j!= 'me'):
            return j
   elif('name is' in name):
      for j in a:
         if(j!= 'name' and j!='is'):
            return j
   elif('change my name to' in name):
      for j in a:
         if(j!= 'change' and j!='my' and j!= 'name' and j!='to'):
            return j
   elif('change name to' in name):
      for j in a:
         if(j!= 'name' and j!= 'name' and j!='to'):
            return j
   else:
      return name

f = open('inc_occ_gender.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
corpus = {}
for row in reader:
   corpus[row[0]] = {row[1]: row[2]}
   
all_text = corpus.values()
all_text = [str (item) for item in all_text]
def stem_tfidf(doc, query):
   query = [query]
   p_stemmer = PorterStemmer()
   tf = TfidfVectorizer(use_idf=True, sublinear_tf=True, stop_words=stopwords.words('english'))
   stemmed_doc = [p_stemmer.stem(w) for w in doc]
   stemmed_query = [p_stemmer.stem(w) for w in query]
   tf_doc = tf.fit_transform(stemmed_doc)
   tf_query = tf.transform(stemmed_query)
   return tf_doc, tf_query
def cos_sim(a, b):
   cosineSimilarities = cosine_similarity(a, b).flatten()
   related_docs_indices = cosineSimilarities.argsort()[:-2:-1]
   if (cosineSimilarities[related_docs_indices] > 0.5):
      ans = [all_text[i] for i in related_docs_indices[:1]]
      for item in ans:
         c, d = item.split(':')
         return d
   else:
      k = 'I am sorry, I cannot help you with this one. Hope to in the future. Cheers :)'
      return k

stop=True
while(stop==True):
   n = input('\nHello, I am a Chatbot! What is your name? : ')
   n = n.lower()
   name = naming(n)
   newname = ''
   stop1=True
   while(stop1==True):
      query = input('\nHi '+(newname if len(newname)!=0 else name)+', Could you reply with your topics of interest from science, arts, and commerce? If you want to exit, type Bye. :')
      query = query.lower()
      query = query.strip("!@#$%^&*()<>,;?")
      if(query=='bye'):
         stop1=False
         print('\nChatbot: This is Chatbot signing off. Bye, take care'+(newname if len(newname)!=0 else name))
      
      elif('my name is' in query or 'call me' in query or 'name is' in query or 'change my name to' in query or 'change name to' in query):
         newname = naming(query)
         print('\nChatbot: Your name is '+newname)

      elif('science' in query):
         print('\nThats great what, could you tell me some interests of yours in science?')

      elif('arts' == query):
         print('\nChatbot: Amazing! I would like to know if you like the justice system or world or want to pursue something else?')   

      elif('justice' == query):
         print('\nChatbot: Thats amazing I would love for you to check out types of judges and lawyers and see if thats where you want to end up!')   
   

      elif('sure' == query):
         print('\nChatbot: Great! I am glad to have helped you out!')   
   

      elif('coding' == query):
         print('\nChatbot: What languages do you code in?')

      elif('biology' == query):
         print('\nChatbot: Thats great! Would you like to become a doctor?')


      elif ('' == query):
         print('\nChatbot: My databse does not contain this, I am still learning :D')


      elif(query=='what is my name?' or query=='what is my name' or query=='whats my name?' or query=='whats my name'):
         if(len(newname)!=0):
            print('\nChatbot: Your name is '+newname)
         else:
            print('\nChatbot: Your name is '+name)
      else:
         if(greeting(query)!=None):
            print('\nChatbot: '+greeting(query)+' '+(newname if len(newname)!=0 else name))
         elif(tfidf_cosim_smalltalk(small_talk_responses, query)!=None):
            x = tfidf_cosim_smalltalk(small_talk_responses, query)
            print('\nChatbot: '+x+(newname if len(newname)!=0 else name))
         else:
            a, b = stem_tfidf(all_text, query)
            g = cos_sim(a, b)
            print('\nChatbot: '+g)
   stop=False