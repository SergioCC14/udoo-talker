def read_file(path):
  file = open(path)
  data = file.read()
  file.close()

  return data



def split_data(data, name):
  dr = data.replace("\n", "").split(',')
  
  return data_formatted : {
    (name + '-x'): dr[0]
    (name + '-y'): dr[1]
    (name + '-z'): dr[2]
  }