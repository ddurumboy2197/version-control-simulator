import pandas as pd

class BatchDataProcessor:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def filter_data(self, column, value):
        return self.data[self.data[column] == value]

    def sort_data(self, column):
        return self.data.sort_values(by=column)

    def group_data(self, column):
        return self.data.groupby(column)

    def aggregate_data(self, column, func):
        return self.data.groupby(column)[func]

    def save_data(self, filename):
        self.data.to_csv(filename, index=False)

# Misol uchun ma'lumotlar
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna'],
    'age': [25, 30, 35, 20, 25, 30],
    'city': ['New York', 'London', 'Paris', 'New York', 'London', 'Paris']
}

# Batch Data Processor yaratish
processor = BatchDataProcessor(data)

# Ma'lumotlarni filtrlovchi
filtered_data = processor.filter_data('name', 'John')
print(filtered_data)

# Ma'lumotlarni tartiblash
sorted_data = processor.sort_data('age')
print(sorted_data)

# Ma'lumotlarni guruhlash
grouped_data = processor.group_data('city')
print(grouped_data)

# Ma'lumotlarni agregatsiyalash
aggregated_data = processor.aggregate_data('age', 'mean')
print(aggregated_data)

# Ma'lumotlarni saqlash
processor.save_data('data.csv')
