class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        # customers = set()
        tables = set()

        mp = {} # int: collections.Counter
        for customer_name, table_number, food_item in orders:
            if table_number not in mp:
                mp[table_number] = collections.Counter()
            mp[table_number][food_item] += 1

            foods.add(food_item)
            # customers.add(customer_name)
            tables.add(int(table_number))

        tables_sorted = sorted(list(tables))
        foods_sorted = sorted(list(foods))

        res = [['Table']]
        res[0].extend(foods_sorted)

        for table in tables_sorted:
            temp = [str(table)]
            for food in foods_sorted:
                temp.append(str(mp[str(table)][food]))
            res.append(temp)
        return res