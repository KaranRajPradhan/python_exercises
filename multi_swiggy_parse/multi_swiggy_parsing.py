from tika import parser
from parse import parse
from pprint import pprint
import os
import json
 
def do_simple_parsing(clean_lines, filter_list):
    order_details = {}
    for text_filter in filter_list:
        for line in clean_lines:
            result = parse(text_filter, line)
            if result:
                order_details.update(result.__dict__["named"])
    return order_details
 
def get_elements_in_between(starts_with, ends_with, clean_lines):
    for line in clean_lines:
        if starts_with == line:
            start_index = clean_lines.index(line) + 1
        elif ends_with in line:
            end_index = clean_lines.index(line)
    elements_in_between = clean_lines[start_index: end_index]
    return elements_in_between
 
def get_place_details(clean_lines):
    starts_with = "Ordered from:"
    ends_with = "Item Name Quantity Price"
    address_list = get_elements_in_between(starts_with, ends_with, clean_lines)
    place_details = {}
    place_details["place_name"] = address_list[0]
    place_details["place_address"] = " ".join(address_list[1:])
    return(place_details)
 
def get_order_item_details(clean_lines):
    starts_with = "Item Name Quantity Price"
    ends_with = "Item Total:"
    items = get_elements_in_between(starts_with, ends_with, clean_lines)
    items_processed = []
    for item in items:
        item_details = {}
        item_splitted = item.split("₹")
        item_details["name"] = " ".join(item_splitted[0].strip().split(" ")[:-1])
        item_details["price"] = item_splitted[-1].strip()
        item_details["quantity"] = item_splitted[0].strip().split(" ")[-1]
        items_processed.append(item_details)
    return(items_processed)
 
def get_recepient_address(clean_lines):
    starts_with = "Delivery To:"
    ends_with = "Disclaimer:"
    recepient_address_list = get_elements_in_between(starts_with, ends_with, clean_lines)
    recepient_address = " ".join(recepient_address_list)
    return(recepient_address)
 
def parse_swiggy_bill(filename):
    parsed = parser.from_file(filename)
    splitted = parsed["content"].split("\n")
    clean_lines = [line for line in splitted if len(line) != 0]
    filter_list = ["Order No: {order_no}", "Order placed at: {order_date}, {order_time} {order_am_pm}",
               'Order Status: {order_status}', 'Item Total: ₹  {order_total}', 'GST: ₹  {gst}',
               'Order Packing Charges: ₹  {packing_charge}', 'Delivery Charges: ₹  {delivery_charge}']
   
    parsed_data = {
    'order_details' : do_simple_parsing(clean_lines, filter_list),
    'place_details' : get_place_details(clean_lines),
    'ordered_item_details' : get_order_item_details(clean_lines),
    'recepient_address' : get_recepient_address(clean_lines)
    }
    return parsed_data
 
if __name__ == "__main__":
    current_dir = os.getcwd()
    os.chdir("pdf_files")
    file_list = os.listdir()
    result_list = {}

    for files in file_list:
        try:
            result = parse_swiggy_bill(files)
            result_list[files] = result
        except UnboundLocalError as e:
            print(e)
            continue

    os.chdir(current_dir)

    pprint(result_list)
    swiggy_data = open("swiggy_data.json", 'w')
    json_data = json.dumps(result_list)
    swiggy_data.write(json_data)
    swiggy_data.close()
    
    # OR
    # with open("swiggy_data.json", 'w') as file_object:
    #     file_object.write(json.dumps(result_list))


