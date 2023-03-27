#tuples  
#very same with string 
#non-immutable ==no changing  
#methods== concat + === slice[3:5] === len()
#nesting is possible

tuple1=("hi",2,4,9,(5,6))
tuple1[1] #2
print(tuple1[-1][0]) #5
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings) #no change to the orginal
#Ratings.sort()   #sort the orginal 
print(tuple1.index(4)) #2
print(sum(Ratings)) #55

##list 
#mutable =changable
#nesting possible 
#concat + is possible
list1=[1,3,5,[1,2]]
list1[1]=5

l=[1,2,3]+[1,1,1] #concatination

list1.extend([5,6])# 2 element added ==concatination
list1.append([5,6]) #1 element added
print(list1)
del(list1[0])
print(list1)

list2=list1 #not new list #both refrence same 1 list ==aliasing
list3=list1[:]#a new list #both refrence d/f lists ==.cloning
#help(list1)



####dictionaries
dict1={"one":1,"two":2,"laptops":['hp','dell']}
dict1['three']=3
del(dict1['one'])

print(dict1)
print(dict1.keys())
print(dict1.values())



##set()
##unique elemnts
##not ordered like list and tuple
# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
B ={1,2,3,"sd",5.4}

print(type(B))  #set

album1= [ "Michael Jackson", "Thriller", 1982, "00:42:19"]
album2 = set(album1) # Convert list to set

album2.add(5)
album2.remove(1982)
print(1982 in album2) #false

# Find the intersections
album_set1=set()
album_set2=set()
###Methods
intersection = album_set1 & album2
album_set1.difference(album_set2)  
album_set1.union(album_set2)
album_set2.issubset(album_set1)     