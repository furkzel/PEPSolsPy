import time

def is_it_palindrome(obj):
    if str(obj) == str(obj)[::-1]:
        return True
    else:
        return False
    
def main():
    return [x * y for x in range(100, 1000) for y in range(100, 1000) if is_it_palindrome(x * y)]

if __name__ == "__main__":
    start = time.time()
    print(max(main()))
    print(time.time() - start)
