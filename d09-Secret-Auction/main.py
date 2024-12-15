import os


def get_best_bidder(auctions):
    sorted_bidders = sorted(
        auctions.items(), key=lambda key: key[1], reverse=True)
    best_bidder_name, value = sorted_bidders[0], sorted_bidders[1]
    print(f'The winner is {best_bidder_name} with a bid of ${value}')


logo = '''
                         ___________
                         \                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

auctions = {}
run = True

print(logo)
while run:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $ "))
    auctions[name] = bid

    other_bidders = input("Are there any other bidders? yes or no").lower()

    if other_bidders == "yes":
        os.system('clear')
    else:
        run = False
        get_best_bidder(auctions)
