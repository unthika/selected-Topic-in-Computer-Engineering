import xml.dom.minidom
dom = xml.dom.minidom.parse('MovieAll_SPN.xml')

for movie in dom.getElementsByTagName("movie"):
    print(movie.getElementsByTagName("name")[0].childNodes[0].data)
    print ("\tType:")
    for type_ in movie.getElementsByTagName("type"):
        print("\t\t"+type_.childNodes[0].data)
    print ("\tMain character:")
    for name_actor in movie.getElementsByTagName("name_actor"):
        print("\t\t"+name_actor.childNodes[0].data)
    print ("\tDirector:")
    print ("\t\t"+movie.getElementsByTagName("director")[0].childNodes[0].data)
    print ("\tDate:")
    day = movie.getElementsByTagName("day")[0].childNodes[0].data
    month = movie.getElementsByTagName("month")[0].childNodes[0].data
    year = movie.getElementsByTagName("year")[0].childNodes[0].data
    print ("\t\t"+day+"-"+month+"-"+year)
    print("==============================")


