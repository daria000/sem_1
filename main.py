#exersize:indexing and slicing

url = https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv

#use indexing slicing to fill in the following output
#copy / paste is not allowed

file_name = url[start_index:end_index]
print(file_name) #ted-sample.csv

url[0:5]
protocol= 
print(protocol) #https

host_name= 
print(host_name) #github.com

#use string composition to construct https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv
output = protocol + ':///' + host_name + '/' + file_name
print(output) #https://github.com/codedthinking/tender-home-bias/releases/