def determine_triangle_type(side1: float, side2: float, side3: float) -> str:
    if side1 == side2 == side3:
        return "triangle equilatéral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "triangle isocèle"
    else:
        return "triangle scalène"