# [ {x + (1/y)}^a  *  {x – (1/y)}^b ]  /  [ {y + (1/x)}^a  *  {y – (1/x)}^b ]
# On reducing the given equation it becomes (x/y)^(a+b)

x,y,a,b = [int(z) for z in input().split()]

def deirectimplement(x,y,a,b):
    part1 = ( (x + (1/y))**a ) * ( (x - (1/y))**b )
    part2 = ( (y + (1/x))**a ) * ( (y - (1/x))**b )

    return part1/part2

def reducedimplement(x,y,a,b):
    answer = (x/y)**(a+b)
    return answer

# use any of the method to get the answer for the equation
answer1 = deirectimplement(x,y,a,b)
answer2 = reducedimplement(x,y,a,b)

print(answer1,answer2)
