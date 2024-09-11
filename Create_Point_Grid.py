import arcpy
import math

# Set workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"
arcpy.env.overwriteOutput = True

# Input polygon feature class <click & drag single feature from TOC>
input_polygon = 

# Temporary fishnet feature class
temp_fishnet = "temp_fishnet"

# Output point feature class
output_points = "output_points"

# Function to calculate grid spacing based on polygon area and required number of points
def calculate_grid_spacing(polygon, min_points):
    area = 0
    with arcpy.da.SearchCursor(polygon, ["SHAPE@"]) as cursor:
        for row in cursor:
            area = row[0].area
    spacing = math.sqrt(area / min_points)
    return spacing

# Get the grid spacing
spacing = calculate_grid_spacing(input_polygon, 200)

# Get the extent of the input polygon
extent = arcpy.Describe(input_polygon).extent
origin_coord = f"{extent.XMin} {extent.YMin}"
y_axis_coord = f"{extent.XMin} {extent.YMin + 1}"
corner_coord = f"{extent.XMax} {extent.YMax}"

# Create a fishnet (polygon grid)
arcpy.CreateFishnet_management(
    out_feature_class=temp_fishnet,
    origin_coord=origin_coord,
    y_axis_coord=y_axis_coord,
    cell_width=spacing,
    cell_height=spacing,
    number_rows="",
    number_columns="",
    corner_coord=corner_coord,
    labels="NO_LABELS",
    template=input_polygon,
    geometry_type="POLYGON"
)

# Select fishnet cells within the polygon
selected_fishnet = "selected_fishnet"
arcpy.SelectLayerByLocation_management(
    in_layer=temp_fishnet,
    overlap_type="INTERSECT",
    select_features=input_polygon,
    selection_type="NEW_SELECTION"
)

# Save the selected fishnet cells to a new feature class
arcpy.CopyFeatures_management(temp_fishnet, selected_fishnet)

# Convert the selected fishnet cells to points (centroids)
arcpy.FeatureToPoint_management(
    in_features=selected_fishnet,
    out_feature_class=output_points,
    point_location="CENTROID"
)

print(f"Grid of points created and saved to {output_points}")

# Select final plot points cells within the polygon
arcpy.SelectLayerByLocation_management(
    in_layer=output_points,
    overlap_type="WITHIN",
    select_features=input_polygon,
    selection_type="NEW_SELECTION"
)

# Delete the feature classes
arcpy.Delete_management("temp_fishnet")
arcpy.Delete_management("selected_fishnet")
 





