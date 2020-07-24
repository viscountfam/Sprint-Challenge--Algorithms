#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) this problem has a time complexity of O(n) it is linear because once you eliminate the extra ns it ends up being
while(a < n)
    a = a + 1


b) this problem has a time complexity of O(n * log(n)) the outer for loop has a time complexity of O(n) and the inner while loop has a time complexity of O(log(n)) when you multiply the two by each other you get O(n * log(n)) because they are nested loops


c) The time complexity of a recursive function is O(the number of recursive calls raised to the nth power) so in this case O(1^(n))


## Exercise II

one possible solution is to create a function that returns all the floors that are above the height from which you can safely drop an egg.

you'd need to subtract the number of the last floor where you could safely drop eggs from from n which here is the number of floors in the building o(1)

then you could use a for loop or a list comprehension to return all the floors above the safe drop zone o(n - drop height)

this solution would have a time complexity of O(n)

another possible solution is to start at the middle floor of the building

mid = n // 2 if we drop an egg from the middle floor and it doesn't break we
move to the midpoint between the middle floor and the top floor if the egg breaks on the floor between the middle and the top we check the middle floor between the middle floor and the floor that we just dropped an egg from. we keep doing this until we find a floor that the egg doesn't break on
this solution would have an O(log(n)) time complexity because we are using a binary solution

