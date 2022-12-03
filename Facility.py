
class Facility:
    def __init__(self, facility_name):
        self.facility_name = facility_name

    def displayFacilities():
        with open("facilities.txt", mode="r") as f:
            list_facility = []
            lines = f.readlines()
            for line in lines[1:]:
                f1 = Facility(line)
                list_facility.append(f1)
        for facility in list_facility:
            print(f"{facility.facility_name}")

    def addFacility():
        add = input("Enter the facility: ")
        facility = Facility(facility_name=add)
        with open("facilities.txt", mode="r") as f:
            list_facility = []
            lines = f.read().splitlines()
            for line in lines:
                f1 = Facility(line)
                list_facility.append(f1)
        list_facility.append(facility)
        Facility.writeListOffacilitiesToFile(list_facility)

    def writeListOffacilitiesToFile(list_facility):
        list_facilities_name = []
        for facility in list_facility:
            list_facilities_name.append(f"{facility.facility_name}\n")
        print(list_facilities_name)
        with open("facilities.txt", mode="w") as f:
            f.writelines(list_facilities_name)


Facility.displayFacilities()
Facility.addFacility()
Facility.displayFacilities()
