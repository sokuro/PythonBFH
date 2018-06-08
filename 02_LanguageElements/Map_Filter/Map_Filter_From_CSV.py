"""
    Using Iterators to:
        > avoid materialize all Records from File in Memory
        > avoid reading in Records as a List
"""
from collections import namedtuple

SalesRecord = namedtuple('SalesRecord', 'transaction_id date time customer_id department amount')


def process_sales_query(file_name, query_func, *query_func_args):
    """
        Open the specified sales CSV file and parses it, generates a iterator of SalesRecord which
        it then passes to query_func along with query_func_args.
    """
    with open(file_name) as file:
        next(file)  # skip header line (the first line in the file)

        # split each text line at the comma (',') -> turns each text line into an array of strings
        split_strings = map(lambda line: line.split(','), file)

        # Parse the array for each record and create a SalesRecord named tuple
        # (parse substring list into record)
        records = map(lambda record_array: SalesRecord(transaction_id=int(record_array[0]),
                                                       date=record_array[1],
                                                       time=record_array[2],
                                                       customer_id=int(record_array[3]),
                                                       department=record_array[4],
                                                       amount=float(record_array[5])), split_strings)
        query_func(records, *query_func_args)


"""
    Pretty format print the supplied SalesRecord.
"""
def pretty_print_sales_record(record):
    print(f'{record.transaction_id:>5} {record.date:>12} {record.time:>10} '
          f'{record.customer_id:>3} {record.department:>12} '
          f'{record.amount:7.2f}')


"""
    List all purchases made by one specific customer.
"""
def list_purchases_of_customer(sales_records_iter, customer_id):
    sales_for_customer = filter(lambda s: s.customer_id == customer_id, sales_records_iter)
    for record in sales_for_customer:
        # print(record)
        pretty_print_sales_record(record)


def main():
    FILE_NAME = 'mocksales.csv'
    process_sales_query(FILE_NAME, list_purchases_of_customer, 23)


main()