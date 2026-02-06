class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] #"Libro Mayor" - lista de transacciones.
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = sum(amount['amount'] for amount in self.ledger)
        return balance
    
    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False    
        
        self.ledger.append({'amount': -amount, 'description': description})
        return True
    
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f"Transfer from {self.name}")
        return True
    
    def check_funds(self, amount):
        if(self.get_balance() < amount):
            return False
        return True
    
    def __str__(self):
        result = self.name.center(30,'*') + '\n'
        for entry in self.ledger:
            amount = entry['amount']
            description = entry['description'][:23]
            result += f"{description:<23}{amount:7.2f}\n"
            total = sum(item["amount"] for item in self.ledger)
        result += (f"Total: {total}")

        return result
    
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent = []

    for category in categories:
        total_withdraw = sum(
            -item['amount'] for item in category.ledger if item['amount'] < 0
        )
        spent.append(total_withdraw)

    total_spent = sum(spent)
    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for percent in percentages:
            line += "•  " if percent >= level else "   "
        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        line = "     "
        for name in names:
            line += (name[i] if i < len(name) else " ") + "  "
        chart += line + "\n"

    return chart.rstrip("\n")


tech = Category('Tech')
food = Category('Food')
school = Category('School')
tech.deposit(50000,'deposit')
tech.withdraw(40000)
food.deposit(20000,'deposit')
food.withdraw(10000)
school.deposit(40000,'deposit')
school.withdraw(35000)

print(create_spend_chart([tech,food,school]))

