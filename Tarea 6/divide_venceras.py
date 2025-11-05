def max_product_divide_conquer(arr):
    if len(arr) < 2:
        return (None, None, float('-inf'))
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    a1, a2, prod_left = max_product_divide_conquer(left)
    b1, b2, prod_right = max_product_divide_conquer(right)
    max_left, min_left = max(left), min(left)
    max_right, min_right = max(right), min(right)
    cross_candidates = [
        (max_left, max_right, max_left * max_right),
        (min_left, min_right, min_left * min_right)
    ]
    best_pair = max(
        [(a1, a2, prod_left), (b1, b2, prod_right)] + cross_candidates,
        key=lambda x: x[2]
    )
    
    return best_pair

arr = [10,2,3,4,5,6,7,8]
num1, num2, producto = max_product_divide_conquer(arr)
print(f"Los números con el mayor producto son {num1} y {num2}, con producto = {producto}")