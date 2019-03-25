import pickle
def load_countvect():
    file_name=open(r"C:\Users\Ac37652\Desktop\server\count_vect.pkl","rb")
    count_vect=pickle.load(file_name)
    return count_vect