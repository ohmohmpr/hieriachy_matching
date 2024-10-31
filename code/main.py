from hierarchical_grouping.file_reader import BinaryPolygonFileReader

#set file path
'''
    Name,            number of sets
    data_auerberg,              796
    data_dottendorf,            871
    data_duisdorf,             2127
    data_endenich,             1060
    data_zentrum,               160
'''
file_path = "data/data_zentrum"
                                
#initialize reader
reader = BinaryPolygonFileReader(file_path)

# while True:
#     try:
#         set_id, polys1, polys2 = reader.read_next_set()
#         print("set id: ",set_id)
#         # print("length of polys1: ", len(polys1))
#         # print("length of polys2: ", len(polys2))
#     except:
#         break

set_id, polys1, polys2 = reader.read_next_set()

'''
    Dataset = data_zentrum
    set_id, polys1, polys2
    0,           4,      4
    1,           7,      6
'''

# Output the results
print("First Set of Polygons:")
for poly in polys1:
    # print(poly)
    print(poly.area)

print("\nSecond Set of Polygons:")
for poly in polys2:
    # print(poly)
    print(poly.area)