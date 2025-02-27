class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        foods, tables = set(), dict() 
        for _, table_number, food_item in orders:
            table_number = int(table_number)
            if table_number not in tables:
                tables[table_number] = Counter()
            tables[table_number][food_item] += 1
            foods.add(food_item)

        tables_sorted = sorted(tables.keys())
        foods_sorted = sorted(list(foods))

        res = [['Table']]
        res[0].extend(foods_sorted)

        for table in tables_sorted:
            temp = [str(table)]
            for food in foods_sorted:
                temp.append(str(tables[table][food]))
            res.append(temp)
        return res