For use in notebooks in Arc Pro .

Creates point grid shapefile for a polygon area of interest. 

Original use: to create 200 plot points on a map for soil disturbance surverys.

PROMPT FOR PYTHON CODE CREATION:

Can you write a Python script using ArcPy to be used in Arc Pro Notebook that creates a grid of evenly spaced points within a polygon feature class? The script should:

1. Have arcpy overwrite = to True.
2. Take an input polygon feature class.
3. Calculate a grid spacing based on the polygon area and a minimum number of points (200).
4. Create a fishnet grid with the calculated spacing.
5. Convert the cells to points (centroids).
6. Select only the points that fall within the input polygon.
7. Save the final points as a new feature class.
8. Clean up any "working files" from the gdb (do not use in_memory).

Please include error handling and print comments explaining each step of the process.
