class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        foods, tables, mp = set(), set(), dict() 
        for customer_name, table_number, food_item in orders:
            int_table_number = int(table_number)
            if int_table_number not in mp:
                mp[int_table_number] = collections.Counter()
            mp[int_table_number][food_item] += 1
            foods.add(food_item)
            tables.add(int_table_number)

        tables_sorted = sorted(list(tables))
        foods_sorted = sorted(list(foods))

        res = [['Table']]
        res[0].extend(foods_sorted)

        for table in tables_sorted:
            temp = [str(table)]
            for food in foods_sorted:
                temp.append(str(mp[table][food]))
            res.append(temp)
        return res