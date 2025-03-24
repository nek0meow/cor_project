import csv

from web.models import Customer


def filter_customers(customers, filters):
    if filters["search"]:
        customers = customers.filter(customer_name__icontains=filters["search"])

    return customers


def export_customers_csv(customers_qs, response):
    writer = csv.writer(response)
    writer.writerow(
        ("customer_name", "customer_email", "customer_phone", "customer_address")
    )
    for customer in customers_qs:
        writer.writerow(
            (
                customer.customer_name,
                customer.customer_email,
                customer.customer_phone,
                customer.customer_address,
            )
        )

    return response


def import_customers_from_csv(file):
    strs_from_file = (row.decode() for row in file)
    reader = csv.DictReader(strs_from_file)

    customers = []
    for row in reader:
        customers.append(
            Customer(
                customer_name=row["customer_name"],
                customer_email=row["customer_email"],
                customer_phone=row["customer_phone"],
                customer_address=row["customer_address"],
            )
        )
    Customer.objects.bulk_create(customers)
