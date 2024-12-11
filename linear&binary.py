def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   for i in range(n):
      x = int(input("Enter the  roll no of student %d : "%(i+1)))
      A.append(x)
   print("Student Info accepted successfully\n\n")
   return n


def display_array(A,n): 
   if(n == 0) :
      print("\nNo records in the database")
   else :
      print("Students  Array : ",end=' ')
      for i in range(n) :
         print("%d  "%A[i],end=' ')
      print("\n");




def Linear_Search(A,n,X) :
   for i in range(n) :
      if(A[i] == X) :
         return i      # found so returning the position i.e index
   return -1       # Not  found
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


def Main() :   
   A = []
   while True :
      print ("\t1 : Accept & Display Students info ")      
      print ("\t2 : Linear Search")
      print ("\t3 : Binary Search")
      print ("\t4 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 4):
         print ("End of Program")
         quit()
      elif (ch==1):
         A = []
         n = accept_array(A)
         display_array(A,n)
      elif (ch==2):
         X = int(input("Enter the roll_no to be searched : "))
         Ls = Linear_Search(A,n,X)
         if(Ls == -1) :
            print("\tRoll no to be Searched not Found\n")
         else :
            print("\tRoll no found at location %d"%(Ls + 1))
      elif (ch==3):
         X = int(input("Enter the roll_no to be searched : "))
         Bs  = binary_search(arr, low, high, x)
         if(bs == -1) :
            print("\tRoll no to be Searched not Found\n")
         else :
            print("\tRoll no found at location %d"%(Bs+ 1))            
      else :
           print ("Wrong choice entered !! Try again")




Main()
