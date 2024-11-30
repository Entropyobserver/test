def linear_search(lst, target):
	for element in lst:
		if element == target:
				return True
	return False
"""
def linear_search_r(lst,n,target):
    try:
        lst[n]
        lst[n] == target
        return True
    except:
        return linear_search_r(lst,n+1,target)
"""

def linear_search_r(lst,n,target):
    if lst[n] ==target:
        return True
    return linear_search_r(lst,n+1,target)
#1.everytime compare target with lst[n]
#use n to control how many times we should call this fuction
#n < 3 it works well,n > 4 list index out of range
#

def main():
    test = [4,56,23,6,7235,73]
    print(linear_search(test,6))
    print(linear_search_r(test,4,6))

main()