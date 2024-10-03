def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Start the new row with a 1
        new_row = [1]
        
        # Compute the values inside the row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        # End the row with a 1
        new_row.append(1)
        # Add the new row to the triangle
        triangle.append(new_row)
    
    return triangle
