import pickle
def load_tfidf():
    file_name=open(r"C:\Users\Ac37652\Desktop\server\tf_transformer.pkl","rb")
    tf_transformer1=pickle.load(file_name)
    file_name.close()
    return tf_transformer1