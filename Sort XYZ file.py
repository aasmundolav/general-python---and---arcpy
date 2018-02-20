def sortasciixyz(infile, outfile, seperator):
    comments = ""
    try:
        array=[]        
        count = 0
        with open(infile,"r") as i:
            for l in i:
                count +=1
                if len(l) > 0:
                    array.append(l.split(seperator))
                else:
                    comment += "\nempty line %s" % count
                    print("empty line %s" % count)
        print("number of lines %s" % len(array))
        comments += "number of lines %s" % len(array)
        from operator import itemgetter

        sortedArray1 = sorted(array, key=itemgetter(1))
        #sortedArray = sorted(sortedArray1, key=itemgetter(0))
        with open(outfile,"w") as u:
            for b in sortedArray1:
                u.write(seperator.join(b))
        return True, comments
    except:
        return False, comments



sortasciixyz(r"D:\MARIA\DTMs\AFC_Route_Prelay_KP_0dot000_to_KP0dot492_DTM.xyz",r"D:\MARIA\DTMs\AFC_Route_Prelay_KP_0dot000_to_KP0dot492_DTM3.xyz", " ")
