import copy

def create_movie(movie_doc, **kwargs):
  temp_dict = copy.deepcopy(movie_doc)
  for item in kwargs:
    if temp_dict.has_key(item):
      temp_dict[item] = kwargs[item]
  print temp_dict

if __name__ == "__main__":
  a = {"a":12, "b":"fdas", "c":"c is this"}
  #create_movie(a, b=312)
  #create_movie(a, b="i do it")
  create_movie(a, c=31)
  print a

