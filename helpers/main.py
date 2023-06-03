from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Return response data
def response_data(status, detail, data=None):
    response_dict = {"status": status, "detail": detail}
    if data is not None:
        response_dict["data"] = data

    return response_dict


# Function to return paginated data
def paginate_data(data, page_number, items_per_page):
    # Pass the data to the paginator module
    paginator = Paginator(data, items_per_page)
    try:
        # Get data specific to page number
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        # Return first page in any exception
        page = paginator.page(1)

    # Get data details after paginated
    try:
        total_data = data.count()
    except TypeError:
        total_data = len(data)

    # Get total number of pages
    total_pages = paginator.num_pages

    # Convert data to list
    data_paginated = list(page)

    # Create an object to be returned
    response_data = {
        "status": "success",
        "detail": "Data fetched successfully",
        "current_page": page.number,
        "total_data": total_data,
        "total_pages": total_pages,
        "data": data_paginated,
    }

    # Return paginated data details
    return response_data
