people = {
    "Ellen Marchner":{"born":1998, "country":"USA", "mother":"Alice Chang", "father":"John Marchner Jr."},
    "John Marchner III":{"born":2001, "country":"USA", "mother":"Alice Chang", "father":"John Marchner Jr."},
    "John Chang":{"born":1999, "country":"USA", "father":"Felix Chang", "mother":"Ethel Kim"},
    "Ethel Kim":{"born":1970, "country":"Korea", "father":"Hyojin Kim", "mother":"Kon Chu"},
    "Felix Chang":{"born":1968, "country":"USA", "mother":"Wenli Muramoto", "father":"Hong Ho Chang"},
    "Alice Chang":{"born":1971, "country":"USA", "mother":"Wenli Muramoto", "father":"Hong Ho Chang"},
    "John Marchner Jr.":{"born":1969, "country":"USA", "father":"John Marchner", "mother":"Mary Schmidt"},
    "Kon Chu":{"born":1941, "died":2012, "country":"Korea", "mother":"Woko Chu"},
    "Hyojin Kim":{"born":1941, "died":2011, "country":"Korea"},
    "Wenli Muramoto":{"born":1938, "died":2001, "country":"China", "father":"Seiji Muramoto", "mother":"Keiko Kawasaki"},
    "Hong Ho Chang":{"born":1936, "died":1997, "country":"China", "father":"Song Chan", "mother":"Mariko Hosugawa"},
    "Mary Schmidt":{"born":1944, "died":2017, "country":"Germany", "mother":"Marie Dupre", "father":"Karl Schmidt"},
    "John Marchner":{"born":1942, "died":2008, "country":"Germany", "father":"Thomas Marchner", "mother":"Elizabeth Koenig"},
    "Woko Chu":{"born":1909, "died":1942, "country":"Korea"},
    "Keiko Kawasaki":{"born":1914, "died":1989, "country":"Japan"},
    "Seiji Muramoto":{"born":1915, "died":1944, "country":"Japan"},
    "Mariko Hosugawa":{"born":1910, "died":1987, "country":"Japan"},
    "Song Chang":{"born":1907, "died":1976, "country":"China"},
    "Marie Dupre":{"born":1921, "died":1998, "country":"France"},
    "Karl Schmidt":{"born":1920, "died":1987, "country":"Germany"},
    "Elizabeth Koenig":{"died":1995},
    "Thomas Marchner":{"born":1916, "died":1988, "country":"Germany"}
    }
def merge(A, B):
    for country in B:
        if country in A:
            A[country] += B[country]
        else:
            A[country] = B[country]
    return
def search(name):
    global input_name
    country_counts = {}
    count = 0
    total_age = 0
    if name not in people:
        return (country_counts, count, total_age)
    if name != input_name and "country" in people[name]:
        country_counts[people[name]["country"]] = 1
    if name != input_name and "born" in people[name] and "died" in people[name]:
        count = 1
        total_age = people[name]["died"] - people[name]["born"]
    if "father" in people[name]:
        father = people[name]["father"]
        (f_country_counts, f_count, f_total_age) = search(father)
        merge(country_counts, f_country_counts)
        count += f_count
        total_age += f_total_age
    if "mother" in people[name]:
        mother = people[name]["mother"]
        (m_country_counts, m_count, m_total_age) = search(mother)
        merge(country_counts, m_country_counts)
        count += m_count
        total_age += m_total_age
    return (country_counts, count, total_age) 
while True:
    input_name = input("Enter the name to search: ")
    if input_name == "":
        break
    if input_name in people:
        (country_counts, count, total_age) = search(input_name)
        if count:
            print("The ancestors of %s have average age %.1f" %
                  (input_name, total_age/count))
        total_country_count = 0
        for country in country_counts:
            total_country_count += country_counts[country]
        if total_country_count:
            print("The national ancestry of", input_name, "is:")
            for country in country_counts:
                percent = 100.0*country_counts[country]/total_country_count
                print("   %s: %.1f%%" % (country, percent))
    else:
        print(input_name, "was not found in the people data base.")
    
