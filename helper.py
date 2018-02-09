import nltk 
from nltk.stem import PorterStemmer, WordNetLemmatizer

def preprocess(filename):
		with open(filename,"r",encoding="utf8") as f:
		    content = f.readlines()

		finallst=[]
		validLetters = "abcdefghijklmnopqrstuvwxyz "   
		for test in content:
				#print(test)
				k=test.rfind(":") #as per whats app text we are removing the date and user name before ":"
				resp=test[k+1:]   #storing the rmaining text
				#print(resp)
				newString = ''.join([char.lower() for char in resp if char.lower() in validLetters]) #removing non alphabet from text
				#print(newString)
				finallst.append(' '.join(word for word in newString.split() if len(word)>3 and len(word)<20)) #remove word len less then 3 or greater than 20
		#print(len(finallst))

		# tupletoremove=('hmm','hah','okay','mai','han','haa','hai','heh','media',
		# 	'hain','omitted','tum','muj','will','thek','mei','kuch','mere','liye','ohh','kiya'
		# 	,'hoga','okk')

		tupletoremove=('hmm','hah','okay','mai','han','haa','hai','heh','media',
			'hain','omitted','tum','muj','will','thek','mei','kuch','mere','liye','ohh','kiya'
			,'hoga','okk','please','group','thank','facebook','added')

		stringtoken = ' '.join(finallst)
		sentences = nltk.sent_tokenize(stringtoken)
		#print(len(sentences))
		port = PorterStemmer()
		sentencestostring = ' '.join(sentences)
		stringtoken_remove_small=' '.join(word for word in sentencestostring.split() if len(word)>3 and len(word)<20 and not word.startswith(tupletoremove))
		return stringtoken_remove_small

#preprocess()