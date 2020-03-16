
from CollectionClass import ClassInventory,ClassIO



choiseUser=int(input("1-сведения о мячах;"
                           "2- сведения о скамейках;"
                           "3 - сведения о матах;"
                           "4 - сведения о брусьях: \n"))
if choiseUser==1:
    array = ClassIO.IO.funRead(choiseUser)
    for i in range(len(array)):
        array_2=array[i].split(",")
        ob=ClassInventory.Ball(array_2[0],int(array_2[1]), int(array_2[2]),array_2[3],array_2[4])
        print(ob.get())
        print()
elif choiseUser==2:
    array = ClassIO.IO.funRead(choiseUser)
    for i in range(len(array)):
        array_2 = array[i].split(",")
        ob = ClassInventory.Bench(array_2[0], int(array_2[1]), int(array_2[2]), array_2[3], array_2[4])
        print(ob.get())
        print()
elif choiseUser == 3:
    array = ClassIO.IO.funRead(choiseUser)
    for i in range(len(array)):
        array_2 = array[i].split(",")
        ob = ClassInventory.Mates(array_2[0], int(array_2[1]), int(array_2[2]), array_2[3], array_2[4],
                                  array_2[5],array_2[6])
        print(ob.funGetMates())
        print()
elif choiseUser == 4:
    array = ClassIO.IO.funRead(choiseUser)
    for i in range(len(array)):
        array_2 = array[i].split(",")
        ob = ClassInventory.Skids(array_2[0], int(array_2[1]), int(array_2[2]), array_2[3], array_2[4], array_2[5])
        print(ob.funGetSkids())
        print()



