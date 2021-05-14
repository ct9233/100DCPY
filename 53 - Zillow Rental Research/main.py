from apartment_research import ApartmentResearch
from data_compiler import DataCompiler

apartment_research = ApartmentResearch()

apartment_research.get_data()
links = apartment_research.links
prices = apartment_research.prices
addresses = apartment_research.addresses

data_compiler = DataCompiler()

for i in range(len(links)):
    data_compiler.write_data(addresses[i], prices[i], links[i])