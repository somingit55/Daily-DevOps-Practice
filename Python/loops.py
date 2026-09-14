# list is data structure which can hold multiple values of multiple type
# array is data structure which can hold same values of multiple type

list_of_cloud = ["aws", "azure", "gcp", "digital ocean", "alibaba"]

print(list_of_cloud)

#add a new cloud 

list_of_cloud.append("Salesforce")  # add to the end

print(list_of_cloud)

# i want to add IBM at second position 

list_of_cloud.insert(2,"IBM")

print(list_of_cloud)

print(len(list_of_cloud))

# insert a Hello Cloud element at 0th index 

list_of_cloud.insert(0,"Hello Cloud")

print(list_of_cloud)

print(len(list_of_cloud))

# Iteration of List

for cloud in list_of_cloud:
    print(cloud)

for i in range(1,11):
    print("Hello Som")