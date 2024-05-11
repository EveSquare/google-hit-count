from main import GoogleSearch

if __name__ == "__main__":
    test1 = GoogleSearch("Google").get_hit_count()

    if test1 == 0:
        print("Test 1 failed")

    test2 = GoogleSearch("Python").get_hit_count()

    if test2 == 0:
        print("Test 2 failed")

    test3 = GoogleSearch(
        "4356uiyikh,mbnvcdsrgdth4vt4eta4tbabt3q4t3abyb75ieeay-0497839*^&%^&$%^$$^*%&^(*&)("
    ).get_hit_count()

    if test3 != 0:
        print("Test 3 failed")

    print("All tests passed")
